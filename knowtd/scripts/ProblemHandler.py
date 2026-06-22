import json
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.utils.inference_utils import infer_all_slot_values, Config
from linkml.validator import validate_file, validate
import yaml

from itertools import product 

import thermo_ontology as thm
import re

class ProblemHandler:
    def __init__(self, ontology_filename, problem_filename):
        '''Loads a problem from file and checks it agains an ontology. 
        Problem can either be filepath to a yaml file or the content of the yaml file itself.
        '''
        self.schemaview = SchemaView(ontology_filename)
        self.schemaview.imports_closure()

        #validate file
        # input can be yaml or file path.
        if isinstance(problem_filename, str) and problem_filename.lower().endswith(('.yml', '.yaml')):
            with open(problem_filename, 'r') as f:
                try:
                    data = yaml.safe_load(f)
                    report = validate_file(file=problem_filename, schema=self.schemaview.materialize_derived_schema(), target_class=data['problem_class'])
                except yaml.YAMLError as e:
                    raise ValueError(f"Invalid YAML in file: {e}")
        elif isinstance(problem_filename, str) and "problem_class:" in problem_filename:
            match = re.search(r'problem_class:\s*(\S+)', problem_filename)
            problem_class = match.group(1) if match else None
            try:
                problem_data = yaml.safe_load(problem_filename)
            except yaml.YAMLError as e:
                raise ValueError(f"Invalid YAML content: {e}")
            report = validate(instance=problem_data, schema=self.schemaview.materialize_derived_schema(), target_class=problem_class)
        elif isinstance(problem_filename, dict):
            problem_class = problem_filename['problem_class']
            report = validate(instance=problem_filename, schema=self.schemaview.materialize_derived_schema(), target_class=problem_class)
        else:
            raise SyntaxError('The specified input cannot be imported.')
        
        if report.results:
            messages = [result.message for result in report.results]
            raise SyntaxError('The specified problem is invalid: \n    ' + "\n    ".join(messages))

        self.problem = yaml_loader.load(problem_filename, target_class=thm.Problem)
        # print(self.problem)
        self.known_instances = {}
        self.instance_count = {}
        self.equation_view = None

        self._collect_instances()
        self._init_missing_items()

    def instances(self, onto_class=None):
        for node in self.known_instances.values():
            node_ancestors = self.schemaview.class_ancestors(self.get_class_name(node))
            if (onto_class is None) or (onto_class in node_ancestors):
                yield node

    def get_class_name(self, obj):
        return obj.__class__.__name__
    
    def create_equations(self):
            eqns = []
            concepts = list(self.instances('Concept'))
            for instance in concepts:
                # iterate over all possible equations
                for eqn_slot in [slot for slot in instance if 'object_references' in (self.schemaview.get_slot(slot).in_subset or [])]:
                    eqn = self.schemaview.get_slot(eqn_slot).range
                    required_objects = {slot.name for slot in self.schemaview.class_induced_slots(eqn) if 'equation_references' in (slot.in_subset or [])} # which objects does the equation require?
                    objects_of_equation = [] # which specific objects does the equation use? List of combinations, as the equation can be initialized multiple times
                    #related_objects = [self.known_instances[r] for r in self._get_all_related_instances(instance)] # all potential used objects (have to be related to the instance)
                    related_objects = self._get_object_has_instances(instance)

                    # get all possible instances of the required objects
                    is_applicable = True
                    for required_object in required_objects:
                        required_range = self.schemaview.induced_slot(required_object, eqn).range
 
                        object_list = []
                        # use the instance to which the equation belongs
                        if required_range in self.schemaview.class_ancestors(instance.class_name):
                            object_list = [instance]
                        else:
                            # for all other required_objects only use related objects of this instance.
                            for ro in related_objects:
                                if not ro in object_list and required_range in self.schemaview.class_ancestors(self.get_class_name(ro)):
                                    object_list.append(ro) 
                        if object_list == []:
                            is_applicable = False
                        objects_of_equation.append([(ro, required_object) for ro in object_list])
                    
                    if is_applicable:
                        # create equations for each combination
                        established_equations = []
                        for combination in list(product(*objects_of_equation)):
                            format_map = dict()
                            mapping = dict()
                            for elem in combination:
                                # format_map contains mappings for string replacement in the equation text
                                elem_1_name = elem[1] if not elem[1].endswith('_id') else elem[1][:-3]
                                format_map[elem_1_name] = elem[0].id
                                format_map.update(self._get_format_map(elem[0], elem_1_name))
                                # mapping contains slots of the equation
                                mapping[elem[1]] = elem[0]
                            if required_objects.issubset(mapping):
                                # check rules
                                if self._check_rule(eqn, mapping):
                                    # create equation
                                    eqn_id = self._create_id_before_obj(eqn)
                                    eqn_object = getattr(thm, eqn)(id=eqn_id, **{e1: mapping[e1].id for e1 in mapping})
                                    self.known_instances[eqn_object.id] = eqn_object
                                    eqn_object.as_text = self.schemaview.induced_slot(class_name=eqn, slot_name='as_text').ifabsent.replace('string(', '')[:-1] # linkml > 1.8.2 is not able to handle brackets in ifabsent in python generator
                                    if 'ModularSumEquation' in self.schemaview.class_ancestors(eqn):
                                        # Modular equations should only refer to one object
                                        # this object contains slots for sum_variable, sum_parameters, sum_equals and iterator_set
                                        for slot in instance: 
                                            if 'sum_variable' in self.schemaview.slot_parents(slot):
                                                sum_variable = instance[slot].replace('#iterator', '{}')
                                            elif 'iterator_set' in self.schemaview.slot_parents(slot):
                                                iterator_set = instance[slot]
                                            elif 'sum_equals' in self.schemaview.slot_parents(slot):
                                                sum_equals = instance[slot]
                                            elif 'parameter_set' in self.schemaview.slot_parents(slot):
                                                parameter_set = instance[slot]
                                            
                                        if parameter_set == None or parameter_set == []:
                                            parameter_set = [1] * len(iterator_set)
                                        elif len(parameter_set) != len(iterator_set):
                                            raise ValueError(f'The amount of specified parameters does not match the size of the iterator_set.\n{parameter_set=}\n{iterator_set=}')
                                        eqn_object.as_text = " + ".join(str(parameter_set[index]) + ' * ' + sum_variable.format(iterator_set[index]) for index in range(len(iterator_set))) + f" = {sum_equals}"
                                    else:
                                        # replace elements in curly braces with the respective object id
                                        eqn_object.as_text = eqn_object.as_text.format_map(format_map)
                                    
                                    # add related variables to equation
                                    self._add_related_variables(eqn_object)
                                    
                                    eqns.append(eqn_object)
                                    established_equations.append(eqn_object)
                                    # print('created eqn', eqn_object.id, ' with', {m: mapping[m].id for m in mapping})
                    
                    # update the equation slot of the concept?
                    if len(established_equations) == 0:
                        instance[eqn_slot] = None
                    elif len(established_equations) == 1:
                        instance[eqn_slot] = established_equations[0]
                    else:
                        instance[eqn_slot] = established_equations

            # Add additional given equations
            for equation in self.problem.additional_equations:
                eqn = getattr(thm, 'AdditionalEquation')(id=self._create_id_before_obj('AdditionalEquation'),
                                                            as_text=equation)
                self.known_instances[eqn.id] = eqn
                eqns.append(eqn)
            return eqns


    def _get_format_map(self, obj, obj_map):
        '''Create dictionary mapping slots to their targets' ids. 
            Considers only slots with references to other objects.
        '''
        format_map = dict()
        slots = [s for s in self.schemaview.class_slots(self.get_class_name(obj)) if 'equation_references' in (self.schemaview.get_slot(s).in_subset or [])]
        
        for s in slots:
            if hasattr(obj[s],'id'):
                format_map[f'{obj_map}#{s}'] = obj[s].id
            elif isinstance(obj[s],str) or isinstance(obj[s],thm.extended_str):
                format_map[f'{obj_map}#{s}'] = obj[s]
            # elif isinstance(obj[s], float) or isinstance(obj[s], int):
            #      format_map[f'{obj_map}#{s}'] = obj[s]
        format_map.pop(obj_map + '#id',None)
        return format_map

    def _get_object_has_instances(self, obj, closure=True):
        '''Returns a list containing all instances, that the object has 
        [and the instances themselves have (closure)]. 
        (using the has-a graph)
        '''
        instances = []
        for slot in obj:
            if not slot == 'id':
                slot_range = self.schemaview.get_slot(slot).range
                if slot_range and \
                    (not slot_range in ['boolean', 'string', 'float', 'integer']) and \
                    (not slot_range in self.schemaview.all_enums()) and \
                    ('Concept' in self.schemaview.class_ancestors(slot_range)):
                    contained_instance = obj[slot] # can be object, string (id) or list
                    if not(isinstance(contained_instance, list)):
                        if isinstance(contained_instance, str):
                            contained_instance = self._get_instance_by_id(obj[slot]) # get object if it is string
                        instances.append(contained_instance)
                        if closure:
                            instances += self._get_object_has_instances(contained_instance, closure)
                    else: # is list
                        for i in contained_instance:
                            list_elem = i # can be object or string
                            if isinstance(i, str):
                                list_elem = self._get_instance_by_id(i) # get object if it is string
                            instances.append(list_elem)
                            if closure:
                                instances += self._get_object_has_instances(list_elem, closure)
  
        return instances
    
    def _get_instance_has_object(self, obj, closure=True):
        '''Returns a list containing all instances, that have the object 
        [and all instances that have this instances (closure)] 
        (using the has-a graph)
        '''
        instances = []
        object_range = self.schemaview.class_ancestors(self.get_class_name(obj))
        for instance in self.instances('Concept'): #improvement: choose instances, with slot with range obj.class
            for slot in instance:
                if slot != 'id':
                    slot_range = self.schemaview.get_slot(slot).range
                    if slot_range in object_range: # object range has to match
                        if (    
                            instance[slot] == obj or
                            (isinstance(instance[slot], list) and obj['id'] in instance[slot]) or
                            (isinstance(instance[slot], str)  and obj['id'] == instance[slot])
                            ):
                            instances.append(instance)
                            if closure:
                                instances += self._get_instance_has_object(instance, closure)
        return instances
    
    def _get_all_related_instances(self, obj):
        '''Returns id's of all instances, that are related to the object.
        [All instances, that the object has and all instances that have the object (closure)].
        It first gets all instances, that have the object and then all instances, that these instances have.
        '''
        related_instances_has = [obj]
        related_instances_has += self._get_instance_has_object(obj, True)
        related_instances = []
        for instance in related_instances_has:
            related_instances.append(instance)
            related_instances += self._get_object_has_instances(instance, True)
        return {ri.id for ri in related_instances}

    def _get_instance_by_id(self, id):
        '''Returns the instance with the given id if it exists
        '''
        for instance in self.instances():
            if instance['id'] == id:
                return instance

    def _collect_instances(self):
        '''Parse the problem and store all known instances.
        '''
        # first collect all named instances provided by the user
        for instance in self._traverse_nodes():
            if hasattr(instance,'id') and instance.id:
                self.known_instances[instance.id] = instance

        # now collect the ones that don't have an id yet
        # assign ids on the fly
        for instance in self._traverse_nodes():
            if hasattr(instance,'id') and not instance.id:
                self._create_id(instance)

    def _init_missing_items(self):
        custom_config = Config(use_expressions=True)
        infer_all_slot_values(self.problem, self.schemaview, config=custom_config)
        if self.problem.valid_problem is None or self.problem.invalid_problem:
            raise SyntaxError(f"Problem file is not a valid {self.problem.problem_class} problem. Failed to satisfy the following constraint: {self.schemaview.induced_slot('valid_problem', self.problem.problem_class).equals_expression}")
        nodes = list(self.known_instances.values())
        while nodes:
            node = nodes.pop()
            #print(self.get_class_name(node))
            for slot in self.schemaview.class_slots(self.get_class_name(node)):
                tgt_class = self.schemaview.get_slot(slot).range
                is_class_reference = tgt_class in self.schemaview.all_classes()
                is_equation_reference = 'object_references' in (self.schemaview.get_slot(slot).in_subset or [])
                if is_class_reference and not is_equation_reference and (node[slot] is None):
                    node[slot] = getattr(thm, tgt_class)(id=self._create_id_before_obj(tgt_class, parent=node, slot=slot))
                    self.known_instances[node[slot].id] = node[slot]
                    if 'Element' in self.schemaview.class_ancestors(tgt_class):
                        nodes.append(node[slot])

    def _traverse_nodes(self, root=None):
        '''Traverse the knowledge graph stopping at each node.
        '''
        nodes = [root if root else self.problem]
        visited_nodes = set()
        while nodes:
            node = nodes.pop()

            # map reference to object if neccessary
            is_reference = (isinstance(node, str) or isinstance(node, thm.extended_str))
            if is_reference and node in self.known_instances:
                node = self.known_instances[node]
            # check that we have an ontology instance that has not been visited
            if not isinstance(node, thm.YAMLRoot) or id(node) in visited_nodes:
                continue
            
            # return the node and add it to the list of visited nodes
            visited_nodes.add(id(node))
            yield node

            # add children for traversal
            if not self.get_class_name(node) in self.schemaview.all_enums() and \
               not self.get_class_name(node) == 'PermissibleValue': 
                for slot in self.schemaview.class_slots(self.get_class_name(node)):
                    child = node[slot]
                    if child:
                        if isinstance(child, list):
                            nodes.extend(child)
                        else:
                            nodes.append(child)

    def _int_to_roman(self, num):
        lookup = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = ''
        for (n, roman) in lookup:
            (d, num) = divmod(num, n)
            res += roman * d
        return res

    def _create_id_before_obj(self, obj_class, parent=None, slot=None):
        '''Create an id for an Element, return it as a string.
        '''
        # init the counter if not yet available
        if not self.instance_count:
            self._init_instance_count()
        
        obj_ancestors = self.schemaview.class_ancestors(obj_class)
        # create ids for properties: <parent_id>_<slot_name>
        # e.g. System1_m
        if 'Variable' in obj_ancestors:
            new_id = f'{slot}_{parent.id}'
        else:
            self.instance_count[obj_class] += 1
            tgt_cnt = self.instance_count[obj_class]
            new_id = f'{tgt_cnt}'
            if 'EquationOfState' in obj_ancestors:
                new_id = f'EoS_{parent.id}'
            elif 'Material' in obj_ancestors:
                new_id = f'{self._int_to_roman(tgt_cnt).lower()}'
            elif 'System' in obj_ancestors:
                new_id = f'{self._int_to_roman(tgt_cnt)}'
            elif 'ChangeOfState' in obj_ancestors:
                new_id = chr(64+tgt_cnt)
            elif 'Equation' in obj_ancestors:
                new_id = f'{obj_class}{tgt_cnt}'
            elif 'Transition' in obj_ancestors:
                parent_change_of_state = parent
                new_id = f'{self._getattr_dot(parent_change_of_state,"initial_state.id")}{self._getattr_dot(parent_change_of_state,"final_state.id")}'        
        
        return new_id

    def _create_id(self, obj):
        '''Create an id for an Element.
        '''
        # print('Create id')
        # init the counter if not yet available
        if not self.instance_count:
            self._init_instance_count()

        obj_class = self.get_class_name(obj)
        obj_ancestors = self.schemaview.class_ancestors(obj_class)
        # create ids for properties: <parent_id>_<slot_name>
        # e.g. System1_m
        if 'Variable' in obj_ancestors or 'LogicalProperty' in obj_ancestors:
            parent,slot = self._find_parent(obj)
            obj.id = f'{slot}_{parent.id}'
            obj.is_required = f'{slot}_{parent.id}' in self.problem.required_variables
        else:
            self.instance_count[obj_class] += 1
            tgt_cnt = self.instance_count[obj_class]
            obj.id = f'{tgt_cnt}'
            if 'EquationOfState' in obj_ancestors:
                obj.id = f'EoS_{self._find_parent(obj)[0].id}'
            elif 'Material' in obj_ancestors:
                obj.id = f'{self._int_to_roman(tgt_cnt).lower()}'
            elif 'System' in obj_ancestors:
                obj.id = f'{self._int_to_roman(tgt_cnt)}'
            elif 'ChangeOfState' in obj_ancestors:
                obj.id = chr(64+tgt_cnt)
            elif 'Equation' in obj_ancestors:
                obj.id = f'{obj_class}{tgt_cnt}'
            elif 'Transition' in obj_ancestors:
                parent_change_of_state = self._find_parent(obj)[0]
                obj.id = f'{self._getattr_dot(parent_change_of_state,"initial_state.id")}{self._getattr_dot(parent_change_of_state,"final_state.id")}'

        # create ids for all other items: <class_name><class_count>
        # e.g. System1
        # else:        
        #     self.instance_count[obj_class] += 1
        #     tgt_cnt = self.instance_count[obj_class]
        #     obj.id = f'{tgt_cnt}'

        self.known_instances[obj.id] = obj
        return obj
    
    def _init_instance_count(self):
        self.instance_count = {c: 0 for c in self.schemaview.all_classes()}
        for c in self.known_instances.values():
            self.instance_count[self.get_class_name(c)] += 1
            
    def _find_parent(self, obj):
        for node in self.known_instances.values():
            for slot in self.schemaview.class_slots(self.get_class_name(node)):
                if (node[slot] == obj):
                    return (node,slot)
        raise Exception(f'Could not find parent of object {obj}.')

    def _get_valid_object_for_equation(self, eqn_name):
        for slot in self.schemaview.class_induced_slots(eqn_name):
            if slot.name == 'object':
                return slot.range
        return None   
    
    def _check_rule(self, eqn_name, mapping):
        '''Check if used objects satisfies all rules of the equation
        '''
        for ancestor in self.schemaview.class_ancestors(eqn_name):
            for rule in self.schemaview.get_class(ancestor).rules:
                if rule.preconditions.slot_conditions:
                    for slot,cond in rule.preconditions.slot_conditions.items(): # rule defines conditions for multiple slots
                        tgt_obj = self._getattr_dot_mapping(mapping=mapping, slot=slot)
                        # can be any combination of range, string, bool, any_of, none_of, exactly_one_of or all_of (see LinkML)
                        # all conditions must be met.
                        
                        # check range, string and bool conditions
                        if not self._check_cond(cond, tgt_obj):
                            return False
                        # any of
                        if cond.any_of:
                            val = False
                            for any_cond in cond.any_of:
                                if self._check_cond(any_cond, tgt_obj):
                                    val = True
                            if not val: # at least one true
                                return False
                        # none_of
                        if cond.none_of:
                            for non_cond in cond.none_of:
                                if self._check_cond(non_cond, tgt_obj):
                                    return False
                        # exactly_one_of
                        if cond.exactly_one_of:
                            val = False
                            for exact_cond in cond.exactly_one_of:
                                if self._check_cond(exact_cond, tgt_obj):
                                    if not val:
                                        val = True
                                    else: # at most one true
                                        return False
                            if not val: # at least one true
                                return False
                        # all_of
                        if cond.all_of:
                            for all_cond in cond.all_of:
                                if not self._check_cond(all_cond, tgt_obj):
                                    return False
        return True

    def _check_cond(self, cond, tgt_obj):
        """checks if the condition contains range, string or bool conditions. 
        All found conditions must be met.
        Return False if one is not met. Otherwise True.
        """
        # range conditions
        if cond.range and (not cond.range in self.schemaview.class_ancestors(self.get_class_name(tgt_obj))):
            return False
        # string enum values
        if cond.equals_string and (str(tgt_obj) != str(cond.equals_string)):
            # print('Hier', cond.equals_string, tgt_obj)
            return False
        # bool conditions
        if cond.equals_expression and tgt_obj != eval(cond.equals_expression):
            return False
        return True

    def _getattr_dot_mapping(self, mapping, slot):
        '''Access a class attribute given in dot notation. Take care of references.
        '''
        slot_split = slot.split('.')
        # Try to get the target object from the mapping using possible key variants
        tgt_obj = mapping.get(slot_split[0])
        if tgt_obj is None:
            tgt_obj = mapping.get(f"{slot_split[0]}_id")
        if tgt_obj is None:
            raise Exception(f"The equation references an instance that is not found in the mapping. Slot '{slot_split[0]}' not in mapping {mapping}.")
        
        for s in slot_split[1:]:
            tgt_obj = getattr(tgt_obj, s)
            #print(type(tgt_obj), isinstance(tgt_obj, thm.extended_str))
            is_reference = (isinstance(tgt_obj, str) or isinstance(tgt_obj, thm.extended_str))
            if is_reference and (s != 'id') and (tgt_obj in self.known_instances):
                tgt_obj = self.known_instances[tgt_obj]

        #preprocess enums:
        if self.schemaview.get_slot(slot_split[-1]).range in self.schemaview.all_enums():
            tgt_obj = tgt_obj.text

        return tgt_obj

    def _getattr_dot(self, obj, slot):
        '''Access a class attribute given in dot notation. Take care of references.
        '''
        tgt_obj = obj
        for s in slot.split('.'):
            tgt_obj = getattr(tgt_obj, s)
            #print(type(tgt_obj), isinstance(tgt_obj, thm.extended_str))
            is_reference = (isinstance(tgt_obj, str) or isinstance(tgt_obj, thm.extended_str))
            if is_reference and (s != 'id') and (tgt_obj in self.known_instances):
                tgt_obj = self.known_instances[tgt_obj]
        return tgt_obj

    def _add_related_variables(self, eqn_object):
        '''Add all variables that are used in the equation to the related_variables slot of the equation.
        '''
        # self.known_instances('Variable')
        eqn_object.related_variables = []
        for var in self.instances('Variable'):
            # Match only if var.id is not part of a larger word (no letter, digit, or _ before/after)
            pattern = r'(?<![\w])' + re.escape(var.id) + r'(?![\w])'
            if re.search(pattern, eqn_object.as_text):
                eqn_object.related_variables.append(var.id)
        # print(eqn_object.as_text, eqn_object.related_variables)

class ConceptHandler(ProblemHandler):
    def __init__(self, ontology_filename, concept_dict, concept):
        '''Loads a concept from a dict and checks it agains an ontology. Similar to ProblemHandler.
        '''
        self.schemaview = SchemaView(ontology_filename)
        self.schemaview.imports_closure()

        #validate file
        report = validate(instance=concept_dict, schema=self.schemaview.materialize_derived_schema(), target_class=concept)
        
        if report.results:
            messages = [result.message for result in report.results]
            raise SyntaxError('The specified problem is invalid: \n    ' + "\n    ".join(messages))

        self.problem = yaml_loader.load(concept_dict, target_class=getattr(thm, concept))
        # print(self.problem)
        self.known_instances = {}
        self.instance_count = {}
        self.equation_view = None

        # hack
        self.problem['valid_problem'] = True
        self.problem['invalid_problem'] = False
        self.problem['additional_equations'] = []

        self._collect_instances()
        self._init_missing_items()
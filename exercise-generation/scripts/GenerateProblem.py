import sys
sys.path.insert(0, 'knowtd')
sys.path.insert(0, 'knowtd/scripts')

import random
import math
from linkml_runtime.utils.schemaview import SchemaView, SlotDefinition
from knowtd.scripts.ProblemHandler import ProblemHandler
from knowtd.scripts.ProblemSolver import ProblemSolver
import networkx as nx

ontology_filename = "knowtd/Ontology/thermodynamics_ontology.yaml"
schemaview = SchemaView(ontology_filename)
defaults = {'boolean': None, 'string': None, 'float': None , 'integer': None}

class ProblemGenerator:
    def __init__(self, problem_class:str, print_solution=False, 
                 attributes={}, values={}, only_template=False):

        # build full problem element
        self.index = {}
        self.all_variables = {}
        self.problem_element = self.generate_concept_element(problem_class, problem_class)
        self.problem_element['problem_class'] = problem_class
        fill_references(self.problem_element, problem_class)

        # assign values to calculate full kg with values
        self.given = {}
        self.attributes = attributes
        self.assign_attributes()
        self.values = values
        self.assign_values()
        self.required_elements_all()
        if only_template:
            return
        
        self.random_given_elements()

        # pprint(self.problem_element)

        self.handler = ProblemHandler(ontology_filename, self.problem_element)

        # compute knowledge graph with values
        self.solve(print_solution)

        # self.select_given_and_required_variables()
        self.select_given_and_required_variables()
        
    def generate_concept_element(self, class_name:str, parent_id:str):
        '''
        Given a class name initializes all attributes and variable slot according to its range. 
        '''
        class_element= {}
        # print('Generate', class_name, 'for', parent_id)
        # first generate id
        if 'id' in schemaview.class_slots(class_name):
            if class_name in schemaview.class_descendants('Variable'):
                class_element['id'] = f"{schemaview.get_class(class_name).annotations['schema:mathExpression']['value']}_{parent_id}"
                if class_name not in schemaview.class_descendants('UniversalQuantity'):
                    self.all_variables[class_element['id']] = schemaview.get_class(class_name).annotations['schema:Unit']['value'] if 'schema:Unit' in schemaview.get_class(class_name).annotations else ''
            
            else:
                if class_name in self.index:
                    self.index[class_name] += 1
                else:
                    self.index[class_name] = 1
                name = class_name
                class_element['id'] = f'{get_id(name, class_name, self.index[class_name])}'
        class_id = class_element['id'] if 'id' in class_element else None
        # then generate all other slots
        for slot_name in schemaview.class_slots(class_name):
            slot_definition = schemaview.induced_slot(slot_name, class_name)
            if slot_name == 'id':
                pass
            elif slot_definition.range in schemaview.class_descendants('Concept') + schemaview.class_descendants('Variable') + schemaview.class_descendants('Attribute') + list(defaults.keys()):
                class_element[slot_name] = self.generate_basic_element(slot_name, class_name, class_id)
            elif slot_definition.range in schemaview.all_enums():
                class_element[slot_name] = self.generate_slot_value(slot_definition, class_id)
        return class_element


    def generate_basic_element(self, slot_name:str, class_name:str, parent_id:str):
        '''
        Given a class name and a slot name, initializes the slot according to its range. 
        '''
        slot_definition = schemaview.induced_slot(slot_name, class_name)
        # print()
        # print(slot_name, slot_definition.range)
        # pprint(slot_definition)
        if slot_definition.inlined:
            if slot_definition.multivalued:
                num = slot_definition.exact_cardinality if slot_definition.exact_cardinality else slot_definition.minimum_cardinality
                for i in range(num):
                    return [self.generate_slot_value(slot_definition, parent_id) for i in range(num)]
            else:
                return self.generate_slot_value(slot_definition, parent_id)
        else:
            # do not create new element but refer to existing element
            # print(slot_name, class_name)
            return self.find_related_slot(slot_definition)
            #what is the matching id?
            # if slot_definition.multivalued:
        return

    def find_related_slot(self, slot_definition:SlotDefinition):
        if slot_definition.range in defaults:
            if slot_definition.ifabsent:
                if 'string' in slot_definition.ifabsent:
                    slot_definition.ifabsent = f"str('{slot_definition.ifabsent[7:-1]}')"
                return eval(slot_definition.ifabsent)
            else:
                # min value?
                return defaults[slot_definition.range]
        elif slot_definition.range in schemaview.all_enums():
            if slot_definition.ifabsent:
                if 'string' in slot_definition.ifabsent:
                    slot_definition.ifabsent = f"str('{slot_definition.ifabsent[7:-1]}')"
                return eval(slot_definition.ifabsent)
            else:
                return None
        else:
            # find matching id
            if slot_definition.multivalued:
                return f'TODO: [{slot_definition.range}]'
            else:
                return f'TODO: {slot_definition.range}'

    def generate_slot_value(self, slot_definition:SlotDefinition, parent_id:str):
        if slot_definition.range in defaults:
            if slot_definition.ifabsent:
                if 'string' in slot_definition.ifabsent:
                    slot_definition.ifabsent = f"str('{slot_definition.ifabsent[7:-1]}')"
                return eval(slot_definition.ifabsent)
            else:
                # min value?
                return defaults[slot_definition.range]
        elif slot_definition.range in schemaview.all_enums():
            if slot_definition.ifabsent:
                if 'string' in slot_definition.ifabsent:
                    slot_definition.ifabsent = f"str('{slot_definition.ifabsent[7:-1]}')"
                return eval(slot_definition.ifabsent)
            else:
                None
        elif slot_definition.range in schemaview.all_classes():
            return self.generate_concept_element(slot_definition.range, parent_id)
    
    def assign_attributes(self):
        for (id, attribute, value) in self.attributes:
            add_attribute_value_to_dict(id, attribute, value, self.problem_element)
            
    def assign_values(self):
        for (id, value) in self.values.items():
            add_value_to_dict(id, float(value), self.problem_element)

    # random given values for the problem
    def random_given_elements(self):
        if self.problem_element['problem_class'] == 'Equilibrium':
            self.random_given_elements_state(self.problem_element['state'])
            self.random_given_system(self.problem_element['state'])
            self.random_given_material(self.problem_element['state'])
        elif self.problem_element['problem_class'] == 'SingleStep':
            # 2+0+2 or 2+1+1 (information initial, transition, final) -> should be able to calculate the full KG
            # random initial state
            self.random_given_elements_state(self.problem_element['states'][0]) # set initial state
            
            # system and material are based on initial state
            self.random_given_material(self.problem_element['states'][0])
            self.random_given_system(self.problem_element['states'][0])
            
            # define transition or second state
            # check attributes to set values for final state
            if ('12', 'is_isothermal', True) in self.attributes:
                self.problem_element['change_of_state']['transition']['del_T']['value'] = 0
                self.problem_element['states'][1]['p']['value'] = random_pressure_isothermal(self.problem_element['pureMaterial']['R']['value'], self.problem_element['states'][0]['T']['value'])
            elif ('12', 'is_isobaric', True) in self.attributes:
                self.problem_element['change_of_state']['transition']['del_p']['value'] = 0
                self.problem_element['states'][1]['T']['value'] = random.randrange(270, 350)
            elif ('12', 'is_isochoric', True) in self.attributes:
                self.problem_element['change_of_state']['transition']['del_V']['value'] = 0
                self.problem_element['states'][1]['p']['value'] = random_pressure_isochor(self.problem_element['pureMaterial']['R']['value'], self.problem_element['states'][0]['rho']['value'])
            elif ('12', 'is_adiabatic', True) in self.attributes:
                self.problem_element['change_of_state']['transition']['Q']['value'] = 0
                self.problem_element['states'][1]['p']['value'] = random.randrange(1, 50) * 10000
            else:
                self.random_given_elements_state(self.problem_element['states'][1])
             

    def random_given_material(self, initial_state):
        if 'pureMaterial' in self.problem_element:
            self.problem_element['pureMaterial']['c_p']['value'] = random.randrange(1000, 2000)
            self.problem_element['pureMaterial']['R']['value'] = initial_state['p']['value'] / (initial_state['T']['value'] * initial_state['rho']['value'])

    def random_given_system(self, initial_state):
        if 'system' in self.problem_element:
            initial_state['rho']['value'] = random.randrange(1, 30) / 10
            self.problem_element['system']['m']['value'] = random.randrange(0, 50) + random.randrange(1, 99) /100
        elif 'systems' in self.problem_element:
            for system in self.problem_element['systems']:
                system['m']['value'] = random.randrange(0, 50) + random.randrange(1, 99) /100
        
    def random_given_elements_state(self, state):
        state['rho']['value'] = random.randrange(1, 30) / 10
        state['T']['value'] = random.randrange(270, 350)
        state['p']['value'] = random_pressure(state['rho']['value'], state['T']['value'])

    def required_elements_all(self):
        self.problem_element['required_variables'] = [item for item in self.all_variables]

    # Solver, calculate all other variables
    def solve(self, print_solution=False):
        self.solver = ProblemSolver(list(self.handler.instances('Variable')), 
                self.handler.create_equations(), 
                self.handler.problem.required_variables)

        solution = self.solver.solve()

        self.solution = {'required': {s: solution[s] for s in solution if s in self.handler.problem.required_variables},
                         'intermediate': {s: solution[s] for s in solution if s not in self.handler.problem.required_variables},
                         'not found': {v for v in self.handler.problem.required_variables if v not in solution}}
        # print solution
        if print_solution:
            print('Solution:')
            print(self.solution['required'])
            print('Intermediate Solutions:')
            print(self.solution['intermediate'])
            print('Could not find:')
            print(self.solution['not found'])

    def remove_value(self, var_id):
        # remove element from problem_element
        remove_elem_from_dict(var_id, self.problem_element)
        self.given.pop(var_id)

    def add_value(self, var_id, value):
        # add element to problem_element
        add_value_to_dict(var_id, value, self.problem_element)
        # add element to given
        self.given[var_id] = value
        
    def select_given_and_required_variables(self):
        '''1. Choose random required variable and use the bipartite graph to generate a solution path with length between 5 and 13 (as seen in the real exercises). 
        2. Select given variables from this path.
        3. Assign values to the given variables.
        4. validate/verify
        preprocessing: generate bipartite graph, select difficulty level.'''
        # create networkx bipartite graph from equations and variables
        B = nx.Graph()
        skip_variables = ('W_t_', 'w_t_', 'u_', 'h_', 's_', 'U_', 'H_', 'S_', 'ratio_')
        if not (12, 'is_polytropic', True) in self.attributes:
            skip_variables = skip_variables + ('n_poly',)
        B.add_nodes_from([v.id for v in self.handler.instances('Variable') if v.id in self.solution['required'] and not v.id.startswith(skip_variables)], bipartite=0)
            
        equations = self.handler.create_equations()
        # print(equations)
        B.add_nodes_from([eq.as_text for eq in equations], bipartite=1)
        for eq in equations:
            for var in eq.related_variables:
                if not var in B.nodes: # only consider equations, if related variables are in the graph (intensive/extensive)
                    B.remove_node(eq.as_text)
                    break
                else:
                    B.add_edge(var, eq.as_text)
                
        # select difficulty level
        difficulty_level = random.randint(5, 13) # test settings. sample problems have 5-13

        # step 1
        # plausbile required variables (Rebecca's list)
        possible_required = ['T_1', 'T_2', 'p_1', 'p_2', 'V_1', 'V_2', 'v_1', 'v_2', 
                             'm_1', 'm_2', 'n_1', 'n_2', 'rho_1', 'rho_2', 
                             'del_V_12', 'del_v_12', 'del_T_12', 'del_p_12', 
                             'Q_12', 'q_12', 'W_12', 'w_12', 
                             'R_gas', 'M_gas', 'c_v_gas', 'c_p_gas',
                             'del_S_12', 'del_U_12',
                             'del_s_12', 'del_u_12']
        intermediate = ['del_s_12', 'del_S_12', 'del_u_12', 'del_U_12', 'del_H_12', 'del_h_12'] 
        # Filter variables to only include those that are present in the current problem and where no direct assignment is given
        filtered_possible_required = [var for var in possible_required if var in B.nodes and var not in self.values and len(list(B.neighbors(var))) >= 1 and all(len(list(B.neighbors(eq))) > 1 for eq in list(B.neighbors(var)))]
        generate_attempts = 7
        
        while generate_attempts > 0:   
            random_required_var = random.choice(filtered_possible_required)
            self.problem_element['required_variables'] = [random_required_var]
                    
            # step 2
            # Select <difficulty_level many> equations that share at least one variable with each other
            try:
                solution_path = get_solution_path(B, random_required_var, difficulty_level, self.values, intermediate)
                # print(solution_path)
                break
            except:
                filtered_possible_required.remove(random_required_var)
                generate_attempts -= 1 
    
        # step 3
        # assign values
        for elem in self.given.copy():
            self.remove_value(elem)
        for var_id in [n for n,d in solution_path.in_degree() if d == 0 and nx.get_node_attributes(B, 'bipartite')[n] == 0]: # make sure it's a variable node
            if var_id.startswith("M_") or var_id.startswith("v_"):
                round_digits = 3
            else:
                round_digits = 2 
            self.add_value(var_id, round(float(self.solution['required'][var_id]), round_digits))
        self.problem_element['required_variables'] = [random_required_var]
        self.expected_solution = {random_required_var: f"{float(self.solution['required'][random_required_var]):.2f} {self.all_variables[random_required_var]}"}
        
        # step 4
        # validate/verify
        valid_exercise = True
        handler = ProblemHandler(ontology_filename, self.problem_element)
        solver = ProblemSolver(list(handler.instances('Variable')), 
                        handler.create_equations(), 
                        handler.problem.required_variables)
        try:
            solution = solver.solve()  
            if random_required_var not in solution:
                valid_exercise = False
                print('Could not solve the generated problem for required variable:', random_required_var)
                # raise ValueError('Could not solve the generated problem!')
            elif self.values and all(var not in solution or f"{solution[var]:.2f}" != f"{self.values[var]:.2f}" for var in self.values):
                valid_exercise = False
                for var in self.values:
                    if var not in solution:
                        print('Expected given variable:', var, ' but it is not in the solution.')
                    elif f"{solution[var]:.2f}" != f"{self.values[var]:.2f}":
                        print('Expected given variable:', var, ' with value:', self.values[var], ' but got:', solution[var])
                # raise ValueError('Generated problem given values do not match expected values!')
            elif f"{solution[random_required_var]:.2f}" != f"{self.solution['required'][random_required_var]:.2f}":
                print('Expected solution:', self.solution['required'][random_required_var], ' but got:', solution[random_required_var], ' possible due to rounding.')
                self.expected_solution = {random_required_var: f"{float(solution[random_required_var]):.2f} {self.all_variables[random_required_var]}"}

        except:
            valid_exercise = False
            print('Could not solve the generated problem!')
            
        if not valid_exercise:
            print('REPEAT GENERATION')
            self.select_given_and_required_variables()
        else:
            # print(solution)
            
            # write solution value with unit (if there is a unit in self.all_variables)
            var_temp = {n: f"{float(solution[n]):.2f}" for n in solution}
            
            for n in var_temp:
                if n in self.all_variables:
                    var_temp[n] += f" {self.all_variables[n]}"
                    
            # solution path can contain more variables than knowTD solution. remove them from yaml.
            for elem in self.given.copy():
                if elem not in var_temp:
                    self.remove_value(elem)
            # remove constant variables
            for elem in ['Rbar_gas1', 'T0_1', 'T0_2']:
                remove_elem_from_dict(elem, self.problem_element)
            
            self.solution_path = {'variables': var_temp,
                                    'equations': {n: {'name': n[:-1], 'expression': str(d['expression'])} for n,d in solver.G_optimized.nodes(data=True) if d['type'] == 'equation'}}
        
# helper functions:
def get_solution_path(G:nx.Graph, start_node:str, length:int, priority_vars={}, intermediate=None):
    '''Given a graph, a start variable node and a equation length, return a solution path including <length> equation nodes.
    nx.Graph: The constructed tree.
    '''
    if start_node not in G.nodes:
        raise ValueError("The start_node must be in the graph G.")
    print('Generating solution path starting at', start_node, 'with length', length)
    # Initialize the tree and add the start node
    tree = nx.DiGraph()
    tree.add_node(start_node)
    
    # Track the number of Eq nodes added
    var_nodes = {start_node}
    eq_nodes = set()

    def add_equation(eq_node, tree, G):
        eq_nodes.add(eq_node)
        tree.add_node(eq_node)
        # add all connected variables
        keep_going = False
        for neighbor in G.neighbors(eq_node):
            if neighbor in var_nodes:
                if not tree.has_edge(neighbor, eq_node) and neighbor != start_node:
                    tree.add_edge(neighbor, eq_node)
                continue  # Skip already added nodes
            tree.add_node(neighbor)
            var_nodes.add(neighbor)
            tree.add_edge(neighbor, eq_node)
            keep_going = True
            
            # if the variable is already given in problem, add assignment equation
            if any(len(list(G.neighbors(eq))) == 1 for eq in list(G.neighbors(neighbor)) if eq not in eq_nodes):
                for assignment_eq in [eq for eq in G.neighbors(neighbor) if len(list(G.neighbors(eq))) == 1 and eq not in eq_nodes]:
                    tree.add_node(assignment_eq)
                    tree.add_edge(assignment_eq, neighbor)
                    eq_nodes.add(assignment_eq)
        return keep_going
            
    something_changed = True
    intermediate_as_given = False
    while something_changed and (len([e for e in eq_nodes if not 'Assignment_' in e]) < length or intermediate_as_given):
        # check of there are more equations to add. Random select one variable (root) node to which an equation can be added
        something_changed = False
        # print('Is the path a tree?', nx.is_tree(tree))
        candidate_variables = [n for n, d in tree.in_degree() if d == 0]  # variable nodes with degree 0 in the tree
        intermediate_as_given = any(var in intermediate for var in candidate_variables)
        if intermediate_as_given:
            candidate_variables = [var for var in candidate_variables if var in intermediate]
        while not something_changed and candidate_variables:
            selected_var = random.choice(candidate_variables)
            candidate_equations = [n for n in G.neighbors(selected_var) if n not in eq_nodes]
            if selected_var != start_node:
                candidate_equations = [eq for eq in candidate_equations if start_node not in G.neighbors(eq)]
            while not something_changed and candidate_equations:
                # prioritize equations that are connected to a given variable
                candidate_equations_priority = [eq for eq in candidate_equations if any(var in G.neighbors(eq) for var in priority_vars)]
                # print('Priority Equations:', candidate_equations_priority)
                if candidate_equations_priority:
                    selected_equation = random.choice(candidate_equations_priority)
                else:
                    selected_equation = random.choice(candidate_equations)
                # print('Trying to add equation:', selected_equation)
                something_changed = something_changed or add_equation(selected_equation, tree, G)
                if not something_changed:
                    candidate_equations.remove(selected_equation)
                else:
                    if tree.has_edge(selected_var, selected_equation):
                        tree.remove_edge(selected_var, selected_equation)
                    tree.add_edge(selected_equation, selected_var)
            # check if equation could be added for selected variable
            if not something_changed:
                candidate_variables.remove(selected_var)
        if not something_changed:
            raise ValueError(f"No more equations can be added to the tree. Desired length {length} could not be reached. Current length: {len(eq_nodes)}")
            break
    return tree

def get_attributes_and_range(concept_name:str):
    '''Given a concept, return attributes and their possible values.'''
    # get all combinations
    attributes = [a for a in schemaview.class_induced_slots(concept_name) if a.in_subset and 'attributes' in a.in_subset]
    possible_values = {a.name: [] for a in attributes}
    for a in attributes:
        possible_values[a.name] = [True, False] if 'boolean' in a.range else list(schemaview.get_enum(a.range).permissible_values)
        if not (a.required or a.ifabsent):
            possible_values[a.name].append(None)
    return possible_values

def fill_references(problem_element, parent_name, parent_element=None):
    parent_element = problem_element if parent_element == None else parent_element
    distinct_objects = {}
    for elem in problem_element:
        if isinstance(problem_element[elem], str) and problem_element[elem].startswith('TODO: '):
            #replace todo with reference
            is_multivalued = '[' in problem_element[elem] and ']' in problem_element[elem]
            problem_element[elem] = problem_element[elem].replace('TODO: ', '').replace('[', '').replace(']', '')

            found_replacement = False
            if is_multivalued:
                for slot_definition in schemaview.class_induced_slots(parent_name):
                    if slot_definition.range == problem_element[elem] and slot_definition.inlined:
                        found_replacement = True
                        if slot_definition.multivalued:
                            problem_element[elem] = [child['id'] for child in parent_element[slot_definition.name]]
                        else:
                            problem_element[elem] = [parent_element[slot_definition.name]['id']]
            else:
                for slot_definition in schemaview.class_induced_slots(parent_name):
                    if slot_definition.range == problem_element[elem] and slot_definition.inlined:
                        if not slot_definition.multivalued:
                            problem_element[elem] = parent_element[slot_definition.name]['id']
                            found_replacement = True
                        else:
                            if not problem_element[elem] in distinct_objects:
                                distinct_objects[problem_element[elem]] = []
                            for i in parent_element[slot_definition.name]:
                                if i['id'] not in distinct_objects[problem_element[elem]]:
                                    distinct_objects[problem_element[elem]].append(i['id'])
                                    problem_element[elem] = i['id']
                                    found_replacement = True
                                    break
            if not found_replacement:
                problem_element[elem] = None
            
        elif isinstance(problem_element[elem], dict):
            fill_references(problem_element[elem], parent_name, parent_element)
        elif isinstance(problem_element[elem], list):
            for list_elem in problem_element[elem]:
                fill_references(list_elem, parent_name, parent_element)

    for elem in problem_element:
        if 'system' in elem:
            if isinstance(problem_element[elem], dict):
                states = problem_element[elem]['related_states'] if problem_element[elem]['related_states'] else []
                changes = problem_element[elem]['related_changes'] if problem_element[elem]['related_changes'] else []
                problem_element[elem]['related_changes_and_states'] = changes + states
            elif isinstance(problem_element[elem], list):
                for sys in problem_element[elem]:
                    states = sys['related_states'] if sys['related_states'] else []
                    changes = sys['related_changes'] if sys['related_changes'] else []
                    sys['related_changes_and_states'] = changes + states
    
def remove_elem_from_dict(elem, container):
    if isinstance(container, dict):
        if 'id' in container and container['id'] == elem and 'value' in container:
                container['value'] = None
        else:
            for c_elem in container:
                remove_elem_from_dict(elem, container[c_elem])
    elif isinstance(container, list):
        for list_elem in container:
            remove_elem_from_dict(elem, list_elem)

def add_value_to_dict(elem, value, container):
    if isinstance(container, dict):
        if 'id' in container and container['id'] == elem:
            container['value'] = value
        else:
            for c_elem in container:
                add_value_to_dict(elem, value, container[c_elem])
    elif isinstance(container, list):
        for list_elem in container:
            add_value_to_dict(elem, value, list_elem)

def add_attribute_value_to_dict(concept_id, attribute, value, container):
    """Given a concept id, attribute name and value, adds the value to the attribute."""
    if isinstance(container, dict):
        if 'id' in container and container['id'] == concept_id and attribute in container:
            container[attribute] = value
        else:
            for c_elem in container:
                add_attribute_value_to_dict(concept_id, attribute, value, container[c_elem])
    elif isinstance(container, list):
        for list_elem in container:
            add_attribute_value_to_dict(concept_id, attribute, value, list_elem)

def get_id(name, class_name, index):
    if class_name == 'System':
        return _int_to_roman(index)
    elif class_name == 'Transition':
        return int(str(index) + str(index+1)) #?
    elif class_name == 'ChangeOfState':
        return chr(64+index)
    elif class_name in schemaview.class_descendants('Material'):
        return f'gas{index}'
    elif class_name in schemaview.class_descendants('State'):
        return index
    else:
        return f'{name}{index}'

def _int_to_roman(num):
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

def get_problemclasses():
    for class_name in schemaview.class_descendants('Problem', reflexive=False):
        class_def = schemaview.get_class(class_name)
        if not class_def.abstract and not 'Contact' in class_name and not 'SystemSpecification' in class_name:
            yield class_name
            
def get_intesive_variables():
    for class_name in schemaview.class_descendants('IntensiveStateVariable', reflexive=False):
        class_def = schemaview.get_class(class_name)
        if not class_def.abstract:
            yield class_name

def get_extensive_variables():
    for class_name in schemaview.class_descendants('ExtensiveStateVariable', reflexive=False):
        class_def = schemaview.get_class(class_name)
        if not class_def.abstract:
            yield class_name

def random_pressure(rho, T):
    """Given a density and a temperature, calculate pressure p such that:
    0.1 bar < p < 5 bar
    and
    0.004 < molar Mass < 0.3 
        this is equivalent to
        0.004 < Rbar * T * rho / p < 0.3
    This is based on the equations M=Rbar / R and R= p / (T*rho) [ideal gas law]"""
    Rbar = 8.31446261815324
    maximal_molar_Mass = 0.3
    minimal_molar_Mass = 0.004
    
    lower = max(10000, Rbar * T * rho / maximal_molar_Mass)
    upper = min(500000, Rbar * T * rho / minimal_molar_Mass)
    
    # Convert bounds to multiples of 1000
    p_min = math.floor(lower / 1000) * 1000
    p_max = math.ceil(upper / 1000) * 1000

    if p_min > p_max:
        if lower < upper:
            p_min = math.floor(lower)
            p_max = math.ceil(upper)
            p = random.randrange(p_min, p_max + 1, 1000)
        else:
            raise ValueError("No valid p multiple of 1000 exists")
    else:
        p = random.randrange(p_min, p_max + 1, 1000) #1000 steps to make the presure easy to read.

    return p

def random_pressure_isothermal(R, T):
    """Given a gas constant R and a temperature, calculate pressure p such that:
    0.1 bar < p < 5 bar
    and
    0.1 < density < 3 
        this is equivalent to
        0.1 * T * R < p < 3 * T * R
    This is based on the equation R= p / (T*rho) [ideal gas law]"""
    maximal_density = 3
    minimal_density = 0.1
    
    lower = max(10000, minimal_density * T * R)
    upper = min(500000, maximal_density * T * R)
    
    # Convert bounds to multiples of 1000
    p_min = math.floor(lower / 1000) * 1000
    p_max = math.ceil(upper / 1000) * 1000

    if p_min > p_max:
        if lower < upper:
            p_min = math.floor(lower)
            p_max = math.ceil(upper)
            p = random.randrange(p_min, p_max + 1, 1000)
        else:
            raise ValueError("No valid p multiple of 1000 exists")
    else:
        p = random.randrange(p_min, p_max + 1, 1000) #1000 steps to make the presure easy to read.

    return p

def random_pressure_isochor(R, rho):
    lower = max(10000,  270 * R / rho)
    upper = min(500000, 350 * R / rho)
    
    # Convert bounds to multiples of 1000
    p_min = math.floor(lower / 1000) * 1000
    p_max = math.ceil(upper / 1000) * 1000

    if p_min > p_max:
        if math.floor(lower) < math.ceil(upper):
            p_min = math.floor(lower)
            p_max = math.ceil(upper)
            p = random.randrange(p_min, p_max + 1, 1000)
        else:
            raise ValueError(f"No valid p multiple of 1000 exists. R={R}, rho={rho}")
    else:
        p = random.randrange(p_min, p_max + 1, 1000) #1000 steps to make the presure easy to read.

    return p
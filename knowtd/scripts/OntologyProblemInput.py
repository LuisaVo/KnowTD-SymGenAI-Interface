from linkml_runtime.utils.schemaview import SchemaView
import re


schema = SchemaView("knowtd/Ontology/thermodynamics_ontology.yaml")

id_count = {}
def get_concept_dict(conceptName):
    '''Given a concept name returns dictionary with variables and attributes and their values.'''
    return {'id': get_id(conceptName)} | get_variables(conceptName) | get_attributes(conceptName) | get_related_concepts(conceptName) if conceptName in schema.class_descendants('Concept') else {}

def get_variables(conceptName):
    '''Given a concept name returns a dictionary with its variables and optional default value.'''
    if not conceptName in schema.class_descendants('Concept'):
        return {}
    variables = {}
    for slot in schema.class_induced_slots(conceptName):
        if slot.range in schema.class_descendants('Variable'):
            range_class = schema.get_class(slot.range)
            value = None
            if 'value' in range_class.slot_usage:
                value = range_class.slot_usage['value'].ifabsent
            if value is not None and isinstance(value, str):
                m = re.search(r"(float|integer|string)\(([^)]*)\)", value)
                if m:
                    cast_type, raw_value = m.group(1), m.group(2)
                    if cast_type == 'float':
                        value = float(raw_value)
                    elif cast_type == 'integer':
                        value = int(raw_value)
                    else:
                        value = raw_value
            variables[slot.name] = {'value': value}
    return variables

def get_attributes(conceptName):
    '''Given a concept name returns a dictionary with its attributes and optional default value.'''
    # bool and enum
    if not conceptName in schema.class_descendants('Concept'):
        return {}
    attributes = {}
    for slot in schema.class_induced_slots(conceptName):
        if slot.range in schema.all_enums():
            attributes[slot.name] = re.search(r"(float|integer|string)\(([A-Za-z0-9. ]+)\)", slot.ifabsent).group(2) if slot.ifabsent else None
        elif slot.range == 'boolean':
            attributes[slot.name] = slot.ifabsent =='True' if slot.ifabsent else None
    return attributes

def get_related_concepts(conceptName):
    '''Given a concept name returns a dictionary with its related concepts (has_a relation). If the related concept is inlined it returns the dict of the related concept, else None/id'''
    if not conceptName in schema.class_descendants('Concept'):
        return {}
    # fill with id if not inlined, else fill with concept dict
    concepts = {}
    for slot in schema.class_induced_slots(conceptName):
        if slot.range in schema.class_descendants('Concept'):
            if schema.is_inlined(slot):
                concepts[slot.name] = get_concept_dict(slot.range)
            else:
                concepts[slot.name] = None 
            if schema.is_multivalued(slot.name):
                concepts[slot.name] = [concepts[slot.name]] if concepts[slot.name] != None else []
    return concepts

def get_problem_concepts(problemClass):
    '''Given a problem class, generates a dictionary with all concepts (dict). 
    If the slot is a list of concepts, it generates the minimum amount of elements.'''
    reset_id_count()
    if not problemClass in schema.class_descendants('Problem'):
        return {}

    concepts = {}
    for slot in schema.class_induced_slots(problemClass):
        if slot.range in schema.class_descendants('Concept'):
            if schema.is_multivalued(slot.name):
                num = slot.exact_cardinality if slot.exact_cardinality else 1
                num = slot.minimum_cardinality if slot.minimum_cardinality else num
                concepts[slot.name] = [get_concept_dict(slot.range) for i in range(1,num+1)]
            else:
                concepts[slot.name] = get_concept_dict(slot.range)
    if 'state' in concepts:
        concepts['system']['related_changes_and_states'] = [concepts['state']['id']]
    elif 'change_of_state' in concepts:
        concepts['system']['related_changes_and_states'] = list(concepts['change_of_state']['id'])
    elif 'change_of_states' in concepts:
        concepts['system']['related_changes_and_states'] = [elem['id'] for elem in concepts['change_of_states']]
    if 'system' in concepts and 'pureMaterial' in concepts:
        concepts['system']['material'] = concepts['pureMaterial']['id']
    reset_id_count()
    return concepts

def get_id(concept_class):
    '''Given a concept class, returns the next id for this class.'''
    if concept_class not in schema.all_classes():
        return None
    
    global id_count
    if concept_class not in id_count:
        id_count[concept_class] = 1
    else:
        id_count[concept_class] += 1

    if 'System' in schema.class_ancestors(concept_class):
        return _int_to_roman(id_count[concept_class])
    elif 'Material' in schema.class_ancestors(concept_class):
        return f'Gas{id_count[concept_class]}' if id_count[concept_class] > 1 else 'Gas'
    elif concept_class == 'EquationOfState':
        return f'EOS{id_count[concept_class]}'
    elif concept_class == 'ChangeOfState':
        return chr(64+id_count[concept_class])
    elif concept_class == 'State':
        return id_count[concept_class]
    elif concept_class == 'Transition':
        return f'{id_count[concept_class]}{id_count[concept_class]+1}'

    return f'{concept_class}{id_count[concept_class]}'

def reset_id_count():
    global id_count
    id_count = {}

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
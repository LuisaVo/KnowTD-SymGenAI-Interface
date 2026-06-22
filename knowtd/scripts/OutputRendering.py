from linkml_runtime.utils.schemaview import SchemaView
import sympy

ontology_filename = "knowtd/Ontology/thermodynamics_ontology.yaml"

unit_mapping = {}
schema = SchemaView(ontology_filename)
for variable in schema.class_descendants("Variable", reflexive=False):
    unit_mapping[schema.get_class(variable).annotations['schema:mathExpression'].value] = schema.get_class(variable).annotations['schema:Unit'].value

def math_typsetting(formula):
    if formula == 0:
        return '0'
    formula = formula.replace('del_','Delta ')
    # formula = formula.replace('polytropic','polytrop\ic')
    formula = formula.replace('_exponent',' exponent')
    # formula = formula.replace('index','i\\ndex')
    # formula = formula.replace('pot', '{pot}')
    # formula = formula.replace('kin','{ki\\n}')
    formula = formula.replace('_Gas','')
    # formula = formula.replace('Rbar', 'barR')
    formula = formula.replace('Delta e_kin_12 + Delta e_pot_12 + ', '')
    formula = formula.replace('Delta E_kin_12 + Delta E_pot_12 + ', '')
    return(formula)

def variable_typsetting_brackets(variable):
    formula = variable.replace('del_', '\\Delta ').replace('_exponent',' exponent')
    if '_' in formula:
        [formula_body, formula_index] = formula.split('_', 1)
        formula = formula_body + '_{' + variable_typsetting_brackets(formula_index) + '}'
    return formula

def latex_typsetting(formula):
    if '/' in formula:
        split_list = formula.split('/')
        if ' ' in split_list[0]:
            left = split_list[0].rsplit(' ', 1)
        else:
            left = ('', split_list[0])
        if split_list[1].startswith('(') and split_list[1].endswith(')'):
            split_list[1] = split_list[1][1:-1]
        formula = left[0] + ' \\frac{' + left[1] + '}{' + split_list[1] + '}'
    return formula

def get_variable_label(variable, value=''):
    var = variable.rsplit("_", 1)[0]
    if var in unit_mapping:
        unit = unit_mapping[var]
    if var not in unit_mapping or unit == 'none' or unit == None:
        unit = ''
    # label
    label = f'{value:.2f} {unit}' if value != '' else ''
    label = label.replace('.00','')
    return(label)

def return_cyto_graph_elements(G, assignments={}, find=[]):
    """Input a G_optimized and a solution dict.
    Returns the cyto elements representation of the solution path."""
    # example:
    # elements=[
    #             # The nodes elements
    #             {'data': {'id': 'one', 'label': 'Node 1'},
    #              'position': {'x': 50, 'y': 50}},
    #             {'data': {'id': 'two', 'label': 'Node 2'},
    #              'position': {'x': 200, 'y': 200}},

    #             # The edge elements
    #             {'data': {'source': 'one', 'target': 'two', 'label': 'Node 1 to 2'}}

    rule_edges = []

    node_label = {}

    for n in G.nodes():
        # handle properties
        # collect all nodes and their label
        if 'Assignment' in n or 'AdditionalEquation' in n:
            # Handle assignments
            pass
            # eqn_formula = G.nodes(data=True)[n]['expression']
            # node_label[n] = (eqn_formula, 'assignment')
        elif '_' in n:
            # Handle variable nodes
            name = math_typsetting(n)
            # unit
            if n in assignments:
                label = get_variable_label(n, assignments[n])
            else: 
                label = ''
            if n in find:
                type = 'required'
            elif f'Assignment{n}' in G.nodes():
                type = 'assignment'
            else:
                type = 'variable'
            node_label[n] = (name, label, type)
        else:
            # Handle remaining (equation nodes)
            eqn_name = ''.join([i for i in n if not i.isdigit()])
            if not 'NotInMotion' in eqn_name and eqn_name in schema.all_classes():
                eqn_formula = G.nodes[n]['expression']
                if isinstance(eqn_formula, sympy.core.symbol.Symbol):
                    eqn_formula = f'{eqn_formula} = 0'
                elif isinstance(eqn_formula, sympy.core.add.Add):
                    eqn_formula = eqn_formula.as_two_terms()
                    eqn_formula = f'{eqn_formula[0]} = {eqn_formula[1] * -1}'
                eqn_formula = math_typsetting(eqn_formula)
                node_label[n] = (eqn_name, eqn_formula, 'equation')
                # check if rule should be added
                if 'Rule' in schema.class_ancestors(eqn_name):
                    for a in schema.class_ancestors(eqn_name):
                        if schema.get_class(a).rules:                       
                            for (item_name, item_label) in [(cond.name, write_rules(cond)) for r in schema.get_class(a).rules for cond in r.preconditions.slot_conditions.values()]:
                                # connect rule(item) to equation(n)
                                if not ('transition.motion' in item_name or 'system.closed' in item_name or 'system.equilibrium' in item_name or 'system.homogeneous' in item_name):
                                    node_label[item_name] = (item_name, item_label, 'rule')
                                    rule_edges.append((item_name, n, 'rule applies'))
    node_elements = [
        {'data': {'id': node, 
                  'label': node_label[node][0] + '\n' + str(node_label[node][1]),
                  'type': node_label[node][2], 
                  'value': str(node_label[node][1])},
         'classes': node_label[node][2]}
        for node in node_label
    ]

    edge_elements = [
        {'data': {
                'source': s, 
                'target': t, 
                'label': ''
                }}
        for s,t in G.edges() if s in node_label and t in node_label
    ] + [
        {'data': {
                'source': s, 
                'target': t, 
                'label': l
                },
         'classes': 'edge'}
        for s,t,l in rule_edges if s in node_label and t in node_label
    ]
    return node_elements + edge_elements


def write_rules(cond):
    rules = ''
    sep = ''
    andString = 'and \n'
    if cond.range:
        rules += f'has range {cond.range}'
        sep = andString
    if cond.equals_string:
        rules += f'{sep} equals {cond.equals_string}'
        sep = andString
    if cond.equals_expression:
        rules += f'{sep} equals {cond.equals_expression}'
        sep = andString
    if cond.any_of:
        rules += f'{sep} Any of:\n'
        for list_cond in cond.any_of:
            rules += f"{write_rules(list_cond)}\n"
        sep = andString
    if cond.all_of:
        rules += f'{sep} All of:\n'
        for list_cond in cond.all_of:
            rules += f"{write_rules(list_cond)}\n"
        sep = andString
    if cond.none_of:
        rules += f'{sep} None of:\n'
        for list_cond in cond.none_of:
            rules += f"{write_rules(list_cond)}\n"
        sep = andString
    if cond.exactly_one_of:
        rules += f'{sep} Exactly one of:\n'
        for list_cond in cond.exactly_one_of:
            rules += f"{write_rules(list_cond)}\n"
    return f'{rules}'

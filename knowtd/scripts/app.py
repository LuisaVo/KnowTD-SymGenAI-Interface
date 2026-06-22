import pprint
from dash import Dash, html, dcc, callback, Output, Input, State, ctx
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
import ProblemInput
import yaml


cyto.load_extra_layouts()

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# default values
problemInput = ProblemInput.Equilibrium()

# html elements
# navigation
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "ML in ChemEng",
                href="https://chemengml.org/",
            )
        ),
    ],
    brand="KnowTD user Inferface",
    brand_href="#",
    color="dark",
    dark=True,
)

example_layout = html.Div([
    html.H2('Load an Example?'),
    html.P('You can manually insert an input or select an example. The examples load a predefined input that can be adjusted. Hit submit (end of page) to send the input to KnowTD.'),
    dbc.Stack([dbc.Select(options=['Custom Input', 'Single Step 1', 'Single Step 2', 'Single Step 3', 'Single Step 4', 'Single Step 5', 'Single Step 6',
                                         'Single Step 7', 'Single Step 8', 'Single Step 9', 'Single Step 10', 'Single Step 11', 'Single Step 12', 'Single Step 13', 
                                         'Cyclic Process 1', 'Cyclic Process 2'], value='Custom Input', id='radio-select-example'),
        
        dcc.Markdown(children='', mathjax=False, id='P-selected-example')
        ], gap=3)
    ], 
    id='examples')

input_layout = html.Div([
        html.Div([
            html.H2('1. Select a Problem Class'),
            html.P('Please select the problem class'),
            dbc.RadioItems(options=['State in Equilibrium', 'Single Step', 'Sequential Steps', 'Cyclic Process'], id='radio-select-problem-class'),
            dbc.Input(id='input-number-states', type='number', min=3, max=99, step=1, placeholder='How many states do you want to generate? (>= 3)', className='invisible'),
            html.P(children='', id='P-selected-Problem-Class')
        ], id='div-problem'),
        html.Hr(),
        html.Div([
            html.H2('2. Enter values for attributes'),
            dbc.Row(children=[], id='div-attribute-input-elements'),
            dbc.Button('Submit attributes', id='button-submit-attribute-input', color='primary', className='invisible'),
            html.P(children='', id='P-submit-attributes', className='invisible')
        ], id= 'div-attribute-input'),
        html.Hr(),
        html.Div([
            html.H2('3. Enter values for the variables'),
            dbc.Row(children=[], id='div-variable-value-input-elements'),
        ], id='div-variable-value-input'),
        dbc.Button('Submit', id='button-submit-input', color='primary', className='invisible'),
        html.P(children='', id='P-submit-input'), 
        
    ], id='div-input')

def get_node_layout(layout):
    if layout == 'tree':
        return {'name': 'dagre',
                'roots': '.rule',
                'directed': 'true'}
    else:
        return {'name': 'cose'}

def get_cyto_layout(id, layout):
    return cyto.Cytoscape(
                            id=id,
                            style={'width': '100%', 'height': '1000px'},
                            layout=get_node_layout(layout),
                            minZoom = 0.5,
                            maxZoom = 2,
                            pan={'x':0, 'y':0},
                            userZoomingEnabled = False,
                            elements={},
                            stylesheet=[
                                # Group selectors
                                {
                                    'selector': 'node',
                                    'style': {
                                        'label': 'data(label)',
                                        'text-halign': 'center',
                                        'text-valign': 'center',
                                        'background-opacity': 0.2,
                                        'min-width': 100,
                                        'width': 'label',
                                        'height': 'label',
                                        'min-height': 100,
                                        'text-wrap': 'wrap'
                                    }
                                },
                                {
                                    'selector': 'edge',
                                    'style': {
                                        'target-arrow-shape': 'triangle',
                                        'arrow-scale': 2,
                                        'curve-style': 'straight'
                                    }
                                },
                                # Class selectors
                                {
                                    'selector': '.variable',
                                    'style': {
                                        'background-color': 'gray',
                                        'line-color': 'black',
                                        'shape': 'ellipse'
                                    }
                                },
                                {
                                    'selector': '.required',
                                    'style': {
                                        'background-color': 'red',
                                        'line-color': 'red',
                                        'shape': 'ellipse'
                                    }
                                },
                                {
                                    'selector': '.assignment',
                                    'style': {
                                        'background-color': 'green',
                                        'line-color': 'green',
                                        'shape': 'ellipse'
                                    }
                                },
                                {
                                    'selector': '.rule',
                                    'style': {
                                        'background-color': 'green',
                                        'line-color': 'green',
                                        'shape': 'round-rectangle'
                                    }
                                },
                                {
                                    'selector': '.equation',
                                    'style': {
                                        'background-color': 'gray',
                                        'line-color': 'black',
                                        'shape': 'rectangle'
                                    }
                                }
                            ]
                        )

output_layout = html.Div([
        html.H2('4. Solution'),
        dbc.Collapse(
            html.Div(children=[
                dbc.Alert("Please note that the server might take up to 60 seconds to compute the solution.", color="primary", id='alert-runtime'),
                dcc.Loading( 
                    children=[
                        html.Div(children=[], id='div-solution-values-elements'),
                        dbc.Row([      
                        dbc.Col(html.A(html.Button('Reset', className='btn btn-primary'), href='/')),
                        dbc.Col(
                            dbc.Row([
                                dbc.Col([html.H4('Zoom'),dcc.Slider(id='slider-solution-graph-zoom', min=0.5, max=2, step=0.1, value=1)]),
                                dbc.Col(dbc.Button('Reset zoom', id='button-reset-solution-graph', color='primary'), width="auto"),
                            ],justify="end"), width=7
                                ),
                        ], justify="end"),
                        # dbc.Alert('', color="primary", id='cytoscape-solution-path-output'),
                        dbc.Tabs([
                            dbc.Tab(get_cyto_layout('cytoscape-solution-path', 'tree'), label="Solution Path"),
                            dbc.Tab(get_cyto_layout('cytoscape-reasoning-graph', 'force'), label="Reasoning Graph")
                            ]),
                        ], id="loading-solution", type="graph")
            ], id='div-utils-solution-graph'),
            id='collapse-solution', is_open=False)
    ], id='div-solution-output')

# body layout
body_layout = dbc.Container([
    html.H1('KnowTD User Inferface'),
    html.Div([
        html.P('This interface can be used to interactively translate a given thermodyanmic problem to KnowTD. The problem then can be submitted to KnowTD and a solution is presented.'),
    ]),
    html.Hr(),
    example_layout,
    html.Hr(),
    input_layout,
    html.Hr(),
    output_layout,
    html.Hr()
],
style={"marginTop": 20})

# App layout
app.layout = html.Div([navbar, body_layout])

# Add controls to build the interaction
# ProblemClass Feedback
@callback(
    Output('P-selected-Problem-Class', 'children'),
    Output('button-submit-attribute-input','className'),
    Input('radio-select-problem-class', 'value'),
)
def update_problemClass(type_chosen):
    if type_chosen:
        return f'You selected the problem class {type_chosen}', 'visible'
    else:
        return '', 'invisible'
    
@callback(
    Output('button-submit-input','className'),
    Input('radio-select-problem-class', 'value'),
    Input('button-submit-attribute-input', 'n_clicks'),
    Input('radio-select-example', 'value')
)
def toggle_button_submit_input_visibility(type_chosen, attribute_button, example_value):
    triggered_id = ctx.triggered_id
    if triggered_id == 'radio-select-problem-class':
        return 'invisible'
    elif triggered_id == 'button-submit-attribute-input' or triggered_id == 'radio-select-example':
        return 'visible'
    else:
        return 'invisible'

@callback(
    Output('input-number-states', 'className'),
    Input('radio-select-problem-class', 'value'),
    Input('radio-select-example', 'value')
)
def toggle_numberOfStepsInput(selected_class, example_selected):
    if selected_class in ['Sequential Steps', 'Cyclic Process'] and example_selected == 'Custom Input':
        return 'visible'
    return 'invisible'


# Boolean Value Input
@callback(
    Output('div-attribute-input-elements', 'children'),
    Input('radio-select-problem-class', 'value'),
    Input('input-number-states', 'value'),
    State('radio-select-example', 'value')
)
def update_attribute_input(type_chosen, numStates, example_selected):
    elements = []
    global problemInput

    if ctx.triggered_id == 'radio-select-problem-class' and type_chosen in ['Sequential Steps', 'Cyclic Process']:
        return dbc.Row(elements)
        # wait for the number of states input

    if example_selected != 'Custom Input':
        pass
    elif type_chosen == 'State in Equilibrium':
        problemInput = ProblemInput.Equilibrium()
    elif type_chosen == 'Single Step':
        problemInput = ProblemInput.SingleStep()
    elif ctx.triggered_id == 'input-number-states' and numStates and numStates >= 3:
        if type_chosen == 'Sequential Steps':
            problemInput = ProblemInput.SequentialSteps(numStates)
        elif type_chosen == 'Cyclic Process':
            problemInput = ProblemInput.CyclicProcess(numStates)
    else: 
        return dbc.Row(elements)
    
    disabled_attr = ['closed', 'equilibrium', 'motion', 'homogeneous']
    for concept in problemInput.get_concepts():
        if list(problemInput.get_attributes(concept)):
            col_elements = []
            col_elements.append(html.H3(f'{concept}:', id=f'{concept}-Attribute-Heading'))
            for variable in problemInput.get_attributes(concept):
                col_elements.append(dbc.Row([
                    dbc.Col(html.P(f'{variable}:', id=f'{concept}-{variable}-Attribute-P'), class_name='col-4'),
                    dbc.Col(dbc.Input(
                                    type='text',
                                    disabled = variable in disabled_attr,
                                    value=problemInput.get_value(concept, variable),
                                    id=f'{concept}-{variable}-Attribute-input',
                                ))],  id=f'{concept}-{variable}-input-column'))
            elements.append(dbc.Col(children=col_elements, id=f'col-{concept}-attribute-input',  class_name='col-4'))
    if elements == []:
        elements.append(dbc.Col(html.H3('There are no attributes.')))
    return dbc.Row(elements)

# Boolean Value Submit
@callback(
    Output('P-submit-attributes', 'children'),
    Input('button-submit-attribute-input', 'n_clicks'),
    State('div-attribute-input-elements', 'children')
)
def update_submit_attribute_input(n_clicks, div_elements):
    global problemInput
    if n_clicks:
        row_children = div_elements['props']['children']
        for concept_column in row_children:
            for concept_elem in concept_column['props']['children']:
                if concept_elem['type'] == 'Row':
                    input_columns = concept_elem['props']['children']
                    for elem in input_columns:
                        if elem['props']['children']['type'] == 'Input':
                            input_elem = elem['props']['children']
                            id_elements = input_elem['props']['id'].replace('-Attribute-input', '').split('-', 1) # list with first element is concept, second is variable, third is 'input'
                            input_value = input_elem['props']['value']
                            if input_value == '':
                                input_value = 'None'
                            problemInput.set_value(id_elements[0], id_elements[1], input_value)
    return ''

# All remaining Variable Value Input
# once the boolean variables are submitted show all variables and allow input and mark as reachable
@callback(
    Output(component_id='div-variable-value-input-elements', component_property='children'),
    Input('button-submit-attribute-input', 'n_clicks')
)
def update_variable_value_input(n_clicks):
    # name, input and radio button (required yes or no) for each variable
    # grouped by concept
    elements = []
    if not n_clicks:
        return dbc.Row(elements)


    for concept in problemInput.get_concepts():
        if list(problemInput.get_variables(concept)):
            col_elements = []
            col_elements.append(html.H3(f'{concept}:', id=f'{concept}-Variable-Heading'))
            for variable in problemInput.get_variables(concept):
                if problemInput.get_unit_of_variable(variable) != '':
                    unit_elem = dbc.InputGroupText(dcc.Markdown(r'${'+problemInput.get_unit_of_variable(variable)+r'}$', mathjax=True), id=f'{concept}-{variable}-Unit-P')
                else:
                    unit_elem = []
                disabled_vars = ['id', 
                                 'equation_of_state', 'transition',
                                 'final_state', 'initial_state', 'related_changes_and_states']
                status = 'allowed'
                if variable in disabled_vars:
                    status = 'disabled'          
                col_elements.append(dbc.Row([
                    dbc.Col(dbc.InputGroup(
                        [dbc.InputGroupText(f'{variable}:', id=f'{concept}-{variable}-Variable-P'), 
                        dbc.Input(type='text', #todo
                                  disabled = variable in disabled_vars,
                                  value=problemInput.get_value(concept, variable),
                                  id=f'{concept}-{variable}-Variable-input'),
                        unit_elem,
                        dbc.InputGroupText(dbc.Checklist(
                                options=[{"label": "required", "value": 'required', "disabled": variable in disabled_vars}],
                                value=['required'] if problemInput.is_required(concept, variable) else [],
                                id=f'{concept}-{variable}-required-checklist',
                                switch=True,
                                label_checked_style={"color": "red"},
                                input_checked_style={
                                    "backgroundColor": "#fa7268",
                                    "borderColor": "#ea6258",
                                },
                                ))
                        ],
                        class_name="mb-2", id=f"{concept}-{variable}-{status}-Input"
                    ))
                ]))
            elements.append(dbc.Col(children=col_elements, id=f'col-{concept}-variable-input', class_name='col-4'))
    if elements == []:
        elements.append(dbc.Col(html.H3('There are no variables.')))
    return dbc.Row(elements)

# Final Submit Button Feedback
@callback(
    Output('div-solution-values-elements', 'children'),
    Output('cytoscape-solution-path', 'elements'),
    Output('cytoscape-reasoning-graph', 'elements'),
    Input('button-submit-input', 'n_clicks'),
    Input('radio-select-problem-class', 'value'),
    State('div-variable-value-input-elements', 'children'),
    prevent_initial_call=True
)
def update_submit(n_clicks, type_chosen, div_elements):
    solution_elements = [html.P('Waiting for KnowTD')]
    cyto_elements = {}
    cyto_reasoning_elements = {}
    if n_clicks and ctx.triggered_id=='button-submit-input' :
        # read input
        if isinstance(div_elements['props']['children'], list):
            for child in div_elements['props']['children']:
                for concept_row in child['props']['children']:
                    if concept_row['type'] == 'Row':
                        for col_element in concept_row['props']['children']:
                            inputGroup = col_element['props']['children']['props']['children'] #InputGroup children
                            if 'allowed' in col_element['props']['children']['props']['id']:
                                [input_concept, input_variable] = inputGroup[0]['props']['id'].replace('-Variable-P', '').split('-', 1) # list with first element is concept, second is variable
                                input_value = inputGroup[1]['props']['value']
                                input_required = inputGroup[3]['props']['children']['props']['value']
                                # handle value input
                                if input_value == '':
                                    input_value = 'None' #todo: try to change variable directly.
                                problemInput.set_value(input_concept, input_variable, input_value)
                                # handle required input
                                if input_required == ['required']:
                                    problemInput.add_required(input_concept, input_variable)
                                elif problemInput.is_required(input_concept, input_variable):
                                    problemInput.remove_required(input_concept, input_variable)

        problemInput.writeYAML()
        #solve
        try:
            problemInput.send_to_solver()
            (required_output, other_output) = problemInput.get_solution_elements_required()
        except:
            print("An exception occurred in KnowTD")
            solution_elements = [html.P("An exception occurred in KnowTD", id='solution-result-P')]
            (required_output, other_output) = ({},{})
        #read output
        if required_output:
            table_header = [
                        html.Thead(html.Tr([html.Th("Variable"), html.Th("Value")]))
                    ]
            rows = [html.Tr([html.Td(dcc.Markdown(f'${variable}$', mathjax=True)),
                              html.Td(dcc.Markdown(f'${required_output[variable]}$', mathjax=True))], className='table-primary') for variable in required_output]
            rows += [html.Tr([html.Td(dcc.Markdown(f'${variable}$', mathjax=True)), html.Td(dcc.Markdown(f'${other_output[variable]}$', mathjax=True))]) for variable in other_output]
            table_body = [html.Tbody(rows)]
            solution_elements = [dbc.Table(table_header + table_body, bordered=True, hover=True, striped=False, responsive=True)]
            cyto_elements = problemInput.get_graph_elements()
            cyto_reasoning_elements = problemInput.get_reasoning_graph_elements()
            # todo here is how to get the graph elements cyto_elements = problemInput.get_reasoning_graph_elements()
        else:
            solution_elements += [html.P('Found no solution.', id='solution-result-P')]
    return solution_elements, cyto_elements, cyto_reasoning_elements

# @callback(
#     Output('cytoscape-solution-path-output', 'children'),
#     Output('cytoscape-solution-path-output', 'className'),
#     Input('cytoscape-solution-path', 'selectedNodeData'),
#     Input('button-reset-solution-graph', 'n_clicks'),
#     Input('button-submit-input', 'n_clicks'),
#     Input('radio-select-problem-class', 'value'),
#     Input('button-submit-attribute-input', 'n_clicks'),
#     Input('radio-select-example', 'value'),
#     prevent_initial_call=True
# )
# def displayTapNodeData(datalist, *n_clicks):
#     content="Click on a node to see its details here"
#     if ctx.triggered_id == 'cytoscape-solution-path':
#         if datalist is not None:
#             if len(datalist)>0:
#                 data=datalist[-1]
#                 content = [f"You recently selected the node: {data['label']} ", 
#                            f"value: {data['value']} ",
#                            f"type: {data['type']}"]

#         return content, 'visible'
#     elif ctx.triggered_id == 'button-submit-input' or ctx.triggered_id=='button-reset-solution-graph':
#         return content, 'visible'
#     else:
#         return '', 'invisible'
    
@callback(
    Output('cytoscape-solution-path', 'zoom'),
    Output('cytoscape-reasoning-graph', 'zoom'),
    Input('slider-solution-graph-zoom', 'value')
)
def update_zoom(value):
    return value, value

@callback(
    Output('collapse-solution', 'is_open'),
    Input('button-submit-input', 'n_clicks'),
    Input('radio-select-problem-class', 'value'),
    Input('radio-select-example', 'value'),
    Input('button-submit-attribute-input', 'n_clicks'),
)
def toggle_solution_graph_elements(n_clicks, v1, v2, v3):
    if ctx.triggered_id == 'button-submit-input':
        return True
    else:
        return False

@callback(
    Output('slider-solution-graph-zoom', 'value'),
    Output('cytoscape-solution-path', 'layout'),
    Output('cytoscape-solution-path', 'elements', allow_duplicate=True),
    Output('cytoscape-reasoning-graph', 'layout'),
    Output('cytoscape-reasoning-graph', 'elements', allow_duplicate=True),
    Input('button-reset-solution-graph', 'n_clicks'),
    prevent_initial_call=True
)
def reset_cyto_graph(n_clicks):
    if n_clicks:
        return 1, get_node_layout('tree'), problemInput.get_graph_elements(), get_node_layout('force'), problemInput.get_reasoning_graph_elements()

# sample Problems
@callback(
    Output('P-selected-example', 'children'),
    Output('P-selected-example', 'mathjax'),
    Output('radio-select-problem-class', 'value'),
    Output('button-submit-attribute-input', 'n_clicks'),
    Input('radio-select-example', 'value')
)
def update_example_selection(example_chosen):
    global problemInput

    if 'Single Step ' in example_chosen:
        problemInput = ProblemInput.SampleSingleStep(example_chosen.replace('Single Step ', ''))
        return problemInput.question, True, 'Single Step', 2
    elif 'Cyclic Process ' in example_chosen:
        problemInput = ProblemInput.SampleCyclicProcess(example_chosen.replace('Cyclic Process ', ''))
        return problemInput.question, True, 'Cyclic Process', 2
    else:
        return '', False, '', None

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

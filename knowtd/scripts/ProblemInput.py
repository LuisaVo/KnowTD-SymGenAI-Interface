from pprint import pprint
from ProblemHandler import ProblemHandler
from ProblemSolver import ProblemSolver
import OutputRendering
import OntologyProblemInput

class ProblemInput():
    def __init__(self, problemClass='SystemProblem'):
        self.problemClass = problemClass
        self.concepts = self.get_concepts_from_ontology(problemClass)
        self.yamlInput = ''
        self.required_variables = list()

        self.solver = None
        self.solution = None
        self.handler = None

    def check_input(self):
        """Checks if the input is consistant. 
        At the moment it only checks if something is required. 
        Todo: check if required is actually in the problem."""
        if not self.required_variables:
            return False
        return True
        # if required not in possible variables return false
        # currently never called
    
    def writeYAML(self):
        """generates the yaml file which can be given to the ProblemHandler"""
        finalYamlData = {'problem_class': self.problemClass,
                         'system': self.concepts['System'],
                         'pureMaterial': self.concepts['Material'],
                         'required_variables': self.required_variables}
        if 'State' in self.concepts: 
            finalYamlData['state'] = self.concepts['State']
        elif 'States' in self.concepts: 
            finalYamlData['states']  = self.concepts['States']
        if 'ChangeOfState' in self.concepts and isinstance(self.concepts['ChangeOfState'], list):
            finalYamlData['change_of_states']  = self.concepts['ChangeOfState']
        elif 'ChangeOfState' in self.concepts and isinstance(self.concepts['ChangeOfState'], dict):
            finalYamlData['change_of_state']  = self.concepts['ChangeOfState']
        self.yamlInput = convert_to_string(remove_None(finalYamlData))
        self.yamlInput['system']['related_changes_and_states'] = self.concepts['System']['related_changes_and_states']
        return

    def get_concepts(self):
        """returns a list of all concept ids of the problem class"""
        for concept in self.concepts:
            if concept == 'States':
                for elem in self.concepts[concept]:
                    yield f"State {elem['id']}"
            elif concept == 'ChangeOfState':
                if isinstance(self.concepts[concept], dict):
                    yield concept
                    yield 'Transition'
                elif isinstance(self.concepts[concept], list):
                    for elem in self.concepts[concept]:
                        yield f"ChangeOfState {elem['id']}"
                        yield f"Transition {elem['transition']['id']}"
            elif concept == 'Material':
                yield concept
                yield 'EquationOfState'
            else:
                yield concept
    
    def get_variables(self, concept, include_attributes=False):
        """returns a list of all variables (bool, num and string) of a concept"""
        target = self._get_concept(concept)
        if include_attributes:
            return target.keys()
        else:
            attributes = list(self.get_attributes(concept))
            return [key for key in target.keys() if not key in attributes]
        
    def get_unit_of_variable(self, variable):
        """given a variable, returns the unit in plain string"""
        if variable in OutputRendering.unit_mapping:
            if OutputRendering.unit_mapping[variable] != 'none' and OutputRendering.unit_mapping[variable] != None:
                return f"{OutputRendering.latex_typsetting(OutputRendering.unit_mapping[variable])}"
            else: 
                return ""
        else:
            return ""
    
    def get_attributes(self, concept):
        """yields all attributes of a concept"""
        # todo überarbeiten mit target
        target = self._get_concept(concept)
        for variable in target:
            if isinstance(target[variable], bool) or not isinstance(target[variable], dict):
                yield variable
            if variable in ['transition', 'equation_of_state']:
                yield variable
    
    def get_value(self, concept, variable):
        """returns a string with the value of the corresponding variable"""
        target = self._get_concept(concept, variable)
        value = target[variable]
        if isinstance(value, dict) and 'value' in value:
            value = value['value']
        if isinstance(value, bool):
            if value == False:
                value = 'False'
            elif value == True:
                value = 'True'
        if ('ChangeOfState' in concept and variable == 'transition') or ('Material' in concept and variable == 'equation_of_state'):
            value = value['id']
        return str(value)
    
    def set_value(self, concept:str, variable:str, value:any):
        """sets the value of the corresponding variable.
        Bool, String and Numbers will be set accordingly.
        Returns nothing"""
        # check if bool
        if value == 'True':
            value = True
        elif value == 'False':
            value = False
        elif value == 'None':
            value = None
        elif isinstance(value, bool):
            pass
        # check if number
        elif variable=='id':
            value = str(value)
        elif isinstance(value, str) and value.startswith('[') and value.endswith(']'):
            value = value.strip("]['").split("', '")
        else:
            try:
                value = float(value)
                if value.is_integer():
                    value = int(value)
            except ValueError:
                pass
            except TypeError:
                pass

        target = self._get_concept(concept, variable)
        if isinstance(target[variable], dict):
            if 'value' in target[variable]:
                target[variable]['value'] = value
            else:
                # variable is inline object, ignore it as it occurs in list of concepts
                pass
                #raise Exception(f"Found the variable {variable} of concept {concept}. Variable is inline object.")
        else:
            target[variable] = value

    def add_required(self, concept, variable):
        """ Adds the variable with indicator of concept to the required list.
        Throws an Exception if variable, concept or id cannot be found."""
        if self.is_required(concept, variable):
            return
        target = self._get_concept(concept, variable)

        if target and 'id' in target:
            self.required_variables.append(f"{variable}_{target['id']}")
        else:
            raise Exception(f"Could not find the variable {variable} or concept {concept}.")
    
    def is_required(self, concept, variable):
        """ Returns True if the variable of the concept is required. 
        Throws an Exception if variable or concept cannot be found."""
        return f'{variable}_{self.get_value(concept, "id")}' in self.required_variables
    
    def remove_required(self, concept, variable):
        if self.is_required(concept, variable):
            self.required_variables.remove(f'{variable}_{self.get_value(concept, "id")}')

    def initialize_solver(self):
        # get directory of module
        ontology_filename = "Ontology/thermodynamics_ontology.yaml"
        
        # preprocess the input and add information from ontology
        self.handler = ProblemHandler(ontology_filename, self.yamlInput)
        # apply solving techniques
        self.solver = ProblemSolver(list(self.handler.instances('Variable')), 
                       self.handler.create_equations(), 
                       self.handler.problem.required_variables)
        
    def start_solver(self):
        if self.solver:
            self.solution = self.solver.solve()
            return self.solution
        else:
            return {}
                
    def send_to_solver(self):
        """Initializes the ProblemHandler and the ProblemSolver and starts the solver. 
        Returns the solution as dict. Does not return solution path"""
        self.initialize_solver()
        return self.start_solver()

    def get_graph_elements(self):
        """If a solution exists, return the cyto elements of the solution path"""
        if self.solver and self.solver.G_optimized and self.solution:
            return OutputRendering.return_cyto_graph_elements(
                self.solver.G_optimized,
                self.solution,
                self.required_variables
                )
        else:
            return []
        
    def get_reasoning_graph_elements(self):
        """If a solution exists, return the cyto elements of the reasoning path"""
        if self.solver and self.solver.G_reasoning and self.solution:
            return OutputRendering.return_cyto_graph_elements(
                self.solver.G_reasoning,
                self.solution,
                self.required_variables
                )
        else:
            return []
        
    def get_all_equations(self):
        """returns a tuple with dictionaries of all available equations and all used equations. 
        The dictionary contains equation name and sympy equation.
        returns (all_equations, used_equations)"""
        return {elem['data']['id']: elem['data']['value'] for elem in self.get_reasoning_graph_elements() if 'classes' in elem and elem['classes'] == 'equation'}, {elem['data']['id']: elem['data']['value'] for elem in self.get_graph_elements() if 'classes' in elem and elem['classes'] == 'equation'}

    def get_solution_elements(self):
        output = dict()
        for variable in self.solution:
            output[OutputRendering.variable_typsetting_brackets(variable)] = f'{OutputRendering.latex_typsetting(OutputRendering.get_variable_label(variable, self.solution[variable]))}'
        return output

    def get_solution_elements_required(self):
        output = dict()
        required_output = dict()
        for variable in self.solution:
            if variable in self.required_variables:
                required_output[OutputRendering.variable_typsetting_brackets(variable)] = f'{OutputRendering.latex_typsetting(OutputRendering.get_variable_label(variable, self.solution[variable]))}'
            else:
                output[OutputRendering.variable_typsetting_brackets(variable)] = f'{OutputRendering.latex_typsetting(OutputRendering.get_variable_label(variable, self.solution[variable]))}'
        return (required_output, output)

    def __str__(self):
        return f'problem class: {self.problemClass}\n concepts: {self.concepts}\n required: {self.required_variables}'
    
    def _get_concept(self, concept, variable=None):
        """Finds the corresponding concept element in self.concepts"""
        target = ''
        if 'Transition' in concept and isinstance(self.concepts['ChangeOfState'], list):
            id = concept.replace('Transition ', '')
            for change in self.concepts['ChangeOfState']:
                if change['transition']['id'] == id or change['transition']['id'] == str(id):
                    target = change['transition']
        elif 'ChangeOfState' in concept and isinstance(self.concepts['ChangeOfState'], list):
            id = concept.replace('ChangeOfState ', '')
            for change in self.concepts['ChangeOfState']:
                if change['id'] == id or change['id'] == str(id):
                    target = change
        elif concept in self.concepts:
            target = self.concepts[concept]
        elif concept == 'Transition' and 'ChangeOfState' in self.concepts:
            target = self.concepts['ChangeOfState']['transition']
        elif 'State ' in concept:
            id = concept.replace('State ', '')
            if 'States' in self.concepts:
                for state in self.concepts['States']:
                    if str(state['id']) == str(id):
                        target = state
            elif 'State' in self.concepts:
                target = self.concepts['State']
        elif 'EquationOfState' in concept:
            target = self.concepts['Material']['equation_of_state']
        
        if target == '':
            raise Exception(f"Could not find the concept {concept}.")
        
        if variable:
            if variable in target:
                return target
            else:
                raise Exception(f"Could not find the variable {variable} of the concept {concept}.")
        else:
            # only look for target
            return target
                
    def get_concepts_from_ontology(self, problemClass):
        '''Access the ontology and get readable concept dict of the problem class.'''
        return {''.join(x for x in elem.replace('pure', '').replace('_states','_state').replace('_', ' ').title() if not x.isspace()): val for (elem,val) in list(OntologyProblemInput.get_problem_concepts(problemClass).items())}
    
class Equilibrium(ProblemInput):
    def __init__(self, problemClass='Equilibrium'):
        super().__init__('Equilibrium')

class SingleStep(ProblemInput):
    def __init__(self, problemClass='SingleStep'):
        super().__init__('SingleStep')
        self.concepts['ChangeOfState']['initial_state'] = '1'
        self.concepts['ChangeOfState']['final_state'] = '2'

class SequentialSteps(ProblemInput):
    def __init__(self,numStates=3, problemClass='SequentialSteps'):
        super().__init__(problemClass)
        if numStates < 3:
            raise ValueError("Cannot create an instance of this class with less than 3 states.")
        self.numberOfStates = len(self.concepts['States'])
        while self.numberOfStates < numStates:
            self.add_state()
        while len(self.concepts['ChangeOfState']) < numStates - 1:
            self.add_change_of_state()
        for i in range(0, len(self.concepts['ChangeOfState'])):
            self.concepts['ChangeOfState'][i]['initial_state'] = str(i+1) #todo
            self.concepts['ChangeOfState'][i]['final_state'] = str(i+2)
    
    def add_state(self):
        """adds a new state at the last position of the sequence"""#todo
        self.numberOfStates += 1
        self.concepts['States'].append(get_state_dict(self.numberOfStates))

    def add_change_of_state(self):
        """adds a new change_of_state at the last position of the sequence"""#todo
        num_change_of_states = len(self.concepts['ChangeOfState'])
        new_id = next_letter_sequence(self.concepts['ChangeOfState'][-1]['id'])
        self.concepts['ChangeOfState'].append(get_change_of_state_dict(new_id, num_change_of_states+1, num_change_of_states+2))
        self.concepts['System']['related_changes_and_states'].append(new_id)

    
class CyclicProcess(SequentialSteps):
    def __init__(self, numStates=3, problemClass='ChangeOfState'):
        super().__init__(numStates=numStates, problemClass='CyclicProcess')
        if len(self.concepts['States']) != len(self.concepts['ChangeOfState']):
            self.add_change_of_state()
        if len(self.concepts['States']) != len(self.concepts['ChangeOfState']):
            raise NotImplementedError(f'There is an implementation error. Please check the init method for {problemClass} with {numStates} States')
        self.concepts['ChangeOfState'][-1]['final_state'] = '1'
        self.concepts['ChangeOfState'][-1]['transition']['id'] = f'{numStates}1'

class SampleSingleStep(SingleStep):
    def __init__(self, num=1):
        super().__init__()
        if num == '1':
            self.set_value('Material', 'R', 287)
            self.set_value('Material', 'c_v', 1010)
            self.set_value('State 1', 'v', 0.05)
            self.set_value('State 1', 'T', 298)
            self.set_value('State 2', 'v', 0.02)
            self.set_value('Transition', 'adiabatic', 'True')
            self.set_value('Transition', 'reversible', 'True')
            self.set_value('Transition', 'is_isentropic', 'True')
            self.add_required('Transition', 'w')
            self.question = '''A gas in a cylinder is compressed reversibly from $v_1 = 0.05 \\frac{m^3}{kg}$ to $v_2 = 0.02 \\frac{m^3}{kg}$. The initial temperature is $T_1 = 298 K$. 
            The process is adiabatic. 
            What is the work supplied per kilogram of gas? 
            The gas is ideal, with $R = 287 \\frac{J}{kg K}$ and $c_v = 1010 \\frac{J}{kg K}$.'''
        elif num == '2':
            self.set_value('Material', 'R', 277)
            self.set_value('Material', 'c_v', 1746)
            self.set_value('State 1', 'v', 0.7)
            self.set_value('State 1', 'p', 200000)
            self.set_value('State 2', 'v', 1.1)
            self.set_value('Transition', 'is_polytropic', 'True')
            self.set_value('Transition', 'n_poly', 0.8)
            self.add_required('Transition', 'w')
            self.add_required('Transition', 'q')
            self.add_required('Transition', 'del_s')
            self.question = '''A gas in a cylinder undergoes a polytropic expansion with the exponent $n = 0.8$. 
            The initial pressure and specific volume are $p_1 = 2$ bar and $v_1 = 0.7 \\frac{m^3}{kg}$, the final specific volume is $v_2 = 1.1 \\frac{m^3}{kg}$. 
            Calculate the following quantities per kilogram of gas: work, heat, entropy change.  
            The gas is ideal, with $R = 277 \\frac{J}{kg K}$ and $c_v = 1746 \\frac{J}{kg K}$.'''
        elif num == '3':
            self.set_value('Material', 'R', 518)
            self.set_value('State 1', 'p', 100000)
            self.set_value('State 1', 'T', 298)
            self.set_value('State 2', 'p', 160000)
            self.set_value('Transition', 'is_isothermal', 'True')
            self.add_required('Transition', 'q')
            self.question = '''A gas in a cooled cylinder undergoes an isothermal compression at $T = 298 K$. 
            The initial and final pressure are $p_1 = 1$ bar, $p_2 = 1.6$ bar. 
            Calculate the heat that has to be removed per kilogram of gas.
            The gas is ideal, with $R = 518 \\frac{J}{kg K}$.'''
        elif num == '4':
            self.set_value('Material', 'R', 117)
            self.set_value('Material', 'c_v', 479)
            self.set_value('State 1', 'v', 0.2)
            self.set_value('State 1', 'p', 170000)
            self.set_value('State 2', 'v', 0.5)
            self.set_value('State 2', 'p', 105000)
            self.set_value('Transition', 'w', -8700)
            self.add_required('Transition', 'q')
            self.question = '''A gas in a heated cylinder is expanded. 
            The pressure changes from $p_1 = 1.7$ bar to $p_2 = 1.05$ bar, the specific volume changes from and $v_1 = 0.2 \\frac{m^3}{kg}$ to $v_2 = 0.5 \\frac{m^3}{kg}$, the work obtained per kilogram of gas is $8.7 \\frac{kJ}{kg}$. 
            Calculate the heat that is supplied per kilogram of gas.
            The gas is ideal, with $R = 117 \\frac{J}{kg K}$ and $c_v = 479 \\frac{J}{kg K}$.'''
        elif num == '5':
            self.set_value('Material', 'R', 297)
            self.set_value('Material', 'c_v', 1040)
            self.set_value('State 1', 'v', 0.8)
            self.set_value('State 1', 'p', 100000)
            self.set_value('State 2', 'v', 1.5)
            self.set_value('Transition', 'is_isobaric', 'True')
            self.add_required('Transition', 'q')
            self.question = '''A gas in a cylinder is expanded, whereby the specific volume increases from $v_1 = 0.8 \\frac{m^3}{kg}$ to $v_2 = 1.5 \\frac{m^3}{kg}$. 
            The cylinder is heated in such a way that the pressure $p = 1$ bar remains constant during the entire process. 
            Calculate the work and the heat per kilogram of gas.
            The gas is ideal, with $R = 297 \\frac{J}{kg K}$ and $c_v = 1040 \\frac{J}{kg K}$.'''
        elif num == '6':
            self.set_value('Material', 'R', 287)
            self.set_value('Material', 'c_v', 1010)
            self.set_value('State 1', 'V', 0.05)
            self.set_value('State 1', 'T', 315)
            self.set_value('State 1', 'p', 100000)
            self.set_value('State 2', 'T', 320)
            self.set_value('Transition', 'W', 500)
            self.add_required('Transition', 'Q')
            self.question = ''' A gas in rigid tank with the volume $V = 0.05 m^3$ is stirred. 
            The initial temperature and pressure are $T_1 = 315 K$, $p_1 = 1$ bar. 
            The stirrer supplies a work of $0.5 kJ$. 
            The tank is cooled, as there is a threshold for the final temperature. 
            Calculate the heat that is removed if the final temperature is $T_2 = 320 K$. 
            The gas is ideal, with $R = 287 \\frac{J}{kg K}$ and $c_v = 1010 \\frac{J}{kg K}$.'''
        elif num == '7':
            self.set_value('Material', 'M', 0.044)
            self.set_value('State 1', 'v', 0.52)
            self.set_value('State 1', 'p', 100000)
            self.set_value('State 2', 'v', 0.2)
            self.set_value('State 2', 'p', 300000)
            self.set_value('Transition', 'is_isentropic', 'True')
            self.add_required('Material', 'c_vm')
            self.question = '''A gas in a cylinder is compressed isentropically. 
            The pressure and specific volume change from $p_1 = 1$ bar, $v_1 = 0.52 \\frac{m^3}{kg}$ to $p_2 = 3$ bar, $v_2 = 0.2 \\frac{m^3}{kg}$. 
            Calculate the molar heat capacity at constant volume $c_{vm}$ of the gas under the assumption that $c_{vm}$ is constant.
            The gas is ideal, its molar mass is $M = 44 \\frac{g}{mol}$.'''
        elif num == '8':
            self.set_value('System', 'm', 1)
            self.set_value('State 1', 'V', 0.8)
            self.set_value('State 1', 'T', 298)
            self.set_value('State 1', 'p', 100000)
            self.set_value('State 2', 'T', 333)
            self.set_value('State 2', 'p', 290000)
            self.set_value('Transition', 'is_isentropic', 'True')
            self.add_required('Material', 'c_vm')
            self.add_required('Material', 'M')
            self.question = '''A cylinder contains $m = 1 kg$ of an ideal gas. 
            The initial volume, pressure and temperature are $V_1 = 0.8 m^3$, $p_1 = 1$ bar, and $T_1 = 298 K$. 
            After an adiabatic reversible compression, the final pressure and temperature are $p_2 = 2.9$ bar, and $T_2 = 333 K$. 
            Calculate the molar mass of the gas, and its molar heat capacity at constant volume $c_{vm}$.'''
        elif num == '9':
            self.set_value('Material', 'R', 297)
            self.set_value('Material', 'c_v', 1040)
            self.set_value('State 1', 'v', 0.8)
            self.set_value('State 1', 'T', 298)
            self.set_value('State 2', 'v', 0.5)
            self.set_value('Transition', 'is_isentropic', 'True')
            self.add_required('Transition', 'w')
            self.question = '''A gas in a cylinder is compressed adiabatically. 
            The initial temperature and specific volume are $T_1 = 298 K$ and $v_1 = 0.8 \\frac{m^3}{kg}$. 
            The final volume is $v_2 = 0.5 \\frac{m^3}{kg}$. Calculate the minimal work that is required per kilogram of gas for this compression.
            The gas is ideal, with $R = 297 \\frac{J}{kg K}$ and $c_v = 1040 \\frac{J}{kg K}$.'''
        elif num == '10':
            self.set_value('Material', 'c_v', 1746)
            self.set_value('State 1', 'rho', 1.2)
            self.set_value('State 1', 'T', 298)
            self.set_value('State 1', 'V', 0.01)
            self.set_value('Transition', 'adiabatic', 'True')
            self.set_value('Transition', 'W', 1000)
            self.add_required('State 2', 'T')
            self.question = '''A gas with the density $\\rho = 1.2 \\frac{kg}{m^3}$ in a rigid adiabatic tank with the volume $V = 0.01 m^3$ is stirred. 
            The initial temperature is $T_1 = 298 K$. 
            Calculate the temperature $T_2$ in the tank, after the stirrer has supplied a work of $1 kJ$. 
            The gas is ideal with $c_v = 1746 \\frac{J}{kg K}$.'''
        elif num == '11':
            self.set_value('Material', 'c_v', 479)
            self.set_value('State 1', 'T', 298)
            self.set_value('State 2', 'T', 353)
            self.set_value('Transition', 'Q', 1300)
            self.set_value('Transition', 'is_isochoric', 'True')
            self.add_required('System', 'm')
            self.question = '''A gas in a closed rigid cylinder is heated by up from $T_1 = 298 K$ to $T_2 = 353 K$. 
            The supplied heat is $1.3 kJ$. 
            Calculate the mass of the gas in the cylinder. 
            The gas is ideal with $c_v = 479 \\frac{J}{kg K}$.'''
        elif num == '12':
            self.set_value('Material', 'M', 0.028)
            self.set_value('Material', 'c_v', 1040)
            self.set_value('State 1', 'p', 190000)
            self.set_value('State 1', 'v', 0.9)
            self.set_value('State 2', 'p', 100000)
            self.set_value('State 2', 'v', 1.5)
            self.set_value('Transition', 'q', 0)
            self.set_value('Transition', 'adiabatic', 'True')
            self.add_required('Transition', 'w')
            self.add_required('Transition', 'del_s')
            self.question = '''A gas in a cylinder expands adiabatically. 
            The initial pressure and specific volume are $p_1 = 1.9$ bar and $v_1 = 0.9 \\frac{m^3}{kg}$, the final pressure and specific volume are $p_2 = 1$ bar and $v_2 = 1.5 \\frac{m^3}{kg}$. 
            Calculate the work per kilogram of gas and the change of the specific entropy.
            The gas is ideal with $c_v = 1040 \\frac{J}{kg K}$ and has a molar mass of $28 \\frac{g}{mol}$.'''
        elif num == '13':
            self.set_value('Material', 'M', 0.03)
            self.set_value('Material', 'c_v', 1009)
            self.set_value('State 1', 'p', 210000)
            self.set_value('State 1', 'T', 273)
            self.set_value('State 2', 'p', 100000)
            self.set_value('Transition', 'is_isentropic', 'True')
            self.set_value('Transition', 'is_polytropic', 'True')
            self.add_required('Transition', 'w')
            self.question = ''' gas in a cylinder undergoes an adiabatic polytropic expansion. 
            The initial pressure and temperature are $p_1 = 2.1$ bar and $T_1 = 273 K$, the final pressure is $p_2 = 1$ bar. 
            Calculate the work per kilogram of gas.
            The gas is ideal with $c_v = 1009 \\frac{J}{kg K}$ and has a molar mass of $30 \\frac{g}{mol}$.'''

class SampleCyclicProcess(CyclicProcess):
    def __init__(self, num=1):
        super().__init__(4)
        self.question = ''
        if num == '1':
            self.set_value('State 1', 'T', 300)
            self.set_value('State 1', 'p', 200000)
            self.set_value('State 2', 'p', 1000000)
            self.set_value('Material', 'R', 290)
            self.set_value('Material', 'c_p', 1015)
            self.set_value('Transition 12', 'is_isentropic', 'True')
            self.set_value('Transition 23', 'is_isobaric', 'True')
            self.set_value('Transition 23', 'q', '50000')
            self.set_value('Transition 34', 'adiabatic', 'True')
            self.set_value('Transition 34', 'reversible', 'True')
            self.set_value('Transition 34', 'is_isentropic', 'True')
            self.set_value('Transition 41', 'is_isobaric', 'True')
            self.add_required('State 2', 'T')
            self.add_required('State 3', 'T')
            self.add_required('State 4', 'T')
            self.add_required('Transition 23', 'w_i')
            self.add_required('Transition 41', 'del_u')
            self.question = r'''We consider a gas in a compartment closed by a movable piston. In the initial state, the piston is locked and the gas is under the temperature $T_1 = 300 K$ and the pressure $p_1 = 2 bar$. In a first step, the locking mechanism is released: the gas is compressed by the piston and undergoes an isentropic compression to $p_2 = 10 bar$ (State 1 $\rightarrow$ State 2). The gas is then isobarically heated, the supplied heat per kilogram of gas is $q_{23} = 50 \frac{kJ}{kg}$ (State 2 $\rightarrow$ State 3). Finally, the moving piston enables an adiabatic and reversibel expansion of the gas to $p_4 = p_1$ (State 3 $\rightarrow$ State 4). The gas then undergoes an isobaric cooling and reaches the state 1 (State 4 $\rightarrow$ State 1).

- Calculate the temperature $T_2$
- Calculate the temperature $T_3$
- Calculate the internal work w_i done on the gas during the step 2 $\rightarrow$ 3
- Calculate the temperature $T_4$
- Calculate the specific internal energy difference $\Delta u$ during the step 4 $\rightarrow$ 1

Assumptions:
- Changes in kinetic and potential energy can be neglected
- The gas is a perfect gas
- The changes of state occur through equilibria

Gas properties:
- $c_p = 1.015 \frac{kJ}{kg K}$
- $R = 0.29 \frac{kJ}{kg K}$'''

        elif num == '2':
            self.set_value('Transition 12', 'is_isothermal', 'True')
            self.set_value('State 1', 'V', 0.001)
            self.set_value('Transition 23', 'adiabatic', 'True')
            self.set_value('Transition 23', 'reversible', 'True')
            self.set_value('Transition 23', 'is_isentropic', 'True')
            self.set_value('State 2', 'V', 0.01)
            self.set_value('State 3', 'T', 301)
            self.set_value('Transition 34', 'adiabatic', 'True')
            self.set_value('Transition 34', 'reversible', 'True')
            self.set_value('Transition 34', 'is_isentropic', 'True')
            self.set_value('State 4', 'V', 0.005)
            self.set_value('Transition 41', 'reversible', 'True')
            self.set_value('System', 'm', 0.03)
            self.set_value('Material', 'c_v', 1009)
            self.set_value('Material', 'M', 0.03)
            self.add_required('State 1', 'T')
            self.add_required('Transition 12', 'q')
            self.add_required('Transition 34', 'q')
            self.add_required('State 1', 'p')
            self.add_required('State 2', 'p')
            self.add_required('State 3', 'p')
            self.add_required('State 4', 'p')
            self.question = r'''Heat is isothermally transferred to $V_1 = 1 L$ of gas during the first step (State 1 $\rightarrow$ State 2). Then follows an adiabatic and reversible expansion of the gas up to $V_2 = 10 L$, reducing the temperature to $T_3 = 301 K$ (State 2 $\rightarrow$ State 3). Heat then isothermally dissipates from the system, the volume decreases down to $V_4 = 6.5 L$ (State 3 $\rightarrow$ State 4). Finally, the gas undergoes an  diabatic and reversible compression, increasing the temperature back to $T_1$ (State 4 $\rightarrow$ State 1). 

- Calculate the temperature $T_1$
- Calculate the supplied heat $q_12$ per kilogram of gas.
- Calculate the removed heat $q_34$ per kilogram of gas.
- We consider $m = 30.0 g$ of gas. Calculate for each state the corresponding pressure.

Assumptions:
- Changes in kinetic and potential energy are negligible
- The gas stays a perfect gas during the cycle
- The changes of state occur through equilibria

Substance data:
- $c_v = 1009 \frac{J}{kg K}$
- $M = 30 \frac{g}{mol}$'''

        elif num == '3':
            self.set_value('Transition 12', 'is_isothermal', 'True')
            self.set_value('State 1', 'V', 0.001)
            self.set_value('Transition 23', 'adiabatic', 'True')
            self.set_value('Transition 23', 'reversible', 'True')
            self.set_value('Transition 23', 'is_isentropic', 'True')
            self.set_value('State 2', 'V', 0.01)
            self.set_value('State 3', 'T', 301)
            self.set_value('Transition 34', 'adiabatic', 'True')
            self.set_value('Transition 34', 'reversible', 'True')
            self.set_value('Transition 34', 'is_isentropic', 'True')
            self.set_value('State 4', 'V', 0.005)
            self.set_value('Transition 41', 'reversible', 'True')
            self.set_value('System', 'm', 0.03)
            self.set_value('Material', 'c_v', 1009)
            self.set_value('Material', 'M', 0.03)
            self.add_required('State 1', 'T')
            self.add_required('Transition 12', 'q')
            self.add_required('Transition 34', 'q')
            self.add_required('State 1', 'p')
            self.add_required('State 2', 'p')
            self.add_required('State 3', 'p')
            self.add_required('State 4', 'p')
            self.question = r'''Heat is isothermally transferred to $V_1 = 1 L$ of gas during the first step (State 1 $\rightarrow$ State 2). Then follows an adiabatic and reversible expansion of the gas up to $V_2 = 10 L$, reducing the temperature to $T_3 = 301 K$ (State 2 $\rightarrow$ State 3). Heat then isothermally dissipates from the system, the volume decreases down to $V_4 = 6.5 L$ (State 3 $\rightarrow$ State 4). Finally, the gas undergoes an  diabatic and reversible compression, increasing the temperature back to $T_1$ (State 4 $\rightarrow$ State 1). 

- Calculate the temperature $T_1$
- Calculate the supplied heat $q_12$ per kilogram of gas.
- Calculate the removed heat $q_34$ per kilogram of gas.
- We consider $m = 30.0 g$ of gas. Calculate for each state the corresponding pressure.

Assumptions:
- Changes in kinetic and potential energy are negligible
- The gas stays a perfect gas during the cycle
- The changes of state occur through equilibria

Substance data:
- $c_v = 1009 \frac{J}{kg K}$
- $M = 30 \frac{g}{mol}$'''

        elif num == '4':
            self.set_value('Transition 12', 'is_isothermal', 'True')
            self.set_value('State 1', 'V', 0.001)
            self.set_value('Transition 23', 'adiabatic', 'True')
            self.set_value('Transition 23', 'reversible', 'True')
            self.set_value('Transition 23', 'is_isentropic', 'True')
            self.set_value('State 2', 'V', 0.01)
            self.set_value('State 3', 'T', 301)
            self.set_value('Transition 34', 'adiabatic', 'True')
            self.set_value('Transition 34', 'reversible', 'True')
            self.set_value('Transition 34', 'is_isentropic', 'True')
            self.set_value('State 4', 'V', 0.005)
            self.set_value('Transition 41', 'reversible', 'True')
            self.set_value('System', 'm', 0.03)
            self.set_value('Material', 'c_v', 1009)
            self.set_value('Material', 'M', 0.03)
            self.add_required('State 1', 'T')
            self.add_required('Transition 12', 'q')
            self.add_required('Transition 34', 'q')
            self.add_required('State 1', 'p')
            self.add_required('State 2', 'p')
            self.add_required('State 3', 'p')
            self.add_required('State 4', 'p')
            self.question = r'''Heat is isothermally transferred to $V_1 = 1 L$ of gas during the first step (State 1 $\rightarrow$ State 2). Then follows an adiabatic and reversible expansion of the gas up to $V_2 = 10 L$, reducing the temperature to $T_3 = 301 K$ (State 2 $\rightarrow$ State 3). Heat then isothermally dissipates from the system, the volume decreases down to $V_4 = 6.5 L$ (State 3 $\rightarrow$ State 4). Finally, the gas undergoes an  diabatic and reversible compression, increasing the temperature back to $T_1$ (State 4 $\rightarrow$ State 1). 

- Calculate the temperature $T_1$
- Calculate the supplied heat $q_12$ per kilogram of gas.
- Calculate the removed heat $q_34$ per kilogram of gas.
- We consider $m = 30.0 g$ of gas. Calculate for each state the corresponding pressure.

Assumptions:
- Changes in kinetic and potential energy are negligible
- The gas stays a perfect gas during the cycle
- The changes of state occur through equilibria

Substance data:
- $c_v = 1009 \frac{J}{kg K}$
- $M = 30 \frac{g}{mol}$'''

def get_state_dict(state_id):
    return {'id': str(state_id),
            'T': {'value': None},
            'p': {'value': None},
            'V': {'value': None},
            'v': {'value': None},
            'rho': {'value': None},
            'U': {'value': None},
            'u': {'value': None},
            'H': {'value': None},
            'h': {'value': None},
            'S': {'value': None},
            's': {'value': None},
            'sm': {'value': None},
            'c': {'value': None},
            'z': {'value': None},
            'E_kin': {'value': None},
            'e_kin': {'value': None},
            'E_pot': {'value': None},
            'equilibrium': True
            }

def get_change_of_state_dict(change_id, initial, final):
    return {'id': str(change_id),
            'initial_state': str(initial),
            'final_state': str(final),
            'transition': get_transition_dict(str(initial)+str(final))
            }

def get_transition_dict(transition_id):
    return {'id': str(transition_id),
            'equilibrium': None,
            'motion': False,
            'adiabatic': None,
            'reversible': None,
            'is_isothermal': None,
            'is_isochoric': None,
            'is_polytropic': None,
            'is_isobaric': None,
            'is_isenthalpic': None,
            'is_isentropic': None,
            'Q': {'value': None},
            'q': {'value': None},
            'W': {'value': None},
            'w': {'value': None},
            'W_i': {'value': None},
            'w_i': {'value': None},
            'W_a': {'value': None},
            'w_a': {'value': None},
            'w_t': {'value': None},
            'del_T': {'value': None},
            'del_p': {'value': None},
            'del_V': {'value': None},
            'del_v': {'value': None},
            'del_U': {'value': None},
            'del_u': {'value': None},
            'del_H': {'value': None},
            'del_h': {'value': None},
            'del_S': {'value': None},
            'del_s': {'value': None},
            'del_sm': {'value': None},
            'del_c': {'value': None},
            'del_z': {'value': None},
            'del_E_kin': {'value': None},
            'del_e_kin': {'value': None},
            'del_E_pot': {'value': None},
            'del_e_pot': {'value': None},
            'n_poly': {'value': None},
            'ratio_T': {'value': None},
            'ratio_p': {'value': None},
            'ratio_v': {'value': None}
            }

def next_letter_sequence(s):
    if s == "":
        return "A"

    # Convert the string to a list of characters
    letters = list(s)
    
    # Start from the last character and move backwards
    for i in range(len(letters) - 1, -1, -1):
        if letters[i] == 'Z':
            letters[i] = 'A'
            # If we are at the first character and it is 'Z', prepend 'A'
            if i == 0:
                letters.insert(0, 'A')
        else:
            # Move to the next character in the alphabet
            letters[i] = chr(ord(letters[i]) + 1)
            break
    
    return ''.join(letters)

    
def remove_None(d):
    if isinstance(d, dict):
        for (key, val) in list(d.items()):
            if isinstance(val, dict) and 'value' in val and val['value'] == None:
                del d[key]
            elif val == None:
                del d[key]
            elif isinstance(val, dict) or isinstance(val, list):
                remove_None(val)
    if isinstance(d, list):
        for elem in d:
            remove_None(elem)
    if d == {} or d == None:
        del d
    return d

def convert_to_string(d):
    if isinstance(d, dict):
        return {str(key): convert_to_string(val) for key, val in list(d.items())}
    elif isinstance(d, list):
        return [convert_to_string(elem) for elem in d]
    elif isinstance(d, int) or isinstance(d, float) or isinstance(d, bool):
        return d
    else:
        return str(d)
        

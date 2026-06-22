from os import mkdir
from os.path import exists

import GenerateProblem
from linkml_runtime.dumpers import yaml_dumper
from knowtd.scripts.ProblemHandler import ProblemHandler

path='../GeneratedProblems'

if not exists(path):
    mkdir(path)

ontology_filename = "../knowtd/Ontology/thermodynamics_ontology.yaml"
    
def write_equations(problem_class_dir, problem_class, attributes={}, name=""):
    problem = GenerateProblem.ProblemGenerator(problem_class, attributes=attributes, only_template=True)
    handler = ProblemHandler(ontology_filename, problem.problem_element)
    eqns = handler.create_equations()
    with open(f"{problem_class_dir}/{problem_class}_{name}_equations.txt", "w") as f:
        for eq in eqns:
            f.write(eq.as_text + "\n")
            
def gen_problem_with_values(problem_class_dir, problem_class, attributes={}, values={}, name=""):
    problem = GenerateProblem.ProblemGenerator(problem_class, attributes=attributes, values=values, only_template=False, version=4, print_solution=True)
    yaml_dumper.dump(problem.problem_element, f"{problem_class_dir}/{problem_class}_{name}_long.yaml", default_flow_style=False)
    clean_dict(problem.problem_element)
    yaml_dumper.dump(problem.problem_element, f"{problem_class_dir}/{problem_class}_{name}.yaml", default_flow_style=False)
    yaml_dumper.dump(problem.expected_solution, f"{problem_class_dir}/{problem_class}_{name}_solution.yaml", default_flow_style=False)
    yaml_dumper.dump(problem.solution_path, f"{problem_class_dir}/{problem_class}_{name}_solution_path.yaml", default_flow_style=False)
    
def gen_problem_template(problem_class_dir, problem_class, attributes={}, name=""):
    problem = GenerateProblem.ProblemGenerator(problem_class, attributes=attributes, only_template=True)
    yaml_dumper.dump(problem.problem_element, f"{problem_class_dir}/{problem_class}_{name}_template.yaml", default_flow_style=False)    

def clean_dict(dict_to_clean):
    # print('check dict:', dict_to_clean)
    remove_list = []
    for key, value in dict_to_clean.items():
        if isinstance(value, dict):
            if 'value' in value and value['value'] is None:
                remove_list.append(key)
            else:
                clean_dict(value)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    clean_dict(item)
    for key in remove_list:
        del dict_to_clean[key]
        
# results from IDP
case1 = {
    '01': {'adiabatic': False, 'reversible': False, 'isothermal': False, 'isochoric': False, 'polytropic': False, 'isobaric': False, 'isentropic': False},
    '02': {'adiabatic': False, 'reversible': False, 'isothermal': False, 'isochoric': True,  'polytropic': False, 'isobaric': False, 'isentropic': False},
    '03': {'adiabatic': False, 'reversible': True,  'isothermal': False, 'isochoric': True,  'polytropic': False, 'isobaric': False, 'isentropic': False}
}
case2 = {
    '04': {'adiabatic': True, 'reversible': False, 'isothermal': False, 'isochoric': False, 'polytropic': False, 'isobaric': False, 'isentropic': False},
    '05': {'adiabatic': True, 'reversible': False, 'isothermal': False, 'isochoric': True,  'polytropic': False, 'isobaric': False, 'isentropic': False},
    '06': {'adiabatic': True, 'reversible': True,  'isothermal': False, 'isochoric': False, 'polytropic': True,  'isobaric': False, 'isentropic': True}
}
case3 = {
    '07': {'adiabatic': False, 'reversible': False, 'isothermal': False, 'isochoric': False, 'polytropic': False, 'isobaric': False, 'isentropic': False},
    '08': {'adiabatic': False, 'reversible': False, 'isothermal': False, 'isochoric': True,  'polytropic': False, 'isobaric': False, 'isentropic': False},
    '09': {'adiabatic': False, 'reversible': True,  'isothermal': False, 'isochoric': False, 'polytropic': False, 'isobaric': False, 'isentropic': False},
    '10': {'adiabatic': False, 'reversible': True,  'isothermal': False, 'isochoric': False, 'polytropic': True,  'isobaric': False, 'isentropic': False},
    '11': {'adiabatic': False, 'reversible': True,  'isothermal': False, 'isochoric': False, 'polytropic': True,  'isobaric': True,  'isentropic': False},
    '12': {'adiabatic': False, 'reversible': True,  'isothermal': True,  'isochoric': False, 'polytropic': True,  'isobaric': False, 'isentropic': False}
}


if __name__ == "__main__":
    # mass generation case 1 to 3:
    problem_class = 'SingleStep'
    cases = {'Q!=0, W=0': case1, 'Q=0, W!=0': case2, 'Q!=0, W!=0': case3}

    for index in case1:
        problem_class_dir = f'{path}/NoWork'
        print(10*'*')
        print(f'case Q!=0, W=0 Generate Problem {index}')
        print(10*'*')
        elem = case1[index]
        attribute_assignment = [('12', f'is_{attr}', val) if attr not in ['adiabatic', 'reversible'] else ('12', attr, val) for attr, val in elem.items()]     
        write_equations(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, name=f'Scenario_{index}')
        gen_problem_template(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, name=f'Scenario_{index}')
        # gen_problem_with_values(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, values={'W_12': 0, 'w_12': 0}, name=f'NoWork_{index}')
        
    for index in case2:
        print(10*'*')
        print(f'case Q=0, W!=0 Generate Problem {index}')
        print(10*'*')
        problem_class_dir = f'{path}/NoHeat'
        elem = case2[index]
        attribute_assignment = [('12', f'is_{attr}', val) if attr not in ['adiabatic', 'reversible'] else ('12', attr, val) for attr, val in elem.items()]    
        write_equations(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, name=f'Scenario_{index}')
        gen_problem_template(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, name=f'Scenario_{index}')
        # gen_problem_with_values(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, values={'Q_12': 0, 'q_12': 0}, name=f'NoHeat_{index}')
        
    for index in case3:
        print(10*'*')
        print(f'case Q!=0, W!=0 Generate Problem {index}')
        print(10*'*')
        problem_class_dir = f'{path}/HeatAndWork'
        elem = case3[index]
        attribute_assignment = [('12', f'is_{attr}', val) if attr not in ['adiabatic', 'reversible'] else ('12', attr, val) for attr, val in elem.items()]
        write_equations(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, name=f'Scenario_{index}')
        gen_problem_template(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, name=f'Scenario_{index}')
        # gen_problem_with_values(problem_class_dir=problem_class_dir, problem_class=problem_class, attributes=attribute_assignment, values={}, name=f'Heat_And_Work_{index}')
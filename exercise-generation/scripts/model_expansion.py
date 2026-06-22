from idp_engine import Theory, IDP, model_check
from idp_engine.Expression import AND, NOT, FALSE, EQUALS
from pprint import pprint

idp = IDP.from_file('scripts/Thermodynamics-knowledgebase.idp')
T, S_default, S_vanilla = idp.get_blocks("T, S_default, S_vanilla")
attributes = [
    'transition_has_case(12)',
    'transition_has_type(12, adiabatic)',
    'transition_has_type(12, reversible)',
    'transition_has_type(12, isothermal)',
    'transition_has_type(12, isochoric)',
    'transition_has_type(12, polytropic)',
    'transition_has_type(12, isobaric)',
    'transition_has_type(12, isentropic)'
]

theory = Theory(T, S_default)

valid_combinations = []

while model_check(theory):
    model = list(theory.expand(1, complete=True))[0]
    if isinstance(model, str):
        # No more models.
        break

    # Prepare a new constraint.
    conj = []
    this_valid_combination = []
    for attr in attributes:
        value = model[attr]
        if value.value == FALSE:
            conj.append(NOT(value.sentence))
        elif attr == 'transition_has_case(12)':
            this_valid_combination.append(str(model[attr].value))
            conj.append(EQUALS([model[attr].sentence, model[attr].value]))
        else:
            this_valid_combination.append(str(model[attr]).replace('transition_has_type(12, ', '')[:-1])
            conj.append(value.sentence)
    
    new_constr = NOT(AND(conj))
    theory.constraints[str(new_constr)] = new_constr
    
    valid_combinations.append(this_valid_combination)

    # Wipe the cache.
    theory._constraintz = None
    theory._slvr = None
    
    
# Results
print('-----------------------------------')
print('Resulting Scenarios:')
case1 = [[elem for elem in c if elem != 'case1'] for c in valid_combinations if 'case1' in c]
case2 = [[elem for elem in c if elem != 'case2'] for c in valid_combinations if 'case2' in c]
case3 = [[elem for elem in c if elem != 'case3'] for c in valid_combinations if 'case3' in c]

print("\nCase 1 combinations:")
print(f"Found {len(case1)} combinations:")
pprint(case1)

print('-----------------------------------')
print("\nCase 2 combinations:")
print(f"Found {len(case2)} combinations:")
pprint(case2)

print('-----------------------------------')
print("\nCase 3 combinations:")
print(f"Found {len(case3)} combinations:")
pprint(case3)

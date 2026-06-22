from idp_engine import Theory, IDP, model_check
from idp_engine.Expression import AND, NOT, FALSE, EQUALS
from pprint import pprint

idp = IDP.from_file('scripts/Triangle_example.idp')
T, S = idp.get_blocks("T, S")
attributes = [
    'has_angle_type()',
    'has_side_type(equilateral)',
    'has_side_type(isosceles)',
    'has_side_type(general)'
]

theory = Theory(T, S)

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
        elif attr == 'has_angle_type()':
            this_valid_combination.append(str(model[attr].value))
            conj.append(EQUALS([model[attr].sentence, model[attr].value]))
        else:
            this_valid_combination.append(str(model[attr]).replace('has_side_type(', '')[:-1])
            conj.append(value.sentence)
    
    new_constr = NOT(AND(conj))
    theory.constraints[str(new_constr)] = new_constr
    
    valid_combinations.append((len(valid_combinations)+1, this_valid_combination))

    # Wipe the cache.
    theory._constraintz = None
    theory._slvr = None
    
    
# Results
print('-----------------------------------')
print('Resulting Scenarios:')
for (id, elem) in valid_combinations:
    print(f"Scenario {id}: {elem}")

case1 = [(id, [elem for elem in c if elem != 'right']) for (id,c) in valid_combinations if 'right' in c]
case2 = [(id, [elem for elem in c if elem != 'obtuse']) for (id,c) in valid_combinations if 'obtuse' in c]
case3 = [(id, [elem for elem in c if elem != 'acute']) for (id,c) in valid_combinations if 'acute' in c]

print('-----------------------------------')
print()

print('Scenarios split by angle attribute:')
print('-----------------------------------')
print()
print("\nCase 1 right combinations:")
print(f"Found {len(case1)} combinations:")
for (id, elem) in case1:
    print(f"Scenario {id}: {elem}")

print('-----------------------------------')
print("\nCase 2 obtuse combinations:")
print(f"Found {len(case2)} combinations:")
for (id, elem) in case2:
    print(f"Scenario {id}: {elem}")

print('-----------------------------------')
print("\nCase 3 acute combinations:")
print(f"Found {len(case3)} combinations:")
for (id, elem) in case3:
    print(f"Scenario {id}: {elem}")

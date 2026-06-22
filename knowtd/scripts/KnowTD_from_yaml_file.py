# run this code in the command line: python test/KnowTD_from_yaml_file.py
from ProblemHandler import ProblemHandler
from ProblemSolver import ProblemSolver

ontology_filename = "Ontology/thermodynamics_ontology.yaml"
problem_filename = "SampleProblems/Problem3.yaml" # specify your yaml file here

handler = ProblemHandler(ontology_filename, problem_filename)

# send the input to KnowTD
solver = ProblemSolver(list(handler.instances('Variable')), 
                       handler.create_equations(), 
                       handler.problem.required_variables)

# obtain solution
solution = solver.solve()

# print solution
print('Solution:')
print({s: solution[s] for s in solution if s in handler.problem.required_variables})

print('Intermediate Solutions:')
print({s: solution[s] for s in solution if s not in handler.problem.required_variables})

# If you are interested in the solution path you can view it here:
solver.draw_nx(solver.G_optimized, values=solution)

# print all equations

# print('All equations')
# pprint(solver.equations)
# print('Used equations')
# pprint({n: solver.equations[n] for n in solver.G_optimized.nodes() if n in solver.equations})

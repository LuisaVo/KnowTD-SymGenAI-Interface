"""
utils/knowTD_solver.py
======================

Adapter layer between the Streamlit interface and the KnowTD ProblemSolver.
"""

import sys, os
sys.path.insert(0, os.path.abspath("knowtd/scripts"))
sys.path.insert(0, os.path.abspath("knowtd"))
from knowtd.scripts.ProblemHandler import ProblemHandler
from knowtd.scripts.ProblemSolver import ProblemSolver
from knowtd.scripts import OutputRendering

class Solver():
    def __init__(self, ontology_file: str, problem_file: str = ''):
        self.ontology_file = ontology_file
        self.problem_file = problem_file
        
    def load_problem(self, problem_file: str) -> bool:
        """Load the problem definition from a YAML file. Validate the file format and returns a boolean indicating success."""
        if self.validate_problem_file(problem_file):
            self.problem_file = problem_file
            return True
        else:            
            return False
    
    def validate_problem_file(self, problem_file: str) -> bool:
        # Placeholder for validation logic
        return True

    def solve(self) -> dict:
        """Load the ontology and problem definition, then solve the problem using the KnowTD ProblemSolver.
        Returns a dictionary containing the solution, including all solved variables, required variables, intermediate variables, and equations used.
        """
        handler = ProblemHandler(self.ontology_file, self.problem_file)
        solver = ProblemSolver(list(handler.instances('Variable')), 
                               handler.create_equations(), 
                               handler.problem.required_variables)
        solution = solver.solve()
        
        return {'status': 'success' if solution and all(r in solution for r in handler.problem.required_variables) else 'failure',
                'all': solution, 
                'required': {s: solution[s] for s in solution if s in handler.problem.required_variables}, 
                'intermediate': {s: solution[s] for s in solution if s not in handler.problem.required_variables}, 
                'equations_all': solver.equations,
                'equations_used': {n: solver.equations[n] for n in solver.G_optimized.nodes() if n in solver.equations},
                'nodes+edges': OutputRendering.return_cyto_graph_elements(solver.G_optimized, solution, handler.problem.required_variables),
                }
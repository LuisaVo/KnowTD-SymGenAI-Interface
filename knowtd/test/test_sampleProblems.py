# create python version of ontology:
# gen-python Ontology/thermodynamics_ontology.yaml > scripts/thermo_ontology.py

import unittest
import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), "Scripts"))
sys.path.append(os.path.join(os.getcwd(), "scripts"))

from ProblemHandler import ProblemHandler
from ProblemSolver import ProblemSolver

class TestSampleProblems(unittest.TestCase):
    def setUp(self):
        self.ontology_filename = "Ontology/thermodynamics_ontology.yaml"
        self.directory = "SampleProblems"
        self.solutions = {   
            'SampleProblems/Problem1.yaml' : {'w_12': '89515.15'},
            'SampleProblems/Problem2.yaml' : {'w_12': '-66226.15', 'del_s_12': '283.03', 'q_12': '149714.13'},
            'SampleProblems/Problem3.yaml' : {'q_12': '-72551.64'},
            'SampleProblems/Problem4.yaml' : {'q_12': '84439.32'},
            'SampleProblems/Problem5.yaml' : {'q_12': '315117.85', 'w_12': '-70000.0000000000'},
            'SampleProblems/Problem6.yaml' : {'Q_12': '-220.70'},
            'SampleProblems/Problem7.yaml' : {'c_vm_Gas': '55.52'},
            'SampleProblems/Problem8.yaml' : {'M_Gas': '0.03', 'c_vm_Gas': '71.40'},
            'SampleProblems/Problem9.yaml' : {'w_12': '44519.05'},
            'SampleProblems/Problem10.yaml' : {'T_2': '345.73'},
            'SampleProblems/Problem11.yaml' : {'m_I': '0.05'},
            'SampleProblems/Problem12.yaml' : {'del_s_12': '15.42', 'w_12': '-73548.95'},
            'SampleProblems/Problem13.yaml' : {'w_12': '-40699.41'},
            'SampleProblems/CyclicProcess2-1.yaml': {'T_2': '475.15', 'T_3': '524.41', 'T_4': '331.10', 'del_u_41': '-22549.47', 'w_i_23': '-14285.71'},
            'SampleProblems/CyclicProcess2-2.yaml': {'q_34': '0'},
            }

    def test_eachProblem(self):
        for filename in os.listdir(self.directory):
            if 'yaml' in filename:
                f = os.path.join(self.directory, filename)
                # checking if it is a file
                if os.path.isfile(f):
                    with self.subTest(f=f):
                        handler = ProblemHandler(self.ontology_filename, f)
                        solver = ProblemSolver(list(handler.instances('Variable')), 
                                            handler.create_equations(), 
                                            handler.problem.required_variables)
                        solution = solver.solve()
                        self.assertIsNot(solution, {})
                        solution = {s: str(round(solution[s],2)) for s in solution if s in handler.problem.required_variables}
                        self.assertIn(f, self.solutions)
                        self.assertEqual(solution, self.solutions[f])


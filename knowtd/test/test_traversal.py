# sympy test
import sympy
import networkx as nx
from pprint import pprint
import unittest
import sys, os
sys.path.append(os.path.join(os.getcwd(), "Scripts"))
from ProblemSolver import ProblemSolver
# from ProblemHandler import ProblemHandler


class EquationObject():
    id = 1
    def __init__(self, as_text):
        self.id = f'Eq{EquationObject.id}'
        EquationObject.id += 1
        self.name = 'Eq'
        self.as_text = as_text
        # print(f'created Equation {self.id=}, {self.name=}, {self.as_text=}')

class SymbolObject():
    id = 1
    def __init__(self, name, value=None):
        self.id = f'{name}_{SymbolObject.id}'
        SymbolObject.id += 1
        self.value = value
        # print(f'created Symbol {self.id=}, {self.value=}')

class TestTraversal(unittest.TestCase): 
    def setUp(self) -> None:
        symbol_list = [SymbolObject('a', 2.5), SymbolObject('b'), SymbolObject('x', 0.0), SymbolObject('y'), SymbolObject('z'), SymbolObject('m'), SymbolObject('m')]
        equation_list= [EquationObject('a_1 + b_2 = 4'),
                        EquationObject('x_3 * y_4 + z_5 = 1.5'),
                        EquationObject('m_6 + m_7 = 99'),
                        EquationObject('m_6 + m_7 + b_2 = 100.5'),]
        self.problem_solver = ProblemSolver(symbol_list, 
                                            equation_list, 
                                            ['b_2', 'z_5'])
        
        # print(self.problem_solver.symbols)
        # print(self.problem_solver.assignments)
        # print(self.problem_solver.equations)
        # print(self.problem_solver.find)
    
    def tearDown(self) -> None:
        EquationObject.id = 1
        SymbolObject.id = 1
        
    def test_initReasoningGraph(self):
        self.problem_solver._init_reasoning_graph()
        node_set = set(['a_1', 'b_2', 'x_3', 'Eq1', 'Assignmenta_1'])
        edge_set = set([('a_1', 'Eq1'), ('a_1', 'Assignmenta_1'), ('b_2', 'Eq1')])
        self.assertTrue(set(self.problem_solver.G_reasoning.nodes()).issuperset(node_set))
        self.assertTrue(set(self.problem_solver.G_reasoning.edges()).issuperset(edge_set))
        
    def test_reasoning_traversal(self):
        self.problem_solver._init_reasoning_graph()
        self.problem_solver._reasoning_traversal()

        self.assertIn('b_2', self.problem_solver.G_traversal)
        self.assertTrue(self.problem_solver.G_traversal.nodes['Eq1'].get('reachable'))
        self.assertTrue(self.problem_solver.G_traversal.nodes['Assignmenta_1'].get('reachable'))
        self.assertTrue(self.problem_solver.G_traversal.nodes['a_1'].get('reachable'))
        self.assertTrue(self.problem_solver.G_traversal.nodes['b_2'].get('reachable'))
        self.assertTrue(self.problem_solver.G_traversal.nodes['Assignmentx_3'].get('reachable'))
        self.assertTrue(self.problem_solver.G_traversal.nodes['x_3'].get('reachable'))
        self.assertTrue(self.problem_solver.G_traversal.nodes['Eq2'].get('reachable'))
        self.assertTrue(self.problem_solver.G_traversal.nodes['z_5'].get('reachable'))

        self.assertFalse(self.problem_solver.G_traversal.nodes['y_4'].get('reachable'))
        self.assertFalse(self.problem_solver.G_traversal.nodes['m_6'].get('reachable'))
        self.assertFalse(self.problem_solver.G_traversal.nodes['m_7'].get('reachable'))

        self.assertEqual(self.problem_solver.G_traversal.nodes['b_2'].get('value'), 1.5)
        self.assertEqual(self.problem_solver.G_traversal.nodes['z_5'].get('value'), 1.5)

        self.assertEqual(self.problem_solver.G_traversal.nodes['y_4'].get('value'), None)
        self.assertEqual(self.problem_solver.G_traversal.nodes['m_6'].get('value'), None)
        self.assertEqual(self.problem_solver.G_traversal.nodes['m_7'].get('value'), None)

        # self.problem_solver.draw_nx(self.problem_solver.G_traversal)
    
    def test_simplify(self):
        self.problem_solver._init_reasoning_graph()
        self.problem_solver._reasoning_traversal()
        self.problem_solver._simplify()

        self.assertIn('b_2', self.problem_solver.G_optimized.nodes())
        self.assertIn('z_5', self.problem_solver.G_optimized.nodes())

        self.assertIn('a_1', self.problem_solver.G_optimized.nodes())
        self.assertIn('x_3', self.problem_solver.G_optimized.nodes())
        
        # not sure if it should be included
        self.assertNotIn('y_4', self.problem_solver.G_optimized.nodes())

        self.assertNotIn('m_6', self.problem_solver.G_optimized.nodes())
        self.assertNotIn('m_7', self.problem_solver.G_optimized.nodes())

        # self.problem_solver.draw_nx(self.problem_solver.G_optimized)

    def test_solve(self):
        solution = self.problem_solver.solve()
        # solve initializes, traverses and simplifies the reasoning graph
        self.assertEqual(solution['b_2'], 1.5)
        self.assertEqual(solution['z_5'], 1.5)

if __name__ == '__main__':  
    unittest.main()

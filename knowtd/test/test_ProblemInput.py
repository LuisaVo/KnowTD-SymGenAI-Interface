from pprint import pprint
import unittest
import sys, os
import yaml
# sys.path.append(os.path.join(os.path.dirname(__file__), "Scripts"))
sys.path.append(os.path.join(os.getcwd(), "scripts"))

from ProblemInput import *
  
class TestProblemInput(unittest.TestCase): 

    def test_Equilibrium(self):
        test = Equilibrium()
        self.assertNotIn('States', test.concepts)
        self.assertNotIn('ChangeOfState', test.concepts)
        self.assertIn('State', test.concepts)


    def test_SingleStep_simpleAccess(self):
        test = SingleStep()
        self.assertIn('States', test.concepts)
        self.assertEqual(len(test.concepts['States']), 2)
        self.assertIn('ChangeOfState', test.concepts)
        self.assertNotIsInstance(test.concepts['ChangeOfState'], list)
        self.assertNotIn('State', test.concepts)

    def test_SequentialSteps(self):
        test = SequentialSteps()
        self.assertIn('States', test.concepts)
        self.assertEqual(len(test.concepts['States']), 3)
        self.assertIn('ChangeOfState', test.concepts)
        self.assertIsInstance(test.concepts['ChangeOfState'], list)
        self.assertEqual(len(test.concepts['ChangeOfState']), 2)
        self.assertNotIn('State', test.concepts)
        
        test = SequentialSteps(numStates=4)
        self.assertEqual(len(test.concepts['ChangeOfState']), 3)
        self.assertEqual(test.concepts['ChangeOfState'][0]['initial_state'], '1')
        self.assertEqual(test.concepts['ChangeOfState'][1]['initial_state'], '2')
        self.assertEqual(test.concepts['ChangeOfState'][2]['initial_state'], '3')

        self.assertEqual(test.concepts['ChangeOfState'][0]['final_state'], '2')
        self.assertEqual(test.concepts['ChangeOfState'][1]['final_state'], '3')
        self.assertEqual(test.concepts['ChangeOfState'][2]['final_state'], '4')

        self.assertEqual(test.concepts['ChangeOfState'][0]['transition']['id'], '12')
        self.assertEqual(test.concepts['ChangeOfState'][1]['transition']['id'], '23')
        self.assertEqual(test.concepts['ChangeOfState'][2]['transition']['id'], '34')



    def test_CyclicProcess(self):
        test = CyclicProcess(numStates=4)
        # pprint(test.concepts)
        self.assertEqual(len(test.concepts['States']), 4)
        self.assertEqual(len(test.concepts['ChangeOfState']), 4)
        self.assertEqual(test.concepts['ChangeOfState'][0]['id'], 'A')
        self.assertEqual(test.concepts['ChangeOfState'][1]['id'], 'B')
        self.assertEqual(test.concepts['ChangeOfState'][2]['id'], 'C')
        self.assertEqual(test.concepts['ChangeOfState'][3]['id'], 'D')

        self.assertEqual(test.concepts['ChangeOfState'][0]['initial_state'], '1')
        self.assertEqual(test.concepts['ChangeOfState'][1]['initial_state'], '2')
        self.assertEqual(test.concepts['ChangeOfState'][2]['initial_state'], '3')
        self.assertEqual(test.concepts['ChangeOfState'][3]['initial_state'], '4')

        self.assertEqual(test.concepts['ChangeOfState'][0]['final_state'], '2')
        self.assertEqual(test.concepts['ChangeOfState'][1]['final_state'], '3')
        self.assertEqual(test.concepts['ChangeOfState'][2]['final_state'], '4')
        self.assertEqual(test.concepts['ChangeOfState'][3]['final_state'], '1')

        self.assertEqual(test.concepts['ChangeOfState'][0]['transition']['id'], '12')
        self.assertEqual(test.concepts['ChangeOfState'][1]['transition']['id'], '23')
        self.assertEqual(test.concepts['ChangeOfState'][2]['transition']['id'], '34')
        self.assertEqual(test.concepts['ChangeOfState'][3]['transition']['id'], '41')

    def test_get_concepts(self):
        test = SingleStep()
        self.assertIn('State 1', test.get_concepts())
        self.assertIn('Transition', test.get_concepts())
        self.assertNotIn('States', test.get_concepts())
        self.assertNotIn('State', test.get_concepts())

        test = Equilibrium()
        self.assertNotIn('State 1', test.get_concepts())
        self.assertNotIn('Transition', test.get_concepts())
        self.assertNotIn('States', test.get_concepts())
        self.assertIn('State', test.get_concepts())

        test = SequentialSteps()
        self.assertIn('State 1', test.get_concepts())
        self.assertIn('State 2', test.get_concepts())
        self.assertIn('ChangeOfState A', test.get_concepts())
        self.assertIn('ChangeOfState B', test.get_concepts())
        self.assertIn('Transition 12', test.get_concepts())
        self.assertIn('Transition 23', test.get_concepts())
        self.assertNotIn('Transition', test.get_concepts())
        self.assertNotIn('States', test.get_concepts())
        self.assertNotIn('State', test.get_concepts())

        test = CyclicProcess()
        self.assertIn('State 1', test.get_concepts())
        self.assertIn('State 2', test.get_concepts())
        self.assertIn('ChangeOfState A', test.get_concepts())
        self.assertIn('ChangeOfState B', test.get_concepts())
        self.assertIn('ChangeOfState C', test.get_concepts())
        self.assertIn('Transition 12', test.get_concepts())
        self.assertIn('Transition 23', test.get_concepts())
        self.assertIn('Transition 31', test.get_concepts())
        self.assertNotIn('Transition', test.get_concepts())
        self.assertNotIn('States', test.get_concepts())
        self.assertNotIn('State', test.get_concepts())

    def test_Get(self):
        test = SingleStep()
        test.concepts['States'][0]['T']['value'] = 300
        test.concepts['System']['m']['value'] = 5
        test.concepts['System']['equilibrium'] = False
        self.assertEqual(test.get_value('State 1', 'T'), '300')
        self.assertEqual(test.get_value('System', 'm'), '5')
        self.assertEqual(test.get_value('System', 'equilibrium'), 'False')        
        
        with self.assertRaises(Exception):
            test.get_value('Transition', 'test')

    def test_Set(self):
        test = SingleStep()
        test.set_value('System', 'm', 50)
        test.set_value('System', 'equilibrium', 'False')
        test.set_value('System', 'homogeneous', False)
        test.set_value('System', 'n', '3.125')
        test.set_value('State 1', 'V', '5')
        test.set_value('Transition', 'del_p', 5.1234)
        test.set_value('ChangeOfState', 'id', 'A')

        self.assertEqual(test.concepts['System']['m']['value'], 50)
        self.assertFalse(test.concepts['System']['equilibrium'])
        self.assertFalse(test.concepts['System']['homogeneous'])
        self.assertEqual(test.concepts['System']['n']['value'], 3.125)
        self.assertEqual(test.concepts['States'][0]['V']['value'], 5)
        self.assertEqual(test.concepts['ChangeOfState']['transition']['del_p']['value'], 5.1234)
        self.assertEqual(test.concepts['ChangeOfState']['id'], 'A')

        with self.assertRaises(Exception):
            test.set_value('Transition', 'test', '123')

    def test_Set_CyclicProcess(self):
        test = CyclicProcess(numStates=4)
        self.assertEqual(test.get_value('Transition 12', 'id'), '12')
        test.set_value('Transition 12', 'id', '12')
        self.assertEqual(test.get_value('Transition 12', 'id'), '12')
        test.set_value('Transition 12', 'is_isentropic', 'True')
        test.set_value('Transition 23', 'is_isobaric', 'True')
        test.set_value('Transition 34', 'q', 10)
        test.set_value('Transition 41', 'w', 10)
        self.assertEqual(test.concepts['ChangeOfState'][0]['transition']['is_isentropic'], True)
        self.assertEqual(test.concepts['ChangeOfState'][1]['transition']['is_isobaric'], True)
        self.assertEqual(test.concepts['ChangeOfState'][2]['transition']['q']['value'], 10)
        self.assertEqual(test.concepts['ChangeOfState'][3]['transition']['w']['value'], 10)

    def test_SetGet(self):
        test = SingleStep()

        test.set_value('System', 'm', 5)
        test.set_value('System', 'n', 5.55)
        test.set_value('System', 'equilibrium', 'False')
        test.set_value('System', 'homogeneous', False)
        test.set_value('Material', 'R', '5')
        test.set_value('Material', 'c_v', '5.41')
        test.set_value('Material', 'c_p', 'ABC')
        self.assertEqual(test.get_value('System', 'm'), '5')
        self.assertEqual(test.get_value('System', 'n'), '5.55')
        self.assertEqual(test.get_value('System', 'equilibrium'), 'False')
        self.assertEqual(test.get_value('System', 'homogeneous'), 'False')
        self.assertEqual(test.get_value('Material', 'R'), '5')
        self.assertEqual(test.get_value('Material', 'c_v'), '5.41')
        self.assertEqual(test.get_value('Material', 'c_p'), 'ABC')

    def test_required(self):
        test = SingleStep()
        test.required_variables.append('del_T_12')
        self.assertEqual(test.required_variables, ['del_T_12'])

        test.add_required('Transition', 'del_V')
        self.assertEqual(test.required_variables, ['del_T_12', 'del_V_12'])

        with self.assertRaises(Exception):
            test.add_required('Transition', 'test')
        
        test = CyclicProcess()
        test.required_variables.append('del_T_12')
        test.add_required('Transition 23', 'del_T')
        test.add_required('Transition 31', 'del_T')
        with self.assertRaises(Exception):
            test.add_required('Transition', 'del_T')
        self.assertEqual(test.required_variables, ['del_T_12', 'del_T_23', 'del_T_31'])

    def test_get_concept(self):
        test = SingleStep()
        # get_concept is used by set_value
        test.set_value('Transition', 'id', '13')
        self.assertEqual(test.get_value('Transition', 'id'), '13')
        with self.assertRaises(Exception):
            test.set_value('Transition', 'test', '13')
        with self.assertRaises(Exception):
            test.set_value('test', 'id', '13')

    def test_writeYAML(self):
        test = SingleStep()
        test.set_value('System', 'm', 50)
        test.set_value('State 1', 'p', 50)
        test.set_value('State 2', 'p', 50)
        test.add_required('System', 'n')
        # test = SampleSingleStep(5)
        test.writeYAML()
        # print(yaml.dump(test.yamlInput, default_flow_style=False))

        test = SampleSingleStep(5)
        test.writeYAML()
        self.assertIn('related_changes_and_states', test.yamlInput['system'])
        self.assertEqual(test.yamlInput['system']['related_changes_and_states'], ['A'])

        test = SampleCyclicProcess(1)
        test.set_value('System', 'related_changes_and_states', "['A', 'B', 'C', 'D']")
        test.writeYAML()
        self.assertIn('A', test.yamlInput['system']['related_changes_and_states'])
        self.assertIn('related_changes_and_states', test.yamlInput['system'])
        self.assertEqual(test.yamlInput['system']['related_changes_and_states'], ['A', 'B', 'C', 'D'])
  
    def test_get_boolean_variables(self):
        # todo
        pass

    def test_get_variables(self):
        # todo
        pass

    def test_initialize_solver(self):
        test = SingleStep()
        test.set_value('State 1', 'V', 5)
        test.set_value('State 2', 'V', 15)
        test.required_variables.append('del_V_12')
        test.writeYAML()
        solverdict = test.send_to_solver()
        self.assertEqual(solverdict, {'V_1': 5.00000000000000,
                                      'V_2': 15.0000000000000,
                                      'del_V_12': 10.0000000000000})

    def test_get_graph_elements(self):
        test = SingleStep()
        test.set_value('State 1', 'V', 5)
        test.set_value('State 2', 'V', 15)
        test.required_variables.append('del_V_12')
        test.writeYAML()
        self.assertEqual(test.get_graph_elements(), [])
        test.send_to_solver()
        self.assertTrue({'data': {'id': 'del_V_12', 'label': 'Delta V_12\n10 m^3', 'type': 'required', 'value': '10 m^3'}, 'classes': 'required'} in test.get_graph_elements())

    def test_generate_Problem_with_n_steps(self):
        test = SequentialSteps()
        self.assertListEqual(test.concepts['System']['related_changes_and_states'], ['A', 'B'])
        with self.assertRaises(ValueError):
         SequentialSteps(numStates=2)
        test = SequentialSteps(numStates=5)
        self.assertListEqual(test.concepts['System']['related_changes_and_states'], ['A', 'B', 'C', 'D'])

        test = CyclicProcess()
        self.assertListEqual(test.concepts['System']['related_changes_and_states'], ['A', 'B', 'C'])
        test = CyclicProcess(numStates=5)
        self.assertListEqual(test.concepts['System']['related_changes_and_states'], ['A', 'B', 'C', 'D', 'E'])


    def test_next_letter_sequence(self):
        self.assertEqual(next_letter_sequence('A'), 'B')
        self.assertEqual(next_letter_sequence('L'), 'M')
        self.assertEqual(next_letter_sequence('Z'), 'AA')
        self.assertEqual(next_letter_sequence('BL'), 'BM')
        self.assertEqual(next_letter_sequence('BZ'), 'CA')
if __name__ == '__main__':  
    unittest.main()
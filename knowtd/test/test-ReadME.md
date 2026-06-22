# How to Test

Using python module unittest to test the code

## How to write a test
- testfile must be named `test*.py`
- Create a class that inherits from unittest.Testcase
- write functions to test
- instead of assert use self.assertEqual self.assertTrue or self.assertFalse
- to test if an exception is fired use:
    `with self.assertRaises(Exception):
            #trigger whatever should throw the exception`
- setup and teardown possible

## How to start the tests
- start all tests: `python -m unittest`
- start a specific test: `python -m unittest test.test_ProblemInput`

## update Ontology
gen-python ontology/thermodynamics_ontology.yaml > scripts/thermo_ontology.py
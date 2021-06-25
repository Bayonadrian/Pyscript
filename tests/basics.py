import unittest
from scripts.basics.variables import variables

class TestVariables(unittest.TestCase, variables):

    def setUp(self) -> None:
        
        self.variable = variables()

    def test_var(self):

        self.assertEqual('var x = 3', self.variable.var('x', 3))

    def test_let(self):

        self.assertEqual('let x = 3', self.variable.let('x', 3))

    def test_const(self):

        self.assertEqual('const x = 3', self.variable.const('x', 3))

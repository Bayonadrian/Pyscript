import unittest
from scripts.basics.variables import variables
from scripts.basics.comments import comments
from scripts.basics.functions import functions

class TestVariables(unittest.TestCase, variables):

    def test_var(self):

        self.assertEqual('var x = 3;', self.var(x= 3))

        with self.assertRaises(Exception):

            self.var(x= 3, y= 2)         

        with self.assertRaises(Exception):

            self.var()

    def test_let(self):

        self.assertEqual('let x = 3;', self.let(x= 3))

        with self.assertRaises(Exception):

            self.let(x= 3, y= 2)

        with self.assertRaises(Exception):

            self.let()

    def test_const(self):

        self.assertEqual('const x = 3;', self.const(x= 3))

        with self.assertRaises(Exception):

            self.const(x= 3, y= 2)

        with self.assertRaises(Exception):

            self.const()

class TestComments(unittest.TestCase, comments):

    def test_comments(self):

        self.assertEqual('// Declare x', self.doComment('Declare x'))

class TestFunctions(unittest.TestCase, functions):

    def setUp(self) -> None:

        vars = (
            'uno',
            'dos',
        )

        body = (
            'var uno = 1',
            'var dos = 2',
            'return uno + dos'
        )
        
        self.fun = functions(name= 'fun', vars=vars, body=body)

    def test_func(self):

        self.assertEqual('''function fun(uno, dos){
     var uno = 1
     var dos = 2
     return uno + dos
}''', self.fun.func())

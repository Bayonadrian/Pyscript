import unittest
from scripts.basics.variables import variables
from scripts.basics.comments import comments

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

class TestComments(unittest.TestCase):

    def setUp(self) -> None:
        
        self.commment = comments()

    def test_comments(self):

        self.assertEqual('// Declare x', self.commment.doComment('Declare x'))

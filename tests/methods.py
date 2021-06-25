import unittest
from scripts.methods.strings import string

class TestStrings(unittest.TestCase, string):

    def test_getLen(self):

        self.assertEqual('var longitude = txt.length;', self.getLen('longitude', 'txt'))
        self.assertEqual('var longitude = "abcd".length;', self.getLen('longitude', 'abcd', False))

    def test_getSlice(self):

        self.assertEqual('var slice = txt.slice(5);', self.getSlice('slice', 'txt', 5))
        self.assertEqual('var slice = "abcd 1234 09876".slice(5);', self.getSlice('slice', 'abcd 1234 09876', 5, var= False))

        self.assertEqual('var slice = txt.slice(5, 8);', self.getSlice('slice', 'txt', 5, 8))
        self.assertEqual('var slice = "abcd 1234 09876".slice(5, 8);', self.getSlice('slice', 'abcd 1234 09876', 5, 8, var= False))

        with self.assertRaises(Exception):

            self.getSlice()

        with self.assertRaises(Exception):

            self.getSlice('slice', 'abcd 1234 09876', 5, 8, 9)

    def test_repl(self):

        self.assertEqual('var repl = txt.replace("r", "h");', self.repl(name= 'repl', txt= 'txt', rep= 'r', to= 'h'))
        self.assertEqual('var repl = "rabbit".replace("r", "h");', self.repl(name= 'repl', txt= 'rabbit', rep= 'r', to= 'h', var= False))
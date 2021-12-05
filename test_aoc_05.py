import unittest
from aoc_05 import *

class part01(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_check_line_ok(self):
        self.assertEqual(check_line(0,1,0,3),1)
        self.assertEqual(check_line(0,6,0,3),1)
        self.assertEqual(check_line(2,1,2,3),1)

    def test_check_line_diag(self):
        self.assertEqual(check_line(0,1,2,3),0)
        self.assertEqual(check_line(0,1,5,3),0)

if __name__ == '__main__':
    unittest.main()
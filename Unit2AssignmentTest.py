import unittest
import Unit2Assignment
from Unit2Assignment import adding_program
from Unit2Assignment import main
import math

class TestAddProgram(unittest.TestCase):

    def test_adding_program(self):
        self.assertEqual(adding_program(10,5), 15)

if __name__ == '__main__':
    unittest.main()


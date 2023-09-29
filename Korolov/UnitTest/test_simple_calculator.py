import unittest
from unittest import result

# import SimpleCalculator

class SimpleCalculator:
    def sum(self, a, b):
        return a + b

class MyTestCase(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def tearDown(self):
        print("\ntearDown executing after the test case. Result:")

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_addition_integer_string(self):
        result = self.calculator.sum(5, "6")
        self.assertEqual(result, "ERROR")

    def test_addition_negative_integers(self):
        result = self.calculator.sum(-5, -6)
        self.assertEqual(result, -11)
        self.assertNotEqual(result, 11)

if __name__ == '__main__':
    unittest.main()
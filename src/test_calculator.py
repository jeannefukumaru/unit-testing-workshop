import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add_1_and_1_should_return_2(self):
        self.assertEqual(2, add(1, 1))

class TestCalculator(unittest.TestCase):
    def test_subtract_2_and_1_should_return_1(self):
        self.assertEqual(1, subtract(2,1))

class TestCalculator(unittest.TestCase):
    def test_multiple_2_and_2_should_return_4(self):
        self.assertEqual(4, mult(2, 2))

class TestCalculator(unittest.TestCase):
    def test_divide_5_and_1_should_return_5(self):
        self.assertEqual(5, divide(5, 1))
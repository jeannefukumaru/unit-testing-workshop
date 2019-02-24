import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add_1_and_1_should_return_2(self):
        self.assertEquals(add(1, 1), 2)
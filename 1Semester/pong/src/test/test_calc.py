import unittest
from src import calc

class TestCase(unittest.TestCase):
    def test_add(self):
        result = calc.add(5,5)
        self.assertEqual(result, 10)

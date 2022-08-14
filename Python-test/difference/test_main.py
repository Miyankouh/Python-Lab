from unittest import TestCase, skipIf
from itertools import accumulate
from time import sleep
from operator import add
from sys import version_info
import main


class DifferenceTests(TestCase):
    def test_normal(self):
        iterable = (10, 20, 30, 40, 50)
        actual = list(main.difference(iterable))
        expected = [10, 10, 10, 10, 10]
        self.assertEqual(actual, expected)
    
    def test_custom(self):
        iterable = (10, 20, 30, 40, 50)
        actual = list(main.difference(iterable, add))
        expected = [10, 30, 50, 70, 90]
        self.assertEqual(actual, expected)

    def test_roundtrip(self):
        original = list(range(100))
        accumulated = accumulate(original)
        actual = list(main.difference(accumulated))
        self.assertEqual(actual, original)
    
    def test_one(self):
        self.assertEqual(list(main.difference([0])), [0])
    
    def test_empty(self):
        self.assertEqual(list(main.difference([])), [])
    
    @skipIf(version_info[:2] < (3, 8), 'accumulate with initial needs +3.8')
    def test_initial(self):
        original = list(range(100))
        accumulated = accumulate(original, initial=100)
        actual = list(main.difference(accumulated, initial=100))
        self.assertEqual(actual, original)

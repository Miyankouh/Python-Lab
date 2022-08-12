from itertools import cycle
from unittest import TestCase
import main


class RepeatEachTests(TestCase):
    def test_default(self):
        actual = list(main.repeat_each('ABC'))
        expected = ['A', 'A', 'B', 'B', 'C', 'C']
        self.assertEqual(actual, expected)
    
    def test_basic(self):
        actual = list(main.repeat_each('ABC', 3))
        expected = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = list(main.repeat_each(''))
        expected = []
        self.assertEqual(actual, expected)
    
    def test_no_repeat(self):
        actual = list(main.repeat_each('ABC', 0))
        expected = []
        self.assertEqual(actual, expected)
    
    def test_negative_repeat(self):
        actual = list(main.repeat_each('ABC', -1))
        expected = []
        self.assertEqual(actual, expected)
    
    def test_infinite_input(self):
        repeater = main.repeat_each(cycle('AB'))
        actual = main.take(repeater, 6)
        expected = ['A', 'A', 'B', 'B', 'A', 'A']
        self.assertEqual(actual, expected)

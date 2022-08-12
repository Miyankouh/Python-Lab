from itertools import count
from unittest import TestCase
import main


class InterleaveTests(TestCase):
    def test_even(self):
        actual = list(main.interleave([1, 4, 7], [2, 5, 8], [3, 6, 9]))
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expected)
    
    def test_short(self):
        actual = list(main.interleave([1, 4], [2, 5, 7], [3, 6, 8]))
        excepted = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, excepted)
    
    def test_mixed_types(self):
        it_list = ['a', 'b', 'c', 'd']
        it_str = '123456'
        it_inf = count()
        actual = list(main.interleave(it_list, it_str, it_inf))
        excepted = ['a', '1', 0, 'b', '2', 1, 'c', '3', 2, 'd', '4', 3]
        self.assertEqual(actual, excepted)

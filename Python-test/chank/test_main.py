"""  
command :  python3 -m unittest discover
"""

from unittest import TestCase
import main


class TakeTestes(TestCase):
    def test_simple_take(self):
        t = main.take(range(10), 5)
        self.assertEqual(t, [0, 1, 2, 3, 4])
    
    def test_null_take(self):
        t = main.take(range(10), 0)
        self.assertEqual(t, [])
    
    def test_negative_take(self):
        self.assertRaises(ValueError, lambda: main.take(-3, range(10)))

    def test_take_too_much(self):
        t = main.take(range(5), 10)
        self.assertEqual(t, [0, 1, 2, 3, 4])


class ChunkedTests(TestCase):
    def test_even(self):
        self.assertEqual(
            list(main.chunked('abcdef', 3)), [['a', 'b', 'c'], ['d', 'e', 'f']]
        )
    
    def test_odd(self):
        self.assertEqual(
            list(main.chunked('abcde', 3)), [['a', 'b', 'c'], ['d', 'e']]
        )

    def test_none(self):
        self.assertEqual(
            list(main.chunked('abcd', None)), [['a', 'b', 'c', 'd']]
        )

    def test_strict_false(self):
        self.assertEqual(
            list(main.chunked('abcde', 3, strict=False)), [['a', 'b', 'c'], ['d', 'e']]
        )

    def test_strict_true(self):
        def f():
            return list(main.chunked('abcde', 3, strict=True))
        
        self.assertRaisesRegex(ValueError, 'iterable is not division by n', f)
        self.assertEqual(
            list(main.chunked('abcdef', 3, strict=True)),
            [['a', 'b', 'c'], ['d', 'e', 'f']]
        )
    
    def test_strict_true_size_none(self):
        def f():
            return list(main.chunked('abcde', None, strict=True))
        
        self.assertRaisesRegex(
            ValueError, 'n cant be None when strict is True', f
        )

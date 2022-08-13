from unittest import TestCase
import main

class OnlyTests(TestCase):
    def test_default(self):
        self.assertEqual(main.only([]), None)
        self.assertEqual(main.only([1]), 1)
        self.assertRaises(ValueError , lambda : main.only([1, 2]))

    def test_custom_value(self):
        self.assertEqual(main.only([], default='!'), '!')
        self.assertEqual(main.only([1], default='!'), 1)
        self.assertRaises(ValueError, lambda : main.only([1, 2], default='!'))

    def test_custom_exception(self):
        self.assertEqual(main.only([], too_long=RuntimeError), None)
        self.assertEqual(main.only([1], too_long=RuntimeError), 1)
        self.assertRaises(RuntimeError, lambda : main.only([1, 2], too_long=RuntimeError))
    
    def test_default_exception_message(self):
        self.assertRaisesRegex(
            ValueError,
            "Expected exactly one item in iterable, but got foo, bar, and perhaps more.",
            lambda: main.only(['foo', 'bar', 'baz'])
        )

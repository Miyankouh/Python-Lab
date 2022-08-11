from unittest import TestCase
import one


class NthLastTest(TestCase):
    def test_basic(self):
        self.assertEqual(one.nth_or_last(range(3), 1), 1)
        self.assertEqual(one.nth_or_last(range(3), 3), 2) #[0, 1, 2] == 2

    def test_default_value(self):
        default = 42
        self.assertEqual(one.nth_or_last(range(0), 3, default), default)
    
    def test_empty_iterable_no_default(self):
        self.assertRaises(ValueError, lambda :  one.nth_or_last(range(0), 0))

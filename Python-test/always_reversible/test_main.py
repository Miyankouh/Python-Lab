from unittest import TestCase
import main


class AlwaysReversibleTests(TestCase):
    def test_regular_reversed(self):
        self.assertEqual(
            list(reversed(range(10))), list(main.always_reversible(range(10)))
        )
        self.assertEqual(
            list(reversed([1, 2, 3])), list(main.always_reversible([1, 2, 3]))
        )
        self.assertEqual(
            reversed([1, 2, 3]).__class__, main.always_reversible([1, 2, 3]).__class__
        )
    
    def test_nonseq_reversed(self):
        self.assertEqual(
            list(reversed(range(10))), list(main.always_reversible(x for x in range(10)))
        )
        self.assertEqual(
            list(reversed([1, 2, 3])), list(main.always_reversible(x for x in [1, 2, 3]))
        )
        self.assertNotEqual(
            reversed((1, 2)).__class__, main.always_reversible(x for x in (1, 2)).__class__
        )

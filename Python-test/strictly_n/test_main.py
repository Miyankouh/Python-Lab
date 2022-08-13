import logging
from unittest import TestCase
import main


class StrictlyNTests(TestCase):
    def test_basic(self):
        iterable = ['a', 'b', 'c' ,'d']
        n = 4
        actual = list(main.strictly_n(iterable, n))
        expected = iterable
        self.assertEqual(actual, expected)
    
    def test_too_short_default(self):
        iterable = ['a', 'b', 'c' ,'d']
        n = 5
        with self.assertRaises(ValueError) as exc:
            list(main.strictly_n(iterable, n))

        self.assertEqual('Too items in iterable (got 4)', exc.exception.args[0])
    
    def test_too_long_default(self):
        iterable = ['a', 'b', 'c' ,'d']
        n = 3
        with self.assertRaises(ValueError) as exc:
            list(main.strictly_n(iterable, n))

        self.assertEqual('Too many item in iterable (got at least 4)', exc.exception.args[0])

    def test_too_short_custom(self):
        call_count = 0
        def too_short(item_count):
            nonlocal call_count
            call_count += 1
            iterable = ['a', 'b', 'c' ,'d']
            n = 6
            actual = []

            for item in main.strictly_n(iterable, n, too_short=too_short):
                actual.append(item)
            expected = ['a', 'b', 'c' ,'d']
            self.assertEqual(actual, expected)
            self.assertEqual(call_count, 1)
        
    def test_too_login_custom(self):
        iterable = ['a', 'b', 'c' ,'d']
        n = 2
        too_long = lambda item_count: logging.warning(
            f'Picked the first {n} items'
        )

        with self.assertLogs(level='WARNING') as exc:
            actual = list(main.strictly_n(iterable, n, too_long=too_long))
        self.assertEqual(actual, ['a', 'b'])
        self.assertIn('Picked the first 2 items', exc.output[0])

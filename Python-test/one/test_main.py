from itertools import count
import traceback
from unittest import TestCase
import main


class OneTests(TestCase):
    def test_basic(self):
        it = ['item']
        self.assertEqual(main.one(it), 'item')
    
    def test_too_short(self):
        it = []
        for too_short, exc_type in [
            (None, ValueError),
            (IndexError, IndexError)
        ]:
            with self.subTest(too_short=too_short):
                try:
                    main.one(it, too_short=too_short)
                except exc_type:
                    formatted_exc = traceback.format_exc()
                    self.assertIn('StopIteration', formatted_exc)
                    self.assertIn('The above exception was the direct cause', formatted_exc)
                else:
                    self.fail()

    def test_too_long(self):
        it = count()
        self.assertRaises(ValueError, lambda: main.one(it))
        self.assertEqual(next(it), 2)
        self.assertRaises(
            OverflowError, lambda: main.one(it, too_long=OverflowError)
        )
    
    def test_too_long_default_message(self):
        it = count()
        self.assertRaisesRegex(
            ValueError,
            'Expected exactly one item in iterable, but got 0, 1, and perhaps more',
            lambda: main.one(it)
        )

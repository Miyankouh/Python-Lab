from unittest import TestCase
import traceback
import one


class FirstTests(TestCase):
    def test_many(self):
        self.assertEqual(one.first(x for x in range(4)), 0)
    
    def test_one(self):
        self.assertEqual(one.first([3]), 3)

    def test_default(self):
        self.assertEqual(one.first([], 'empty'), 'empty')

    def test_empty_stop_iteration(self):
        try:
            one.first([])
        except ValueError:
            formatted_exc = traceback.format_exc()
            self.assertIn('StopIteration', formatted_exc)
            self.assertIn('The above exception was the direct cause', formatted_exc)
        else:
            self.fail()

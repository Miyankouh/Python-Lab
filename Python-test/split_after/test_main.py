from unittest import TestCase
import main


class SplitAfterTests(TestCase):
    def test_start_with_sep(self):
        actual = list(main.spilt_after('xooxoo', lambda c: c == 'x'))
        expected = [['x'], ['o', 'o', 'x'], ['o', 'o']]
        self.assertEqual(actual, expected)
    
    def test_ends_with_sep(self):
        actual = list(main.spilt_after('ooxoox', lambda c: c == 'x'))
        expected = [['o', 'o', 'x'], ['o', 'o', 'x']]
        self.assertEqual(actual, expected)

    def test_no_sep(self):
        actual = list(main.spilt_after('ooo', lambda c: c == 'x'))
        expected = [['o', 'o', 'o']]
        self.assertEqual(actual, expected)

    def test_max_spile(self):
        for args, expected in [
            (
                ('a,b,c,d', lambda c: c ==',', -1),
                [['a', ','], ['b', ','], ['c', ','], ['d']]
            ),
            (
                ('a,b,c,d', lambda c: c ==',', 0),
                [['a', ',', 'b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda c: c ==',', 1),
                [['a', ','], ['b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda c: c ==',', 2),
                [['a', ','], ['b', ','], ['c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda c: c ==',', 10),
                [['a', ','], ['b', ','], ['c', ','], ['d']]
            ),
            (
                ('a,b,c,d', lambda c: c =='@', 2),
                [['a', ',', 'b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda c: c !=',', 2),
                [['a'], [',', 'b'], [',', 'c', ',', 'd']]
            )
        ]:
            actual = list(main.spilt_after(*args))
            self.assertEqual(actual, expected)

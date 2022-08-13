from unittest import TestCase
import main


class AlwaysIterableTests(TestCase):
    def test_single(self):
        self.assertEqual(list(main.always_iterable((1))), [1])
    
    def test_string(self):
        for obj in ['foo', b'bar', 'baz']:
            actual = list(main.always_iterable(obj))
            expected = [obj]
            self.assertEqual(actual, expected)
    
    def test_base_type(self):
        dict_obj = {'a':1, 'b':2}
        str_obj = '123'

        default_actual = list(main.always_iterable(dict_obj))
        default_expected = list(dict_obj)
        self.assertEqual(default_actual, default_expected)
        
        custom_actual = list(main.always_iterable(dict_obj, base_type=dict))
        custom_expected = [dict_obj]
        self.assertEqual(custom_actual, custom_expected)

        str_actual = list(main.always_iterable(str_obj, base_type=None))
        str_expected = list(str_obj)
        self.assertEqual(str_actual, str_expected)

        base_type = ((dict,),)
        custom_actual = list(main.always_iterable(dict_obj, base_type=base_type))
        custom_expected = [dict_obj]
        self.assertEqual

    def test_iterable(self):
        self.assertEqual(list(main.always_iterable([0, 1])), [0, 1])
        self.assertEqual(list(main.always_iterable([0, 1], base_type=list)), [[0, 1]])
        self.assertEqual(list(main.always_iterable(iter('foo'))), ['f', 'o', 'o'])
        self.assertEqual(list(main.always_iterable([])), [])
    
    def  test_none(self):
        self.assertEqual(list(main.always_iterable(None)), [])
    
    def test_generator(self):
        def _gen():
            yield 0
            yield 1
        self.assertEqual(list(main.always_iterable(_gen())), [0, 1])

from unittest import TestCase
import main


class SequenceViewTests(TestCase):
    def test_int(self):
        view = main.SequenceView((1, 2, 3))
        self.assertEqual(repr(view), "SequenceView((1, 2, 3))")
        self.assertRaises(TypeError, lambda: main.SequenceView({}))
    
    def test_update(self):
        seq = [1, 2, 3]
        view = main.SequenceView(seq)
        self.assertEqual(len(view), 3)
        self.assertEqual(repr(view), "SequenceView([1, 2, 3])")

        seq.pop()
        self.assertEqual(len(view), 2)
        self.assertEqual(repr(view), "SequenceView([1, 2])")
    
    def test_indexing(self):
        seq = ('a', 'b', 'c', 'd', 'e', 'f')
        view = main.SequenceView(seq)
        for i in range(-len(seq), len(seq)):
            self.assertEqual(view[i], seq[i])
    
    def test_abc_methods(self):
        seq = ('a', 'b', 'c', 'd', 'e', 'f', 'f')
        view = main.SequenceView(seq)

        self.assertIn('b', view)
        self.assertNotIn('g', view)
        self.assertEqual(list(iter(view)), list(seq))
        self.assertEquals((list(reversed(view))), list(reversed(seq))) 
        self.assertEqual(view.index('b'), 1)
        self.assertEqual(view.count('f'), 2)

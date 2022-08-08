""" 
cd work directory

start test:
    python3 -m unittest test_one.py
OR
    python3 -m unittest discover  -> It is used when the file must start with (testـ)

"""

import unittest
import one


class OneTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(4, 5), 9)
        self.assertEqual(one.add(-1, 4), 3)
    
    def test_subtract(self):
        self.assertEqual(one.subtract(5, 0), 5)

    def test_multiply(self):
        self.assertEqual(one.multiply(7, 0), 0)
    
    def test_division(self):
        self.assertEqual(one.division(30, 5), 6)
        self.assertRaises(ZeroDivisionError, one.division, 4, 0) # except

if __name__ == "__main__":
    unittest.main()

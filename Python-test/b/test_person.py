import unittest
from person import Person


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('majid', 'miyankouh')
        self.p2 = Person('nima', 'miyankouh')

    def tearDown(self):
        print('Done....')
    
    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'majid miyankouh')
        self.assertEqual(self.p2.fullname(), 'nima miyankouh')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'majidmiyankouh@email.com')
        self.assertEqual(self.p2.email(), 'nimamiyankouh@email.com')


if __name__ == '__main__':
    unittest.main()

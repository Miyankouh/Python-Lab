"""
step 1: create virtualenv & run virtualenv
step 2: pip install -r requirements.txt  OR  pip install pytest 
step 3: run command :  pytest  OR  pytest -v (file name)
"""

import pytest
import time
from one import Person


class TestPerson:
    @pytest.fixture
    def setup(self):
        self.p1 = Person('majid', 'miyankouh')
        self.p2 = Person('nima', 'miyankouh')
        yield 'setup'
        time.sleep(2)

    def test_fullname(self, setup):
        assert self.p1.fullname() == 'majid miyankouh'
        assert self.p2.fullname() == 'nima miyankouh'

    def test_email(self, setup):
        assert self.p1.email() == 'majidmiyankouh@email.com'
        assert self.p2.email() == 'nimamiyankouh@email.com'

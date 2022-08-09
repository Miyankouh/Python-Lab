"""  
step 1: create virtualenv & run virtualenv
step 2: pip install -r requirements.txt  OR  pip install nose 
step 3: run command :  nosetests  OR  nosetests -v (file name)
"""

import one


def test_add():
    assert one.add(3, 4) == 7
    assert one.add(5, 4) == 9
    assert one.add(-1, 4) == 3
    assert one.add(12, 4) == 16
    assert one.add(0, 8) == 8

def test_subtract():
    assert one.subtract(4, 5) == -1
    assert one.subtract(9, 5) == 4
    assert one.subtract(45, 10) == 35
    assert one.subtract(4, 15) == -11

def test_multiply():
    assert one.multiply(3, 4) != 11

def test_division():
    assert one.division(50, 5) == 10

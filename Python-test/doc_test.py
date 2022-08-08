"""
>>> add(5, 6)
11

>>> subtract(6, 9)
-3

>>> multiply(4 , 20)
80
"""



def add(x, y):
    """  
    >>> add(7, 6)
    13
    >>> add(2, 7)
    9
    >>> add(4, -1)
    3
    >>> add(0, 5)
    5
    """
    return x + y


def subtract(x, y):
    """
    >>> subtract(5, 4)
    1
    """
    return x - y


def multiply(x, y):
    """
    >>> multiply(5, 4)
    20
    >>> multiply(5, 8)
    40
    """
    return x * y



"""  
cd work directory/

start test:
    python3 -m doctest (file name) 
OR 
    python3 -m doctest -v (file name)    
"""
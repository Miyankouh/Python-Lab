from itertools import islice
from collections.abc import Sequence
from collections import deque


l = [99, 1, 2, 3, 4, 5, 6, 7]
e = []

_marker = object()

def one(iterable, too_short=None, too_long=None):
    it = iter(iterable)
    try:
        first_value = next(it)
    except StopIteration as e:
        raise(
            too_short or ValueError('too few items in iterable (expected 1)')
        ) from e

    try:
         second_value = next(it)
    except StopIteration:
        pass
    else:
        msg = (
            'Expected exactly one item in iterable, but got {!r}, {!r}, and perhaps more'              
            .format(first_value, second_value)
        )
        raise too_long or ValueError(msg)
    
    return first_value
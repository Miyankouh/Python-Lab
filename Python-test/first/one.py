from itertools import islice
from functools import partial


l = [99, 1, 2, 3, 4, 5, 6, 7]
e = []

_marker = object()

def first(iterable, default=_marker):
    try:
        return next(iter(iterable))
    except StopIteration as e:
        if default is _marker:
            raise ValueError(
                ' first() was called on an empty iterable,and no default value was provided'
            ) from e
        return default

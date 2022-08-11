from itertools import islice
from collections.abc import Sequence
from collections import deque


l = [99, 1, 2, 3, 4, 5, 6, 7]
e = []

_marker = object()


def last(iterable, default=_marker):
    try:
        if isinstance(iterable, Sequence):
            return iterable[-1]
        elif hasattr(iterable, '__reversed__'):
            return next(reversed(iterable))
        else:
            return deque(iterable, maxlen=1)[-1]
    except (IndexError, TypeError, StopIteration):
        if default is _marker:
            raise ValueError(
                'last() was called on an empty iterable, and no default was provided.'
            )
        return default


def nth_or_last(iterable, n, default=_marker):
    return last(islice(iterable, n+1),  default=default)


print(nth_or_last(l, 5))

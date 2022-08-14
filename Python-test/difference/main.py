from itertools import chain,tee, starmap
from operator import sub


def difference(iterable, func=sub, *, initial=None):
    a, b = tee(iterable)
    try:
        first = [next(b)]
    except StopIteration:
        return iter([])
    
    if initial is not None:
        first = []
    
    return chain(first, starmap(func, zip(b, a)))

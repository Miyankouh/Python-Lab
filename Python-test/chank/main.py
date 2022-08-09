from itertools import islice
from functools import partial


l = [1, 2, 3, 4, 5, 6]

def take(iterable, n):
    return list(islice(iterable, n))


def chunked(iterable, n, strict=False):
    iterator = iter(partial(take, iter(iterable), n), [])
    if strict:
        if n is None:
            raise ValueError('n cant be None when strict is True')
        def ret():
            for chunk in iterator:
                if len(chunk) != n:
                    raise ValueError('iterable is not division by n ')
                yield chunk
        return iter(ret())
    else:
        return iterator


print(list(chunked(l, 3, strict=True)))

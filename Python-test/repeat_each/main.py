from itertools import chain, islice, repeat


l = [1, 2, 3, 4, 5, 6, 7]

def take(iterable, n):
    return list(islice(iterable, n))

def repeat_each(iterable, n=2):
    return chain.from_iterable(map(repeat, iterable, repeat(n)))
    
from itertools import  chain


l = [0, 1, 2, 3, 4, 5, 6, 7]
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def interleave(*iterable):
    return chain.from_iterable(zip(*iterable))

print(list(interleave(l, s)))

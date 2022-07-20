"""  
    Exponential Time o(n^n)
"""

from itertools import chain, combinations

def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


if __name__ == "__main__":
    print(list(subsets(['a', 'b', 'c'])))
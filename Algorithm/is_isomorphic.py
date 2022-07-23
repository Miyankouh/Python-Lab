"""  
    is isomorphic
        foo, bar => False
        foo, bee => True

        {f:b, o:e, w:e} (b, e, e)
"""

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    dict = {}
    set_values = set()
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_values:
                return False
            dict[s[i]] = t[i]
            set_values.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False

    return True


if __name__ == '__main__':
    print(is_isomorphic('foo', 'bee'))
    print(is_isomorphic('foo', 'bar'))
    print(is_isomorphic('newman', 'python'))
    print(is_isomorphic('paper', 'title'))

s = ['a', 'b', 'c' ,'d']


def raise_(exception, *args):
    raise exception(*args)


def strictly_n(iterable, n, too_short=None, too_long=None):
    if too_short is None:
        too_short = lambda item_count: raise_(
            ValueError, 
            f'Too items in iterable (got {item_count})'
        )

    if too_long is None:
        too_long = lambda item_count: raise_(
            ValueError, 
            f'Too many item in iterable (got at least {item_count})'
        )
    
    it = iter(iterable)
    for i in range(n):
        try:
            item = next(it)
        except StopIteration:
            too_short(i)
            return
        else:
            yield item

    try:
        next(it)
    except StopIteration:
        pass
    else:
        too_long(n+1)

def only(iterable, default=None, too_long=None):
    it = iter(iterable)
    first_value = next(it, default)
    try:
        seconde_value = next(it)
    except StopIteration:
        pass
    else:
        msg = ('Expected exactly one item in iterable, but got {}, {}, and perhaps more.').format(
            first_value, seconde_value
        )
        raise too_long or ValueError(msg)
    return first_value

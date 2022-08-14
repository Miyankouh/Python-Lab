def split_after(iterable, pred, max_spilt=-1):
    if max_spilt == 0:
        yield list(iterable)
        return
    
    buf = []
    it = iter(iterable)
    for item in it:
        buf.append(item)
        if pred(item) and buf:
            yield buf
            if max_spilt == 1:
                yield list(it)
                return
            buf = []
            max_spilt -= 1
    if buf:
        yield buf

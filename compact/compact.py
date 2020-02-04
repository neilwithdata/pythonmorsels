def compact(seq):
    seq_iter = iter(seq)
    try:
        prev = next(seq_iter)
        yield prev
    except StopIteration:
        pass
    else:
        for item in seq_iter:
            if item != prev:
                yield item
            prev = item

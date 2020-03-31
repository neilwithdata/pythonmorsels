# return the last n elements from the iterable
def tail(iterable, n):
    if n <= 0:
        return list()

    it = iter(iterable)
    ret = []
    while True:
        try:
            ret.append(next(it))
            if len(ret) > n:
                del ret[0]
        except StopIteration:
            return ret


if __name__ == '__main__':
    print(tail([1, 2, 3], 2))
    print(tail('hello', 4))
    print(tail('hello', 0))
    print(tail('hello', -2))

    squares = (n ** 2 for n in range(10))
    print(tail(squares, 3))

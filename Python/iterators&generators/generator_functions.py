import math
from functools import lru_cache


class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            fact = math.factorial(self.i)
            self.i += 1
            return fact


def fact():
    i = 0

    def inner():
        nonlocal i
        f = math.factorial(i)
        i += 1
        return f
    return inner


@lru_cache()
def fib_recursive(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1

    for _ in range(n - 2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


class FibIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = fib_iterative(self.i)
        self.i += 1
        return result


class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Squares.squares_gen(self.n)

    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2


def get_squares():
    yield from (i ** 2 for i in range(10))


for item in get_squares():
    print(item)
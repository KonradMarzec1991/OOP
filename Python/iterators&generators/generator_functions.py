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
    fib_0, fib_1 = 1, 1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


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


fib_iter = FibIterator(10)
for i in fib_iter:
    print(i)

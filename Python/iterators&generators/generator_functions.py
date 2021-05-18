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

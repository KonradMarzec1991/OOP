import math


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


f5 = FactIter(5)
print(list(f5))
print(list(f5))
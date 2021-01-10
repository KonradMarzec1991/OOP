def cycle(n):
    counter = -1

    def inner():
        nonlocal counter
        if counter >= n:
            counter = -1
        counter += 1
        return counter
    return inner


class Cycle:
    def __init__(self, n):
        self.n = n
        self.counter = -1

    def __call__(self):
        if self.counter >= self.n:
            self.counter = -1
        self.counter += 1
        return self.counter

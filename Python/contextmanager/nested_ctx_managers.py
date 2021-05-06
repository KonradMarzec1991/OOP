from ctx_decorator import open_file


class NestedContextManager:
    def __init__(self, *contexts):
        self._enters = []
        self._exits = []
        self._values = []

        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values

    def __exit__(self, exc_type, exc_val, exc_tb):
        for ext in self._exits[::-1]:
            ext(exc_type, exc_val, exc_tb)
        return False


with NestedContextManager(
    open_file('file1.txt', 'r'),
    open_file('file2.txt', 'r')
) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

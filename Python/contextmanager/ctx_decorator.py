def open_file(f_name, mode='r'):
    print(f'openinig {f_name} file')
    f = open(f_name, mode)
    try:
        yield f
    finally:
        print(f'closing {f_name} file')
        f.close()


class GenContextManager:
    def __init__(self, gen):
        self._gen = gen

    def __enter__(self):
        print('calling next to perform yielded value from generator')
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling next to perform cleanup in generator')
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


file_gen = open_file('test.txt', 'r')
with GenContextManager(file_gen) as f:
    f.writelines('abcd')

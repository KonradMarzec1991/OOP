import csv

f_names = 'cars.csv', 'personal_info.csv'

for f_name in f_names:
    with open(f_name) as f:
        print(next(f), end='')
        print(next(f), end='')
    print('\n----------')


for i in (0, 1):
    with open(f_names[i]) as f:
        dialect = csv.Sniffer().sniff(f.read(1000))
        print(dialect.delimiter)


def get_dialect(f_name):
    with open(f_name) as f:
        return csv.Sniffer().sniff(f.read(1000))


class FileParser:
    def __init__(self, f_name):
        self.f_name = f_name

    def __enter__(self):
        self._f = open(self.f_name, 'r')
        self._reader = csv.reader(self.f_name, dialect=get_dialect(self.f_name))
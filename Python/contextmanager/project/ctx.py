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

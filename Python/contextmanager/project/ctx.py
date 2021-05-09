f_names = 'cars.csv', 'personal_info.csv'

for f_name in f_names:
    with open(f_name) as f:
        print(next(f), end='')
        print(next(f), end='')
    print('\n----------')
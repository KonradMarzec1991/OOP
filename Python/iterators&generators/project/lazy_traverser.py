from collections import namedtuple
import csv



def open_file(file_name: str):
    with open(file_name) as f:
        column_headers = next(f).strip('\n').split(',')
        sample_data = next(f).strip('\n').split(',')

        print(column_headers)
        print(sample_data)

        column_names = [
            header.replace(' ', '_').lower()
            for header in column_headers
        ]
        print(column_names)
        print(list(zip(column_names, sample_data)))

        Ticket = namedtuple('Ticket', column_names)


open_file('nyc_parking_tickets_extract.csv')
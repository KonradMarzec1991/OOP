from collections import namedtuple
import csv


DataRow = namedtuple('DataRow', [
    'summons_number',
    'plate_id',
    'registration_state',
    'plate_type',
    'issue_date',
    'violation_code',
    'vehicle_body_type',
    'vehicle_make',
    'violation_description',
])


def open_file(file_name: str):
    with open(file_name) as f:
        reader = csv.reader(f)
        print(next(reader))

        for row in reader:
            print(row)


open_file('nyc_parking_tickets_extract.csv')
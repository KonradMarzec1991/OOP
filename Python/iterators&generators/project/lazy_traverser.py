from collections import namedtuple
from functools import partial
from datetime import datetime


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


def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_str(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        return cleaned
    except ValueError:
        return default


column_parser = (
    parse_int,
    parse_str,
    partial(parse_str, default=''),
    partial(parse_str, default=''),
    parse_date,
    parse_int,
    partial(parse_str, default=''),
    parse_str,
    partial(parse_str, default='')
)
from collections import namedtuple, defaultdict
from functools import partial
from datetime import datetime


def parse_int(value, *, default=None):
    """
    Returns parsed integer or None
    """

    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    """
    Returns parsed date or None
    """

    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_str(value, *, default=None):
    """
    Returns parsed string or None
    """

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


def parse_row(row, column_names, default=None):
    """
    Returns namedtuple with applied parsers for its fields
    """

    Ticket = namedtuple('Ticket', column_names)

    fields = row.strip('\n').split(',')
    parsed_data = [func(field) for func, field in zip(column_parser, fields)]
    if all(bool(item) for item in parsed_data):
        return Ticket(*parsed_data)
    return default


def open_file(file_name: str):
    with open(file_name) as f:
        column_names = [
            header.replace(' ', '_').lower()
            for header in next(f).strip('\n').split(',')
        ]

        print(column_names)

        makes_count = defaultdict(int)
        for row in f:
            ticket = parse_row(row, column_names)
            if ticket:
                makes_count[ticket.vehicle_make] += 1

        makes_count = sorted(
            makes_count.items(),
            key=lambda t: -t[1]
        )
        print(makes_count)


open_file('nyc_parking_tickets_extract.csv')
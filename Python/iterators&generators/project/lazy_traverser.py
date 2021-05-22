from collections import namedtuple, defaultdict
from functools import partial
from datetime import datetime


FILE_NAME = 'nyc_parking_tickets_extract.csv'


def parse_int(value, *, default=None):
    """Returns parsed integer or None"""

    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    """Returns parsed date or None"""

    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_str(value, *, default=None):
    """Returns parsed string or None"""

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


def get_headers(file_name):
    """Returns list of headers for given file"""

    with open(file_name) as f:
        return [
            header.replace(' ', '_').lower()
            for header in next(f).strip('\n').split(',')
        ]


def parse_row(row, default=None):
    """Returns namedtuple with applied parsers for its fields"""

    Ticket = namedtuple('Ticket', get_headers(FILE_NAME))

    fields = row.strip('\n').split(',')
    parsed = [func(field) for func, field in zip(column_parser, fields)]
    if all(bool(item) for item in parsed):
        return Ticket(*parsed)
    return default


def read_file(file_name):
    """Iterates lazily given file"""

    with open(file_name) as f:
        next(f)
        yield from f


def parsed_data():
    for row in read_file(FILE_NAME):
        parsed = parse_row(row)
        if parsed:
            yield parsed


def violation_count():
    makes_count = defaultdict(int)
    for ticket in parsed_data():
        makes_count[ticket.vehicle_make] += 1
    return sorted(makes_count.items(), key=lambda t: -t[1])

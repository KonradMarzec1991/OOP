from html import escape
from decimal import Decimal


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i><{1}/i>)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(a):
    return html_escape(a).replace('\n', '<br>\n')


def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(
        html_escape(k), htmlize(v)) for k, v in d.items()
    )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    if isinstance(arg, (float, Decimal)):
        return html_real(arg)
    if isinstance(arg, str):
        return html_str(arg)
    if isinstance(arg, (list, tuple)):
        return html_list(arg)
    if isinstance(arg, dict):
        return html_dict(arg)
    return html_escape(arg)

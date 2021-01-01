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

    registry = {
        object: html_escape,
        int: html_int,
        float: html_real,
        Decimal: html_real,
        str: html_str,
        list: html_list,
        tuple: html_list,
        set: html_list,
        dict: html_dict,
    }

    fn = registry.get(type(arg), registry[object])
    return fn(arg)


print(htmlize({1, 2, 3}))
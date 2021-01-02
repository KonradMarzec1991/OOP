from html import escape


def html_escape(arg):
    return escape(str(arg))


def single_dispatch(fn):
    registry = {object: fn}

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorated.register = register
    decorated.dispatch = dispatch
    return decorated


@single_dispatch
def htmlize(arg):
    return escape(str(arg))


@htmlize.register(int)
def html_int(a):
    return '{0} (<i><{1}/i>)'.format(a, str(hex(a)))


@htmlize.register(float)
def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


@htmlize.register(str)
def html_str(a):
    return html_escape(a).replace('\n', '<br>\n')


@htmlize.register(list)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(dict)
def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(
        html_escape(k), htmlize(v)) for k, v in d.items()
    )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

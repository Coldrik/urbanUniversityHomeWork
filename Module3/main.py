def test():
    a = 'Voodoo'
    b = 'People'
    print(a, b)


def test2(a, b='имеет', *, c):
    print(a, b, c)


test()
test2('Читаемость', c='значение')

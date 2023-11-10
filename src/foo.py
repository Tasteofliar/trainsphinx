def greeting(name, age):
    '''
    greeting function, nice to meet you.

    :param str name: input your name.
    :param int age: input your age.

    :returns: greeting word.
    :rtype: str

    code example

    .. code-block:: python

        res = greeting(name='foo', age=20)
        print(res)

    +------------------------+------------+----------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 | helllllo |
    | (header rows optional) |            |          |          |          |
    +========================+============+==========+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 | aa       |
    +------------------------+------------+----------+----------+----------+
    | body row 2             | ...        | ...      |          |          |
    +------------------------+------------+----------+----------+----------+
    '''
    result = 'Hello, {} {} years old.'.format(name, age)

    return result
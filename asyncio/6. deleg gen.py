from inspect import getgeneratorstate


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def subgen():

    while True:

        try:

            message = yield
        except StopIteration:
            print('exx')
            break
        else:
            print('.......', message)

    return 'returned from subgen()'

@coroutine
def delegator(g):

    # while True:
    #
    #     try:
    #         data = yield
    #         g.send(data)
    #     except StopIteration:
    #         pass
    result = yield from g
    print(result)


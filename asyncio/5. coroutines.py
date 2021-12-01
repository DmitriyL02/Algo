from inspect import getgeneratorstate


def coroutine(func):

    def inner(*args, **kwargs):

        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


@coroutine
def subgen():
    x = 'Ready to acccept message'
    message = yield x
    print('Subgen received: ', message)


@coroutine
def average():
    count = 0
    summ = 0

    average = None

    while True:

        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)



g = average()
print(g.send(5))
g.throw(StopIteration)
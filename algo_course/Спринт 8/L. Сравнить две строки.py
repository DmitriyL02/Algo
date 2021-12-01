def f(a):
    return ''.join(filter(lambda x: ord(x) % 2 == 0, list(a)))


def equals_strings(a, b):

    even_a = f(a)
    even_b = f(b)

    if even_a > even_b:
        return 1
    elif even_a == even_b:
        return 0
    return -1


if __name__ == '__main__':

    print(equals_strings(input(), input()))

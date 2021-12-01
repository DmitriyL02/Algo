def remote_work():

    number = int(input())
    elements = []

    while number:

        if number % 2 != 0:
            elements.append(1)
        else:
            elements.append(0)

        number = number // 2

    return reversed(elements)


if __name__ == '__main__':

    print(*remote_work(), sep='')

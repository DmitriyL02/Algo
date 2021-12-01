def is_four_positive():

    number = int(input())
    counter = 4

    if number == 1:
        return True

    while counter <= number:

        if counter == number:
            return True
        counter = counter * 4

    return False


if __name__ == '__main__':
    print(is_four_positive())

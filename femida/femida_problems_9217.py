def is_palindrome(number):

    if number < 0:
        return False

    numbers = []

    while number > 0:

        numbers.append(number % 10)
        number = number // 10

    return numbers == numbers[::-1]


if __name__ == '__main__':

    print(is_palindrome(12344321))

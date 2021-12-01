def factorial(n):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def partical(n, k):

    number = factorial(n)
    if number < 10**k:
        return number

    return str(number)[-k:]


if __name__ == '__main__':

    n, k = input().split()
    answer = partical(int(n), int(k))

    if isinstance(answer, list):
        print(*answer, sep='')
    else:
        print(answer)

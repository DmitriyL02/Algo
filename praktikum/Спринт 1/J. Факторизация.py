def factorization(n):

    i = 2
    numbers = []
    while i * i <= n:
        while n % i == 0:
            numbers.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        numbers.append(n)
    return numbers


if __name__ == '__main__':

    print(*factorization(int(input())))

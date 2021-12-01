def fib(n):

    cur = 1
    if n > 2:
        cur = fib(n - 1) + fib(n - 2)
    return cur


if __name__ == '__main__':

    print(fib(int(input()) + 1))

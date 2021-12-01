def is_even(value):
    return value % 2 == 0


def main():
    x, y, z = list(map(lambda val: is_even(int(val)), input().split()))
    return 'WIN' if x == y == z else 'FAIL'


if __name__ == '__main__':

    print(main())

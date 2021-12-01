def main():

    a, x, b, c = list(map(int, input().split()))

    return a * (x*x) + b * x + c


if __name__ == '__main__':

    print(main())
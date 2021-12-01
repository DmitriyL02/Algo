def krujki():

    memo = set()

    for i in range(int(input())):

        krujek_type = input()

        if krujek_type not in memo:
            print(krujek_type)
            memo.add(krujek_type)


if __name__ == '__main__':

    krujki()
# Лацис Дмитрий Сергеевич
# Задача: B. Ловкость рук
# ID: 52279165
# URL: https://contest.yandex.ru/contest/23390/run-report/52279165/


def hands_magic(k, key_numbers):

    key_counter = {}
    points = 0

    for num in key_numbers:
        if num.isdigit():
            if num not in key_counter:
                key_counter[num] = 0
            key_counter[num] += 1

    for num in key_counter:
        if key_counter[num] <= k + k:
            points += 1
    return points


if __name__ == '__main__':

    k = int(input())
    key_numbers = []

    for _ in range(4):
        key_numbers += list(input())

    print(hands_magic(k, key_numbers))

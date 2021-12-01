# Лацис Дмитрий Сергеевич
# Задача: A. Ближайший ноль
# ID: 52279160
# URL: https://contest.yandex.ru/contest/23390/run-report/52279160/


def neighbour_zero(neighbours_counter, neighbours):

    left_pos = None
    right_pos = None
    output = [None] * neighbours_counter

    for idx in range(len(neighbours)):

        if neighbours[idx] == 0:
            left_pos = idx
            output[idx] = 0
        elif left_pos is not None:
            output[idx] = idx - left_pos

    for idx in range(len(output) - 1, -1, -1):
        if output[idx] == 0:
            right_pos = idx
        elif right_pos is not None:
            if output[idx] is None or output[idx] > right_pos - idx:
                output[idx] = right_pos - idx

    return output


if __name__ == '__main__':

    neighbours_counter = int(input())
    neighbours = list(map(int, input().split()))
    print(*neighbour_zero(neighbours_counter, neighbours))

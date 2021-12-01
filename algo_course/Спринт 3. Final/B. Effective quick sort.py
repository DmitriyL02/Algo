# Лацис Дмитрий Сергеевич
# Задача: B. Эффективная быстрая сортировка
# ID: 53582188
# URL: https://contest.yandex.ru/contest/24735/run-report/53582188/

from collections import namedtuple
from typing import List


def quicksort(arr: List, low: int, high: int) -> None:

    if low < high:
        rank = partition(arr, low, high)
        quicksort(arr, rank+1, high)
        quicksort(arr, low, rank-1)


def partition(arr: any, lower: int, higher: int) -> int:

    i = lower - 1
    pivot = higher
    for j in range(lower, higher):
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[higher] = arr[higher], arr[i+1]
    return i + 1


if __name__ == '__main__':

    interns_count = int(input())
    intern_mask = namedtuple('intern', ['solved_tasks', 'penalty', 'login'])
    interns = [None] * interns_count

    for idx in range(interns_count):

        login, solved_tasks, penalty = input().split()

        interns[idx] = intern_mask(
            login=login, solved_tasks=-int(solved_tasks), penalty=int(penalty))

    quicksort(interns, 0, interns_count - 1)

    for intern in interns:
        print(intern.login)

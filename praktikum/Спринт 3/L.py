def binary_search(array, target, left, right, memo=-1):

    if right <= left:
        return memo

    middle = (left + right) // 2

    if array[middle] >= target:
        memo = middle + 1
        return binary_search(array, target, left, middle, memo)

    return binary_search(array, target, middle + 1, right, memo)


def binary_search_2(array, target, left, right, memo=-1):

    if right <= left:
        return memo

    middle = (left + right) // 2

    if array[middle] >= target + target:
        memo = middle + 1
        return binary_search_2(array, target, left, middle, memo)

    return binary_search_2(array, target, middle + 1, right, memo)


if __name__ == '__main__':

    days = int(input())
    cost_per_day = list(map(int, input().split()))
    bike_cost = int(input())

    first_lower = binary_search(cost_per_day, bike_cost, 0, len(cost_per_day))
    second_higher = binary_search_2(cost_per_day, bike_cost, 0, len(cost_per_day))
    print(first_lower, second_higher)

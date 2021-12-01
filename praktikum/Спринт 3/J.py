def bubble_sort(array, length):

    if length == 1:
        print(*array)
        return

    last_is_change_status = None

    for i in range(length - 1):
        is_change = False
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                last_is_change_status, is_change = is_change, True

        if last_is_change_status is None and not is_change:
            print(*array)

        if not is_change:
            return

        print(*array)


if __name__ == '__main__':

    length = int(input())
    numbers = list(map(int, input().split()))

    bubble_sort(numbers, length)

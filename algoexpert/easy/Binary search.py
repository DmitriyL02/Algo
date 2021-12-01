def binarySearch(array, target):
    # Write your code here.
    length = len(array)

    left = 0
    right = length - 1

    while left <= right:

        middle = (left + right) // 2

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

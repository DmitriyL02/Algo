def isMonotonic(array):
    # Write your code here.
    length = len(array)

    if not array or length < 2:
        return True

    is_positive = array[0] < array[-1]

    for i in range(1, length):

        if is_positive:
            if array[i - 1] > array[i]:
                return False
        else:
            if array[i - 1] < array[i]:
                return False

    return True


print(isMonotonic([1, 1, 1, 1, 0, 1]))
def insertionSort(array):
    # Write your code here.
    length = len(array)

    for i in range(1, length):
        while i > 0 and array[i - 1] > array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1

    return array

print(insertionSort([4, 3, 2, 1, 5, 6]))
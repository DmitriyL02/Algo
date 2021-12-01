def bubbleSort(array):
    # Write your code here.

    length = len(array)

    for i in range(length):
        for j in range(i + 1, length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array

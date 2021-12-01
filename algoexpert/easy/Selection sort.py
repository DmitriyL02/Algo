def selectionSort(array):
    # Write your code here.
    for i in range(len(array)-1):
        for k in range(i+1, len(array)):
            if array[k] < array[i]:
                array[k], array[i] = array[i], array[k]

    return array

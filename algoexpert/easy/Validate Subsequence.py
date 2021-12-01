def isValidSubsequence(array, sequence):

    i = 0
    j = 0
    seq_length = len(sequence)
    arr_length = len(array)

    while j < seq_length and i < arr_length:

        if array[i] == sequence[j]:
            j += 1
        i += 1

    if j == seq_length:
        return True

    return False

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 0]))

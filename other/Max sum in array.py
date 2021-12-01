def max_sum_subarray(arr, k):

    max_sum = float('-inf')
    start = 0
    current_sum = 0

    for end, val in enumerate(arr):
        current_sum += val
        if end - start + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[start]
            start += 1

    return max_sum


print(max_sum_subarray([1, 1, 2, 2, 3, 3, 10, 0, 0, 11, 11, 11], 3))

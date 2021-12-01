def rob(arr):

    if not arr:
        return 0

    prev, cur = 0, arr[0]

    for i in range(1, len(arr)):

        tmp = max(prev + arr[i], cur)

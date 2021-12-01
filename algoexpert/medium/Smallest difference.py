def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    i = 0
    j = 0

    min_diff = float('inf')
    current = float('inf')
    min_values = None

    while i < len(arrayOne) and j < len(arrayTwo):

        x, y = arrayOne[i], arrayTwo[j]

        if x < y:
            current = y - x
            i += 1
        elif x > y:
            current = x - y
            j += 1
        else:
            return [x, y]

        if current < min_diff:
            min_diff = current
            min_values = [x, y]

    return min_values

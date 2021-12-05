import operator


def mergeOverlappingIntervals(intervals):

    intervals.sort(key=operator.itemgetter(0))

    output = [intervals[0]]

    for i in range(1, len(intervals)):

        curr_interval = intervals[i]
        prev_interval = output[-1]

        if curr_interval[0] <= prev_interval[1]:
            if curr_interval[1] > prev_interval[1]:
                prev_interval[1] = curr_interval[1]
        else:
            output.append(curr_interval)

    return output


# tests
intervals = [
    [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]],
    [[0, 0]],
    [[0, 10], [10, 11]],
    [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]],
    [[1, 1], [1, 1], [1, 1]],
    [[1, 22], [-20, 30]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]],
    []
]




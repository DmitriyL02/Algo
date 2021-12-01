def nonConstructibleChange(coins):

    change = 0
    coins.sort()

    for idx in range(len(coins)):

        if coins[idx] > change + 1:
            return change + 1

        change += coins[idx]

    return change + 1


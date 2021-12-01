def numTrees(n: int) -> int:
    c = 1

    for i in range(n):

        c = c * 2 * (2 * i + 1) // (i + 2)

    return c


if __name__ == '__main__':

    numTrees(int(input()))

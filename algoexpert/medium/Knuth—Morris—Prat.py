def knuthMorrisPrattAlgorithm(string, substring):
    # Write your code here.
    m = len(substring)
    p = [0] * m

    n = len(string)

    i = 1
    j = 0

    while i < m:

        if substring[i] != substring[j]:

            if j > 0:
                p[i] = 0
            else:
                j = p[j - 1]

        if substring[i] == substring[j]:
            p[i] = j + 1
            j += 1

        i += 1

    i = 0
    j = 0

    while i < n:

        if string[i] == substring[j]:

            i += 1
            j += 1

            if j == m:
                return True
        else:

            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    return False



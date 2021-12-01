def prefix_function(s):

    length = len(s)
    prefix_arr = [0] * len(s)

    for i in range(1, length):

        k = prefix_arr[i - 1]

        while k > 0 and s[k] != s[i]:
            k = prefix_arr[k - 1]

        if s[k] == s[i]:
            k += 1

        prefix_arr[i] = k

    return prefix_arr


if __name__ == '__main__':

    print(*prefix_function(input()), sep=' ')

def binary_subsequence_search(s, t):
    j = 0
    for i in range(len(t)):
        if j >= len(s):
            return True
        if s[j] == t[i]:
            j += 1
            if j == len(s):
                return True
    return False


if __name__ == '__main__':

    print(binary_subsequence_search(input(), input()))

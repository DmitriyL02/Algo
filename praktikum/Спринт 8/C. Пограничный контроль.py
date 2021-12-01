def is_valid_string(s1, s2):

    max_length = len(s1)
    min_length = len(s2)

    if max_length < min_length:
        s1, s2 = s2, s1
        max_length, min_length = min_length, max_length

    if max_length - min_length > 1:
        return 'FAIL'
    elif max_length == 0 and min_length == 0:
        return 'OK'

    i = 0
    j = 0
    mistakes_count = 0
    while j < min_length:

        if s1[i] != s2[j]:

            mistakes_count += 1

            if mistakes_count > 1:
                return 'FAIL'

            if (i + 1 < max_length and s1[i + 1] == s2[j]) and not (i + 1 < max_length and j + 1 < min_length and s1[i + 1] == s2[j + 1]):
                j -= 1

        i += 1
        j += 1

    return 'OK'


if __name__ == '__main__':

    print(is_valid_string(input(), input()))

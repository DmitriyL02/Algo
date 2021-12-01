def longest_word():

    length = int(input())
    words = input().split()

    if not words:
        return

    max_word = []

    for word in words:

        if not max_word:
            max_word.append((word, len(word)))
        else:
            if len(word) > max_word[-1][1]:
                max_word.append((word, len(word)))
            if length - max_word[-1][1] <= 0:
                return max_word[-1]

    return max_word[-1]


if __name__ == '__main__':

    print(*longest_word(), sep='\n')

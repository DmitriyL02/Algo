"""
Дана строка, состоящая из букв A-Z:
"AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
Нужно написать функцию RLE, которая на выходе даст строку вида:
"A4B3C2XYZD4E3F3A6B28"
И сгенерирует любую ошибку, если на вход пришла невалидная строка.

Пояснения:
1. Если символ встречается 1 раз, он остается без изменений
2. Если символ повторяется более 1 раза, к нему добавляется количество повторений
"""


def rle(letters):

    length = len(letters)
    output = []
    i = 0
    j = 1

    while i < length:

        letter = letters[i]

        if not letter.isalpha():
            raise ValueError(f'{letter} is not alphabet symbol')

        while (i + j < length) and letters[i + j] == letter:
            j += 1

        if j > 1:
            letter += str(j)

        i += j
        j = 1

        output.append(letter)

    return output


if __name__ == '__main__':

    letters = input()
    print(*rle(letters), sep='')

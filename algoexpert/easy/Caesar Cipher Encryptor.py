def caesarCipherEncryptor(string, key):

    words = [None] * len(string)

    for idx, letter in enumerate(string):
        tmp = (ord(letter) + (key % 26)) % 122

        if tmp == 0:
            tmp = 122

        elif tmp < 97:
            tmp = tmp + 96

        words[idx] = chr(tmp)

    return ''.join(words)

print(caesarCipherEncryptor('abc', 0))
def is_palindrome():

    sentence = [letter.lower() for letter in input()
                if letter.isdigit() or letter.isalpha()]
    return sentence == sentence[::-1]


if __name__ == '__main__':

    print(is_palindrome())

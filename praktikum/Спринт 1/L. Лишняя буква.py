def main():

    word_1 = list(input())
    word_2 = list(input())

    base_solver = dict()

    for letter in word_1:
        if letter not in base_solver:
            base_solver[letter] = 0
        base_solver[letter] += 1

    for letter in word_2:

        if letter not in base_solver or base_solver[letter] == 0:
            return letter
        base_solver[letter] -= 1

    return


if __name__ == '__main__':

    print(main())
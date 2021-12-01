def firstNonRepeatingCharacter(string):
    # Write your code here.

    solver = {}

    for letter in string:

        if letter not in solver:
            solver[letter] = 0
        solver[letter] += 1

    for idx, letter in enumerate(string):

        if solver[letter] == 1:
            return idx

    return -1


print(firstNonRepeatingCharacter('aaabcd'))

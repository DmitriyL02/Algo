class Solution:

    NUMBERS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    MATH_SYMBOLS = {'-', '+'}

    MAX_INT = (2 ** 31) - 1
    MIN_INT = -(2 ** 31)

    def myAtoi(self, s: str) -> int:

        if not s:
            return 0

        symbols = list(s)
        total = 0
        pos = 0
        length = len(symbols)

        for idx in range(length):

            if (symbols[idx] in self.NUMBERS or
                    (symbols[idx] in self.MATH_SYMBOLS and pos < 1)):
                symbols[pos], symbols[idx] = symbols[idx], symbols[pos]
                pos += 1
            elif symbols[idx] == ' ' and pos < 1:
                continue
            else:
                break

        res = 0

        if symbols[0] not in self.NUMBERS:
            res = 1

        while res < pos:
            total = (total * 10) + self.NUMBERS[symbols[res]]
            res += 1

        if symbols[0] == '-':
            total = -total
        if total > self.MAX_INT:
            return self.MAX_INT
        elif total < self.MIN_INT:
            return self.MIN_INT

        return total

print(Solution().myAtoi("   +0 123"))
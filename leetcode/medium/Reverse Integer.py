class Solution:

    def reverse(self, x: int) -> int:

        total = 0
        is_positive = x > 0
        x = abs(x)

        MIN_INT = -2**31
        BIG_INT = (2**31)-1

        while x > 0:

            num_pop = x % 10
            x //= 10

            total = total * 10 + num_pop

            if not MIN_INT <= total <= BIG_INT:
                return 0

        return total if is_positive else -total





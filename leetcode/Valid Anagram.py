class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        solver = {}

        if not(s and t):
            return True
        elif not s or not t:
            return False

        for letter in s:
            if letter not in solver:
                solver[letter] = 0
            solver[letter] += 1

        for letter in t:

            if letter not in solver or solver[letter] == 0:
                return False
            solver[letter] -= 1

        for key in solver:

            if solver[key] > 0:
                return False

        return True


print(Solution().isAnagram('ab', 'b'))
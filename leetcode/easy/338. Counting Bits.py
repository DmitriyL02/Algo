from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bites = [0] * (n + 1)

        for i in range(1, n+1):
            bites[i] = bites[i >> 1] + i % 2

        return bites[:n+1]
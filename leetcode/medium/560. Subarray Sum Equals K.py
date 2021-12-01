from typing import Optional, List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> any:

        numbers = dict()

        for num in nums:

            sub_sum = k - num
            if sub_sum in numbers:
                numbers.pop()

obj = Solution()

print(obj.subarraySum([1, 2, 3], 3))
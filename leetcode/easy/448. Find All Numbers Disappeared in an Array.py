from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums.sort()

        nums_2 = set(range(1, len(nums) + 1))

        return list(set(nums) ^ nums_2)



a = Solution()

print(a.findDisappearedNumbers([1,1]))

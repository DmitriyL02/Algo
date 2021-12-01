from typing import Optional, List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return []

        nums.sort()
        output = []

        for idx, num in enumerate(nums):
            if num == target:
                output.append(idx)

        return output

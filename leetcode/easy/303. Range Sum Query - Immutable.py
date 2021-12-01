from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        sums = []

        current_sum = 0
        for num in nums:
            current_sum += num
            sums.append(current_sum)

        self.sums = sums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]

# # Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])



#
# param_1 = obj.sumRange(2, 5)
# print(param_1)

print(obj.sums)
print(obj.sumRange(2, 5))
class Solution:
    def removeDuplicates(self, nums) -> int:

        if not nums:
            return 0

        length = len(nums)
        template_mark = '_'
        prev_value = nums[0]

        for i in range(1, length):

            if nums[i] == prev_value:
                nums[i] = template_mark
            else:
                prev_value = nums[i]

        pos = 0

        for i in range(length):

            if nums[i] != template_mark:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        for _ in range(pos, length):
            nums.pop()

        return len(nums)

print(Solution().removeDuplicates([1, 1, 2, 2, 3, 3]))
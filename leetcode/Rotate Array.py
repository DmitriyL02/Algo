from typing import List

'''
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

[1,2,3,4,5,6,7]


'''

def rotate(nums: List[int], k: int) -> None:

    length = len(nums)

    for idx, num in range(1, length):

        # k = k %
        pass


rotate([1,2,3,4,5,6,7], 3)
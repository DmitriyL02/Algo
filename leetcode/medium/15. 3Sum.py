from typing import List


class Solution:

    def threeSum(self, array: List[int]) -> List[List[int]]:

        length = len(array)

        if length < 2:
            return []

        res = []
        array.sort()

        for i in range(length - 1):

            left = i + 1
            right = len(array) - 1

            while left < right:

                total = array[i] + array[left] + array[right]

                if total == 0:
                    if [array[i], array[left], array[right]] not in res:
                        res.append([array[i], array[left], array[right]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

        return res

# Лацис Дмитрий Сергеевич
# Задача: A. Поиск в сломанном массиве
# ID: 53629055
# URL: https://contest.yandex.ru/contest/24735/run-report/53629055/

from typing import List


def broken_search(nums: List[int], target: int,
                  left: int = 0, right: int = 0) -> int:

    right = right or len(nums) - 1
    mid = (right + left) // 2

    left_num = nums[left]
    right_num = nums[right]

    if left_num == target:
        return left

    if nums[mid] == target:
        return mid

    if right_num == target:
        return right

    if left_num < nums[mid]:
        if left_num <= target <= nums[mid]:
            return broken_search(nums, target, left, mid)

        return broken_search(nums, target, mid, right)

    elif left_num > nums[mid]:
        if left_num > target <= right_num and target > nums[mid]:
            return broken_search(nums, target, mid, right)

        return broken_search(nums, target, left, mid)

    return -1

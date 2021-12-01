# https://femida.yandex-team.ru/problems/921


def moveZeros(nums):

    pos = 0

    for i in range(len(nums)):

        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

    while nums and nums[-1] == 0:
        nums.pop()

    return nums

print(moveZeros([1, 0, 1 ,1, 0]))

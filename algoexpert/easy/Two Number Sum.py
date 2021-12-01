def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return len([potentialMatch, num])
        nums[num] = None
    return []


print(twoNumberSum([1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3], 2))
button_letters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combination(nums, m: int = -1, prefix=None, keys=None):

    keys = keys or []
    prefix = prefix or []

    m = len(nums) if m == -1 else m

    if m == 0:
        print(*prefix, end=" ", sep="")
        return

    if not keys:
        for number in nums:
            keys.append(button_letters[number])

    for symbol in keys[0]:

        prefix.append(symbol)
        combination(nums[1::], m-1, prefix, keys[1::])
        prefix.pop()


if __name__ == '__main__':

    combination(list(input()))

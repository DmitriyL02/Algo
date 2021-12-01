def remove_zeroes(numbers):

    pos = 0

    # O(n) - один проход по всей последовательности
    for idx in range(len(numbers)):

        if numbers[idx] != 0:
            # O(1) - get and set item
            numbers[pos], numbers[idx] = numbers[idx], numbers[pos]
            pos += 1

    # O(n) в худшем случае
    while numbers and numbers[-1] == 0:

        # O(1) - pop last item
        numbers.pop()

    return numbers


if __name__ == '__main__':

    numbers = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]

    print(*remove_zeroes(numbers), sep=' ')

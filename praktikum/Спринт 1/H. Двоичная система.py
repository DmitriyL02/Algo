ADD_RULES = {
    (1, 0): 1,
    (0, 1): 1,
    (0, 0): 0,
    (1, 1): 10
}


def main():

    first_num = list(input())
    second_num = list(input())

    if len(second_num) > len(first_num):
        first_num, second_num = second_num, first_num

    memory = 0
    output = []

    while first_num:

        slug_1 = int(first_num.pop())

        if second_num:
            slug_2 = int(second_num.pop())
        else:
            slug_2 = memory
            memory = 0

        summary = ADD_RULES[(slug_1, slug_2)] + memory
        memory = 0

        if (first_num and summary <= 1) or not first_num:
            output.append(str(summary))
        else:
            memory = 1
            if summary > 10:
                output.append('1')
            else:
                output.append('0')

    return output[::-1]


if __name__ == '__main__':

    print(*main(), sep='')

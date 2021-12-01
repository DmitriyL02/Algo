def concat_string(base_string, letters):

    letters.sort(key=lambda x: x[1])

    modify_string = []
    last_used_index = 0

    for item in letters:

        if item[1] == 0:
            modify_string.append(item[0])
        else:
            modify_string.append(
                base_string[last_used_index:item[1]] + item[0]
            )
            last_used_index = item[1]

    if last_used_index < len(base_string):
        modify_string.append(base_string[last_used_index:])

    return modify_string


if __name__ == '__main__':

    main_string = input()
    length = int(input())

    add_strings = [None] * length

    for idx in range(length):

        word, index = input().split()
        add_strings[idx] = (word, int(index))

    print(*concat_string(main_string, add_strings), sep='')

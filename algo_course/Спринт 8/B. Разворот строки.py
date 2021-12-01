def flip_string(string):

    memory = string.split()
    start = 0
    end = len(memory) - 1

    while start < end:

        memory[start], memory[end] = memory[end], memory[start]
        start += 1
        end -= 1

    return memory


if __name__ == '__main__':

    print(*flip_string(input()), sep=' ')

def to_number(value):
    return tuple(map(int, value.split()))


def main():

    row = int(input())
    col = int(input())

    output = []
    matrix = []

    for _ in range(row):
        matrix.append(to_number(input()))

    y = int(input())
    x = int(input())

    element_pos = matrix[y][x]

    if y + 1 < row:
        output.append(matrix[y + 1][x])
    if y - 1 >= 0:
        output.append(matrix[y - 1][x])
    if x + 1 < col:
        output.append(matrix[y][x + 1])
    if x - 1 >= 0:
        output.append(matrix[y][x - 1])

    return sorted(output)


if __name__ == '__main__':

    print(*main())

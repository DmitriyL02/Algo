def conference(arr, k):

    table = {}
    for id in arr:
        if id in table:
            table[id] += 1
        else:
            table[id] = 1
    table = list(table.items())

    table.sort(key=lambda x: -int(x[1]))

    ans = []
    for i in range(0, k):
        ans.append(table[i][0])

    return ans


if __name__ == "__main__":

    input()
    arr = input().split()
    k = int(input())

    print(*conference(arr, k), sep=' ')

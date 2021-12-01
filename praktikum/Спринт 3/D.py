def pleasuring(childs, cookies):
    pleasure = 0
    i = 0
    for j in range(len(cookies)):
        if i >= len(childs):
            break
        if childs[i] == cookies[j] or childs[i] < cookies[j]:
            i += 1
            pleasure += 1

    return pleasure


if __name__ == '__main__':

    input()
    childs = sorted(list(map(int, input().split())))
    input()
    cookies = sorted(list(map(int, input().split())))

    print(pleasuring(childs, cookies))

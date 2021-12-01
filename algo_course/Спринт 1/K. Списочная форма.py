def main():
    _ = input()
    return list(str(int(''.join(input().split())) + int(input())))


if __name__ == '__main__':

    print(*main())

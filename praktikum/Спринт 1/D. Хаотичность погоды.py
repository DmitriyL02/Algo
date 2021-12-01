def weather_counter():

    days_total = int(input())

    if not days_total:
        return 0
    elif days_total == 1:
        return 1

    counter = 0
    days = list(map(int, input().split()))

    for idx in range(days_total):

        if idx < days_total - 1:

            if idx == 0 and days[idx] > days[idx + 1]:
                counter += 1
            elif days[idx] > days[idx - 1] and days[idx] > days[idx + 1]:
                counter += 1

        elif idx == days_total - 1 and days[idx - 1] < days[idx]:
            counter += 1

    return counter


if __name__ == '__main__':

    print(weather_counter())

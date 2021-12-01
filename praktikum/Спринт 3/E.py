def home_buy(issues, budget):
    homes_own = 0
    for i in range(len(issues)):
        if budget >= issues[i]:
            budget = budget - issues[i]
            homes_own += 1
    return homes_own


if __name__ == '__main__':

    budget = list(map(int, input().split()))[1]
    issues = sorted(list(map(int, input().split())))

    print(home_buy(issues, budget))

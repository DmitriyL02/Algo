# https://femida.yandex-team.ru/problems/4154

# size_t maxOnes(const std::vector<int>& v);
#
# assert(maxOnes({0, 0}) == 0);
# assert(maxOnes({1, 0}) == 1);
# assert(maxOnes({0, 1}) == 1);
# assert(maxOnes({1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1}) == 5);
# assert(maxOnes({1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1}) == 6);


def max_ones(v):

    if not v:
        return 0

    length = len(v)
    current_max = 0
    ones = 0
    sub_ones = 0

    for i in range(length):

        if v[i] == 1:
            ones += 1
        elif i + 1 < length and v[i] == 0 and v[i + 1] == 1:
            if sub_ones > 0:
                current_max = max(ones, current_max)
                ones = i - (sub_ones + 1)
            sub_ones = i
        else:
            if ones > current_max:
                current_max = ones
            ones = 0
            sub_ones = 0

    return max(ones, current_max)


def test():
    assert max_ones([0, 0]) == 0
    assert max_ones([1, 0]) == 1
    assert max_ones([0, 1]) == 1
    assert max_ones([1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1]) == 5
    assert max_ones([1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]) == 6
    assert max_ones([0, 0, 0, 1, 0, 1, 0, 1, 0, 1]) == 2
    assert max_ones([1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]) == 8


test()
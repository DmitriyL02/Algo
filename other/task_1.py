# O(len(s)), s = first_seq
def not_intersection_numbers(first_seq, second_seq):
    return set(first_seq) - set(second_seq)


if __name__ == '__main__':

    print(*not_intersection_numbers([1, 2, 3, 4, 6], [1, 2, 3, 0, 7]), sep=' ')


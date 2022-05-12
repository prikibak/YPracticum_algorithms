import sys
from collections import defaultdict


speed_debug = False

def main():
    n = int(read_line())
    if n == 0:
        print(0)
        return
    arr = list(map({'0':-1,'1':1}.get, read_line().split()))
    if n == 1:
        print(0)
        return
    # n = 100_000
    # arr = []
    # for _ in range(n//2):
    #     arr.append(-1)
    #     arr.append(1)

    print(1) if speed_debug else None
    first_n_sums = get_first_n_sums(arr)
    print(first_n_sums) if speed_debug else None
    print(2) if speed_debug else None
    lvls_indexes = defaultdict(list)
    for index, lvl in enumerate(first_n_sums):
        if len(lvls_indexes[lvl]) == 2:
            lvls_indexes[lvl][-1] = index
        else:
            lvls_indexes[lvl].append(index)
    print(lvls_indexes) if speed_debug else None
    print(3) if speed_debug else None
    max_diff = -float('inf')
    for lvl, indexes in lvls_indexes.items():
        curr_diff = indexes[-1] - indexes[0]
        if max_diff < curr_diff:
            max_diff = curr_diff
    print(max_diff)
    print(4) if speed_debug else None


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


def get_first_n_sums(arr):
    # first_n_sums = [None] * len(arr)
    sum_ = 0
    for i, number in enumerate(arr):
        # sum_ += number#{1:1,0:-1}[number]
        # arr[i] = sum_
        arr[i] = sum_
        sum_ += number#{1:1,0:-1}[number]
    arr.append(sum_)
    return arr


if __name__ == '__main__':
    main()

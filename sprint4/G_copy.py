import sys


def main():
    n = int(read_line())
    if n == 0:
        print(0)
        return
    arr = list(map({'0':-1,'1':1}.get, read_line().split()))
    if n == 1:
        print(0)
        return
    # n = 10_000
    # arr = []
    # for _ in range(n//2):
    #     arr.append(-1)
    #     arr.append(1)

    # initial_sum = sum(arr)
    # res = foo(arr, 0, n - 1, initial_sum)
    # # print(res)
    # print(res[1] - res[0] + 1)
    print(1)
    first_n_sums = get_first_n_sums(arr)
    # def key_2(elem):
    #     i, j = elem
    #     left_sum = first_n_sums[i - 1] if i > 0 else 0
    #     return first_n_sums[j] - left_sum
    print(2)
    def key_(elem):
        # i, j = elem
        # left_sum = first_n_sums[i - 1] if i > 0 else 0
        # if first_n_sums[j] - left_sum == 0:
        #     return j - i
        # return -float('inf')
        i, j = elem
        if first_n_sums[j+1] - first_n_sums[i] == 0:
            return j - i
        return -float('inf')
    max_length = -float('inf')
    max_elem = None, None
    # for elem in ((i, j) for i in range(n-1) for j in range(i+1, n)):
    #     max_length = max(max_length, key_(elem))
    for i in range(n-1):
        for j in range(i+1, n):
            elem = i, j
            if max_length < key_(elem):
                max_length = key_(elem)
                max_elem = elem
    print(3)
    # print(indexes)
    # print(list(map(key_2, indexes)))
    # print(list(map(key_, indexes)))
    # # print(arr[0:9+1])
    # # print(first_n_sums[0:9+1])
    if max_length != -float('inf'):
        print(max_elem)
        print(max_length + 1)
    else:
        print(0)


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


def foo(arr, left_index, right_index, current_sum):
    # print(left_index, right_index, current_sum)
    if current_sum == 0 or right_index <= left_index:
        return left_index, right_index, current_sum

    first_res = foo(arr, left_index+1, right_index, current_sum - arr[left_index])
    second_res = foo(arr, left_index, right_index-1, current_sum - arr[right_index])
    return max([first_res, second_res], key=lambda elem: elem[1] - elem[0])


if __name__ == '__main__':
    main()

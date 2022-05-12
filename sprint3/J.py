import sys


def main():
    numbers_count = int(read_line())
    numbers = list(map(int, read_line().split()))
    res_arr = bubble_sort(numbers)
    print('\n'.join(res_arr))


def read_line():
    return sys.stdin.readline()


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        current_elem, j = numbers[i], i
        while j > 0 and current_elem < numbers[j-1]:
            numbers[j], j = numbers[j-1], j-1
        numbers[j] = current_elem
        # print(' '.join(map(str, numbers)))


def bubble_sort(numbers):
    res_arr = []
    for i in range(0, len(numbers)):
        # print(j, len(numbers), j < (len(numbers) - 1) )
        for j in range(0, len(numbers) - 1):
            # print(numbers[j], numbers[j+1])
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            j += 1
        cur_res = ' '.join(map(str, numbers))
        if len(res_arr) == 0 or cur_res != res_arr[-1]:
            res_arr.append(cur_res)
    return res_arr


if __name__ == '__main__':
    main()

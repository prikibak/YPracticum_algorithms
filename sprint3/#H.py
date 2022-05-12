"""
In:
38
82 58 66 34 64 37 40 97 93 52 28 98 90 64 19 22 21 83 56 70 46 17 31 51 55 41 68 18 98 89 88 74 6 6 31 36 35 8
Out:
9898979390898888382747068666664645856555251464140373635343131282221191817
"""
import sys


def main():
    numbers_count = int(read_line())
    numbers = list(read_line().split())
    insertion_sort(numbers)
    print(''.join(reversed(numbers)))


def read_line():
    return sys.stdin.readline()


def insertion_sort(numbers):
    def first_less(x1, x2):
        return x1 + x2 < x2 + x1

    for i in range(1, len(numbers)):
        current_elem, j = numbers[i], i
        while j > 0 and first_less(current_elem, numbers[j-1]):
            numbers[j], j = numbers[j-1], j-1
        numbers[j] = current_elem


# def bubble_sort(numbers):
#     res_arr = []
#     for i in range(0, len(numbers)):
#         # print(j, len(numbers), j < (len(numbers) - 1) )
#         for j in range(0, len(numbers) - 1):
#             # print(numbers[j], numbers[j+1])
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#             j += 1
#         cur_res = ' '.join(map(str, numbers))
#         if len(res_arr) == 0 or cur_res != res_arr[-1]:
#             res_arr.append(cur_res)
#     return res_arr


if __name__ == '__main__':
    main()

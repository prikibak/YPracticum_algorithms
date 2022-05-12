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


if __name__ == '__main__':
    main()
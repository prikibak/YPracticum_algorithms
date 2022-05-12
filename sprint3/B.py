import sys


config = {
    2:'abc', 3:'def', 4:'ghi',
    5:'jkl', 6:'mno', 7:'pqrs',
    8:'tuv', 9:'wxyz'
}


def main():
    numbers = list(read_line().replace('\n', ''))
    res_lst = []
    find_combinations(numbers, 0, '', res_lst)
    print(' '.join(res_lst))


def read_line():
    return sys.stdin.readline()


def find_combinations(numbers, position, s, res_lst):
    if position == len(numbers):
        res_lst.append(s)
    else:
        current_key = numbers[position]
        options = config[int(current_key)]
        for symbol in options:
            find_combinations(numbers, position + 1, s + symbol, res_lst)


if __name__ == '__main__':
    main()

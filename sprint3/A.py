import sys


def main():
    n = int(read_line())
    brakets_list = []
    find_all_brakets_combinations(2*n, brakets_list, '')
    print('\n'.join([
        brakets for brakets in brakets_list
        if is_true_breakets_seq(brakets)]))


def read_line():
    return sys.stdin.readline()


def find_all_brakets_combinations(double_n, brakets_list, s):
    if double_n == 0:
        brakets_list.append(s)
    else:
        find_all_brakets_combinations(double_n - 1, brakets_list, s + '(')
        find_all_brakets_combinations(double_n - 1, brakets_list, s + ')')


def is_true_breakets_seq(s: str):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            raise NotImplementedError(f'Not braket symbol: {char}')
    return len(stack) == 0


if __name__ == '__main__':
    main()

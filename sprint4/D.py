import sys
from collections import OrderedDict


def main():
    n = int(read_line())
    ordered_counter = OrderedDict()
    for _ in range(n):
        name = read_line()
        if ordered_counter.get(name, None) is None:
            ordered_counter[name] = 0
        else:
            ordered_counter[name] += 1
    for name, _ in ordered_counter.items():
        print(name)


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


if __name__ == '__main__':
    main()

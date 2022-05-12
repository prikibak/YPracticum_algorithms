import sys
from collections import defaultdict


def main():
    s1 = read_line()
    s2 = read_line()
    is_not_eq_length = len(s1) != len(s2)
    if is_not_eq_length:
        print('NO')
        return
    symbols_mapper1 = {}
    symbols_mapper2 = {}
    for i in range(len(s1)):
        symbol1 = s1[i]
        symbol2 = s2[i]
        mapped_symbol = symbols_mapper1.get(symbol1, None)
        back_mapped_symbol = symbols_mapper2.get(symbol2, None)
        if mapped_symbol is None and back_mapped_symbol is None:
            symbols_mapper1[symbol1] = symbol2
            symbols_mapper2[symbol2] = symbol1
        elif mapped_symbol != symbol2 or back_mapped_symbol != symbol1:
            print('NO')
            return
    print('YES')


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


def check_length(s1, s2):
    return len(s1) != len(s2)


if __name__ == '__main__':
    main()

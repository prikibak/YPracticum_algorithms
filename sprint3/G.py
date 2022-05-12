import sys


def main():
    """
    0 - pink
    1 - yellow
    2 - crimson
    """
    n = int(read_line())
    arr = read_line().split()
    res = ([], [], [])
    for el in arr:
        res[int(el)].append(el)
    print(' '.join(sum(res)))


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


def sum(elems):
    if len(elems) == 0:
        return None
    else:
        res = elems[0]
        for elem in elems[1:]:
            res += elem
        return res


if __name__ == '__main__':
    main()

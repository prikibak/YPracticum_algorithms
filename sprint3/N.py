import sys


def main():
    n = int(read_line())
    lst = []
    for _ in range(n):
        clumb = list(map(int, read_line().split()))
        lst.append(clumb)
    lst.sort()
    start_indx, end_inxs = lst[0]
    for clumb in lst[1:]:
        curr_start_indx, curr_end_inxs = clumb
        if start_indx == curr_start_indx:
            end_inxs = curr_end_inxs
        elif curr_start_indx <= end_inxs:
            if curr_end_inxs > end_inxs:
                end_inxs = curr_end_inxs
        else:
            print(start_indx, end_inxs)
            start_indx, end_inxs = clumb
    print(start_indx, end_inxs)


def read_line():
    return sys.stdin.readline()[:-1]  # remove \n


if __name__ == '__main__':
    main()

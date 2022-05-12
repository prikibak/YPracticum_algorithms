import sys


def main():
    string1 = read_line()
    string2 = read_line()
    print(is_sub_string(string1, string2))


def read_line():
    return sys.stdin.readline()[:-1]  # remove \n


def is_sub_string(s1, s2):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)


if __name__ == '__main__':
    main()

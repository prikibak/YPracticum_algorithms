import sys


def main():
    a = int(read_line())
    m = int(read_line())
    arr_s = read_line()
    chars_dct = {
        **{chr(code): code for code in range(ord('a'), ord('z')+1)},
        **{chr(code): code for code in range(ord('A'), ord('Z')+1)}}
    first_n_sum = get_first_n_hash_sums(arr_s, a, m, chars_dct)
    t = int(read_line())
    for _ in range(t):
        i, j = read_line().split()#list(map(lambda num: int(num)-1, read_line().split()))
        i, j = int(i)-1 , int(j)-1
        # res = (elem[1] * a + elem[0]) % (a ** (j - i + 1))
        def decode_elem(elem):
            return elem
            # return elem[1] * a + elem[0]
        pow_ = pow(a, j - i + 1, m)
        res = (decode_elem(first_n_sum[j]) - (decode_elem(first_n_sum[i-1]) * pow_) % m) % m
        print(res)


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


# def str_hash(s, a, m):
#     sum_ = 0
#     for char in s:
#         sum_ = (sum_ * a + ord(char)) % m
#     return sum_


def get_first_n_hash_sums(arr_s, a, m, chars_dct):
    first_n_sum = [0] * (len(arr_s) + 1)  # one more element for i-1 when i==0
    sum_ = 0
    # sum_part1, sum_part2 = 0, 0
    i = 0
    for i in range(len((arr_s))):
        # # sum_ = ((sum_part2 * a + sum_part1) * a + ord(char)) % m
        # # sum_part1, sum_part2 = sum_ % a, sum_ // a
        # # arr_s[i] = (sum_part1, sum_part2)
        char = arr_s[i]
        # sum_ = (sum_part2 * a + sum_part1)
        sum_ = (sum_ * a + chars_dct[char]) % m
        # first_n_sum[i] = sum_ % a, sum_ // a
        first_n_sum[i] = sum_
        i += 1
    return first_n_sum


if __name__ == '__main__':
    main()

"""
#TOTRY:
- for each element: how many elements going left and right (then repeat for sub-trees)
"""
import sys
import itertools
from collections import defaultdict
# from math import comb


def to_tree(perm):
    return str(perm[-3:])


def get_tree_variants_count(n):
    res = defaultdict(int)
    for perm in itertools.permutations(list(range(n))):
        binnary_tree_array = to_tree(perm)
        res[binnary_tree_array] += 1
    return len(res)



def main():
    node_number = int(sys.stdin.readline())
    print(get_tree_variants_count(node_number))


if __name__ == '__main__':
    main()

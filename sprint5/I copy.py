import sys
from math import comb


def get_tree_variants(binary_tree: list, available_nodes_number: int):
    if available_nodes_number == 0:
        return [tuple(binary_tree)]

    res = []
    for i, node in enumerate(binary_tree):
        if node == 1:
            if binary_tree[2*i+1] == 0:
                new_b_tree = list(binary_tree)
                new_b_tree[2*i+1] = 1
                res += get_tree_variants(new_b_tree, available_nodes_number-1)
            if binary_tree[2*i+2] == 0:
                new_b_tree = list(binary_tree)
                new_b_tree[2*i+2] = 1
                res += get_tree_variants(new_b_tree, available_nodes_number-1)
    return res



def main():
    node_number = int(sys.stdin.readline())
    binary_tree_copasity = sum(2**i for i in range(node_number))
    print('binary_tree_copasity', binary_tree_copasity)
    print('comb', comb(binary_tree_copasity, node_number))
    binary_tree = binary_tree_copasity * [0]
    binary_tree[0] = 1
    print(len(set(get_tree_variants(binary_tree, node_number-1))))


if __name__ == '__main__':
    main()

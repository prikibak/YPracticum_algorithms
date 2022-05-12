# # Comment it before submitting
# from typing import Tuple, Optional


# class Node:
#     def __init__(self, left=None, right=None, value=0, size=0):
#         self.right = right
#         self.left = left
#         self.value = value
#         self.size = size


def _get_size(node):
    return node.size if node is not None else 0


def split(root, k):
    if root is None:
        return None, None
    if _get_size(root.left) + 1 <= k:
        k_fixed = k - (_get_size(root.left) + 1)
        root.right, right_side = split(root.right, k_fixed)
        root.size -= _get_size(right_side)
        if root.right is not None:
            root.right.size -= _get_size(right_side)
        return root, right_side
    left_side, root.left = split(root.left, k)
    root.size -= _get_size(left_side)
    if root.left is not None:
        root.left.size -= _get_size(left_side)
    return left_side, root


# def set_sizes(node):
#     if node is None:
#         return 0
#     node.size = 1 + set_sizes(node.left) + set_sizes(node.right)
#     return node.size


def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)

    left, right = split(node6, 4)
    # set_sizes(left)
    # set_sizes(right)

    # print(left.size, right.size)
    assert(left.size == 4)
    assert(right.size == 2)

# test()

# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
from itertools import zip_longest


def _lmr_pass(tree, seq):
    if tree.left is not None:
        yield from _lmr_pass(tree.left, seq + '0')
    yield tree.value, seq
    if tree.right is not None:
        yield from _lmr_pass(tree.right, seq + '1')


def solution(root1, root2):
    if root1 is None and root2 is not None:
        return False
    if root1 is not None and root2 is None:
        return False

    if root1 is None and root2 is None:
        return True

    for val1, val2 in zip_longest(_lmr_pass(root1, ''), _lmr_pass(root2, '')):
        if val1 != val2:
            return False
    return True


def test():
    # node1 = Node(3,  None,  None)
    # node2 = Node(4,  None,  None)
    # node3 = Node(4,  None,  None)
    # node4 = Node(3,  None,  None)
    # node5 = Node(2, node1, node2)
    # node6 = Node(2, node3, node4)
    # node7 = Node(1, node5, node6)

    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)

    assert solution(node7)

# test()

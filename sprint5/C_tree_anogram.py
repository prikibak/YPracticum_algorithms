# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def _lmr_pass(tree, seq):
    if tree.left is not None:
        yield from _lmr_pass(tree.left, seq + '0')
    yield tree.value, seq
    if tree.right is not None:
        yield from _lmr_pass(tree.right, seq + '1')


def _rml_pass(tree, seq):
    if tree.right is not None:
        yield from _rml_pass(tree.right, seq + '0')
    yield tree.value, seq
    if tree.left is not None:
        yield from _rml_pass(tree.left, seq + '1')


def solution(root):
    if root.left is None and root.right is not None:
        return False
    if root.left is not None and root.right is None:
        return False

    if root.left is None and root.right is None:
        return True

    for val1, val2 in zip(_lmr_pass(root.left, ''), _rml_pass(root.right, '')):
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

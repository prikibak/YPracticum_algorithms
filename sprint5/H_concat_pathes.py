# # Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def _get_all_numbers(node):
    if node is None:
        return []

    if node.left is None and node.right is None:
        return [str(node.value)]

    if node.left is None:
        return [str(node.value) + el for el in _get_all_numbers(node.right)]
    elif node.right is None:
        return [str(node.value) + el for el in _get_all_numbers(node.left)]
    else:
        return [str(node.value) + el for el in _get_all_numbers(node.right)]\
            + [str(node.value) + el for el in _get_all_numbers(node.left)]


def solution(root) -> int:
    return sum(map(int, _get_all_numbers(root)))


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275

    assert solution(node1) == 2
    assert solution(None) == 0

# test()

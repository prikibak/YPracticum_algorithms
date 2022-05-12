# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def get_depth(node: Node):
    if node is None:
        return 0, True

    left_depth, left_balanced = get_depth(node.left)
    right_depth, right_balanced = get_depth(node.right)

    balanced = left_balanced and right_balanced \
        and abs(left_depth - right_depth) <= 1

    return max(left_depth, right_depth) + 1, balanced


def solution(root: Node):
    depth, balanced = get_depth(root)
    return balanced


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


test()

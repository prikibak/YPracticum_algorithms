class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return f'{self.value}, {self.left is not None}, {self.right is not None}'


def solution(node: Node):
    _, _, state = check_binary_search_tree(node)
    return state


def check_binary_search_tree(node: Node):
    # if node is None:
    #     return float('inf'), -float('inf'), True

    # left_min, left_max, left_state = None, None, True
    # right_min, right_max, right_state = None, None, True

    if node.left:
        left_min, left_max, left_state = check_binary_search_tree(node.left)
        if left_state is False:
            return None, None, left_state
    else:
        left_min, left_max, left_state = node.value, node.value, True

    if node.right:
        right_min, right_max, right_state = check_binary_search_tree(node.right)
        if right_state is False:
            return None, None, right_state
    else:
        right_min, right_max, right_state = node.value, node.value, True

    # print(left_max, right_min)
    state = ((not node.left) or left_max < node.value) \
        and ((not node.right) or node.value < right_min)

    # print(node, '|', state)
    return left_min, right_max, state


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


# if __name__ == '__main__':
#     test()

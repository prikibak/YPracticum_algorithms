# Напишите функцию, которая будет выводить по неубыванию все ключи от L до R
# включительно в заданном бинарном дереве поиска.
# Ключи в дереве могут повторяться. Решение должно иметь сложность O(h+k)
# , где h –— глубина дерева, k — число элементов в ответе. В данной задаче
# если в узле содержится ключ x, то другие ключи, равные x , могут быть как
# в правом, так и в левом поддереве данного узла. (Дерево строил стажёр, так
# что ничего страшного).

# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def print_range(node, l, r):
    if node.value < l:  # LMR optimization for interval search?
        if node.right is not None:
            print_range(node.right, l, r)
        return
    else:  # node.value >= l
        if node.left is not None:
            print_range(node.left, l, r)

    # if node.left is not None:
    #     print_range(node.left, l, r)

    value = node.value
    if l <= value and value <= r:
        print(value)
    elif value > r:
        return

    if node.right is not None:
        print_range(node.right, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8

if __name__ == '__main__':
    test()

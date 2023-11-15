# 97363513
"""
-- ПРИНЦИП РАБОТЫ --
В первую очередь проиходит поиск в бинарном дереве целевого узла по значению.
На каждом шаге, если узел не найден, продолжаем поиск в правом (или левом) поддереве, если текущий узел меньше (больше) целевого значения.

Если узел найден, начинается процедура удаления:
1. Если удаляемый узел имеет левое поддерево, находим в нем максимальный (крайний правый) узел и меняем местами с удаляемым.
    1. Следим чтобы новый узел на месте удаляемого сохранил его ссылку на правое (сам новый узел не имеет правого поддерева т.к. крайний правый).
    2. Если новый узел имеет левое поддерево - его нужно зацепить на изначального родителя нового узла.
        (в качестве правого поддерева, если родитель не целевой узел).
2. Иначе, если удаляемый узел имеет правое поддерево, находим в нем минимальный (крайний левый) узел и меняем местами с удаляемым.
    1. Следим чтобы новый узел на месте удаляемого сохранил его ссылку на левое (сам новый узел не имеет левого поддерева т.к. крайний левый).
    2. Если новый узел имеет правое поддерево - его нужно зацепить на изначального родителя нового узла
        (в качестве левого поддерева, если родитель не целевой узел).
3. Иначе, просто удаляем узел т.к. у него нет поддеревьев.

Далее
1. Если удаляемый узел имеет родителя, следим за тем чтобы ссылка у этого родителя осталась актуальной (либо пустой, если удаляемый узел без поддеревьев).
2. Если удаляемый узел не имеет родителя значит удаляется корень (и тогда возвращаем узел как новый корень).

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Крайний правый узел в левом поддереве будет самым большим узлом в левом поддереве (согласно принципу построения бинарного дерева поиска).
Но он также будет меньше любого узла в правом поддереве. Поэтому если сделать его целевым узлом - принцип построения дерева не нарушится.

Такая же логика для крайнего левого в правом поддереве.

Остаётся убедиться в корректности реализации.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Поиск в бинарном дереве поиска O(h) = O(log(n)).

Поиск элемента для замены в худшем случае O(h) = O(log(n)).

Замена узлов - O(1).

Общая сложность по времени:

O(h) = O(log(n))

p.s. предполагается что дерево сбалансировано, иначе O(h) может быть равно O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Равно количеству элементов в бинарном дереве поиска O(n)

"""
from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

        def print(self, pad_number=0, tab='___') -> str:
            print(tab*pad_number, self.value)
            if self.left is not None:
                self.left.print(pad_number+1)
            else:
                print(tab*(pad_number+1), self.left)
            if self.right is not None:
                self.right.print(pad_number+1)
            else:
                print(tab*(pad_number+1), self.right)
else:
    from node import Node


def find(root, key):
    current_node, parrent_node = root, None
    while current_node and current_node.value != key:
        if current_node.value > key:
            current_node, parrent_node = current_node.left, current_node
        else:
            current_node, parrent_node = current_node.right, current_node
    return current_node, parrent_node


def get_min(root):
    assert root is not None
    current_node, parrent_node = root, None
    while current_node and current_node.left:
        current_node, parrent_node = current_node.left, current_node
    return current_node, parrent_node


def get_max(root):
    assert root is not None
    current_node, parrent_node = root, None
    while current_node and current_node.right:
        current_node, parrent_node = current_node.right, current_node
    return current_node, parrent_node


def remove(root, key) -> Optional[Node]:
    target_node, target_parrent = find(root, key)
    if target_node is None:
        return root

    new_target_node = None
    if target_node.left:
        max_left_branch_node, max_left_branch_parrent = get_max(target_node.left)
        if max_left_branch_parrent is None:  # parrent == target_node
            max_left_branch_node.right = target_node.right
        else:  # parrent != target_node
            max_left_branch_parrent.right = max_left_branch_node.left
            max_left_branch_node.right = target_node.right
            max_left_branch_node.left = target_node.left

        new_target_node = max_left_branch_node
    elif target_node.right:
        min_right_branch_node, min_right_branch_parrent = get_min(target_node.right)
        if min_right_branch_parrent is None:  # parrent == target_node
            min_right_branch_node.left = target_node.left
        else:  # parrent != target_node
            min_right_branch_parrent.left = min_right_branch_node.right
            min_right_branch_node.right = target_node.right
            min_right_branch_node.left = target_node.left

        new_target_node = min_right_branch_node

    if target_parrent is None:  # target_node is root-node
        return new_target_node

    if target_parrent.left is target_node:  # target_node is not root-node
        target_parrent.left = new_target_node
    else:
        target_parrent.right = new_target_node
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    # node7.print()
    # print('****'*4)
    # # node_, parrent  = find(node7, 7)
    # # parrent.print()
    # # if node_ is not None:
    # #     node_.print()

    # newHead = remove(node7, 2)
    # newHead.print()

    newHead = remove(node7, 10)
    # newHead.print()
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8

    # newHead = remove(node7, 3)
    # newHead.print()


if __name__ == '__main__':
    test()

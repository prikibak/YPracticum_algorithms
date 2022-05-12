# 56278391  убрал закоменченный не используемый код
"""
-- ПРИНЦИП РАБОТЫ --
Сначала через бинарный поиск с адаптивным условием нахожу начальный (или минимальный)
элемент массива. Зная его можно разбить массив на два строго отсортированных и запустить
бинарный поиск на одном из них. А именно, если левая сдвинутая часть не пуста и искомый
элемент меньше минимального (смого левого) в ней - то ищем в ней, иначе ищем в правой части.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Благодаря нахождению начального элемента появляется возможность разделить массив на два
отсортированных (причем найти его можно со скоростью O(log(n))). Также дальше на осортированных
массивах мы можем запустить бинарный поиск (который также отработает за O(log(n))).

Таким образом поставленные условия задачи будут выполнены.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
На каждом рукурсивном шаге половина массива отсекается. Таким образом сложность по времени O(log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В текущей реализации доп память ипользуется только для храниения индексов (таких как left_index,
middle_index, right_index), искомого значения и ссылки на массив => O(1).

Рекурсивных вызовов будет O(log(n)).

Общая сложнасть O(log(n)).

"""
import sys


def main():
    n = int(read_line())
    k = int(read_line())
    arr = list(map(int, read_line().split()))
    print(broken_search(arr, k))


def read_line():
    return sys.stdin.readline().replace('\n', '')


def broken_binary_search(nums, left_index, right_index, target):
    middle_index = left_index + (right_index - left_index) // 2
    next_middle_index = (middle_index + 1) % len(nums)

    if nums[middle_index] == target:
        return middle_index
    if right_index - left_index <= 0:
        return -1

    left_sorted = False
    if nums[left_index] < nums[middle_index]:
        left_sorted = True

    if left_sorted:
        if nums[left_index] <= target <= nums[middle_index]:
            return broken_binary_search(nums, left_index, middle_index, target)
        else:
            return broken_binary_search(nums, next_middle_index, right_index, target)
    elif not left_sorted:
        if nums[next_middle_index] <= target <= nums[right_index]:
            return broken_binary_search(nums, next_middle_index, right_index, target)
        else:
            return broken_binary_search(nums, left_index, middle_index, target)
    else:
        return -1


def broken_search(nums, target) -> int:
    return broken_binary_search(nums, 0, len(nums)-1, target)


if __name__ == '__main__':
    main()

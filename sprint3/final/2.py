# 55933745  убрал закоменченный не используемый код
"""
-- ПРИНЦИП РАБОТЫ --
Считываем массив состваных элементов, преобразуем и группируем их в картеж таким образом чтобы
уловлетворить требуемые приоритет и направление сортировки.

Далее применяется реализация быстрой сортировки без использования дополнительной памяти. Принцип
in-place реализации взят из описания условия задачи.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Реализация удовлетворяет требованиям. Доп память не успользуется. Вместо этого выполняется поиск
неправильно расположенных (относительно pivot) элементов и их swap, пока не пересекутся индексы,
отслеживающие неправильно расположенные элементы.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложно доказать, но в среднем и в лучшем случае - O(n*log(n)).
В хуждем можно подобрать kill-sequence которая отработает за O(n^2).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Сортировка выполняется in-place без выделения доп памяти на хранение промежуточных массивов.

При этом каждый рекурсивный вызов требует O(1) памяти для храниения индексов и ссылки на массив.
Среднее количество рекурсивных вызовов при хорошей стратегии выбора опорного элемента будет O(log(n)).
Общая сложность таким образом O(1*log(n)) = O(log(n)).

В худжем случае количество рекурсивных вызовов может быть равно O(n). Худшая пространственная сложность
будет соответсвующей.

"""
import sys


def main():
    n = int(read_line())
    arr = read_arr(n)
    inplace_quick_sort(arr, 0, len(arr)-1)
    print_res(arr)


def read_line():
    return sys.stdin.readline().replace('\n', '')


def read_arr(n):
    arr, i = [None]*n, 0
    for i in range(n):
        row = read_line().split()
        arr[i] = (-int(row[1]), int(row[2]), row[0])
    return arr


def inplace_quick_sort(arr, left_index, right_index):
    if right_index - left_index < 1:
        return
    elif right_index - left_index == 1:
        if arr[right_index] < arr[left_index]:
            arr[right_index], arr[left_index] = arr[left_index], arr[right_index]
        return

    pivot_index = left_index + 1
    pivot_value = arr[pivot_index]

    i, j = left_index, right_index
    while i < j:
        while arr[j] > pivot_value:
            j -= 1
        while arr[i] < pivot_value:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    inplace_quick_sort(arr, left_index, j)
    inplace_quick_sort(arr, i, right_index)


def print_res(arr):
    for _, _, name in arr:
        print(name)


if __name__ == '__main__':
    main()

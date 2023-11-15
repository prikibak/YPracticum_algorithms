# 97327139
"""
-- ПРИНЦИП РАБОТЫ --
Все элементы считываются в специальный класс Competitor в котором реализованы спецаильные методы компарации в соответствии с требованиями задачи
 (таким образом получается список элементов пригодных к элементарному упорядочиванию).

Далее на основе этого списка формируется структура данных - Куча. Методом обратной итерации по внутреннему списку с просеиванием каждого элемента вниз.

После чего все элементы по-порядку считываются из Кучи методом pop и выводятся в стандартных оутпут.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

Согласно логике построенния структуры данных Куча корнем в ней всегда будет максимальный (минимальный) элемент.
Метод pop работает таким образом, что возвращает текущий максимальный (минимальный) элемент и приводит Кучу в нормальный (heapified) вид
 (ставит последний элемент на место корня и просеивает его вниз).

Таким образом, последовательно доставая элементы из Кучи методом pop мы получаем исходную последовательность в отсортированном виде.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Сначала мы создаём список из объекстов Competitor за O(n) времени.

Дальше на основе списка создается Куча. Алгоритм предпологает обратное итерирование по списку O(n) с вызовом на каждой итерации метода sift_down O(log(n)).
Таким образом общая сложность построения Кучи из списка O(n*log(n)). На самом деле, можно доказать что построение Кучи таким методом укладыватся в O(n), но
я думаю что такое доказательство выходит за рамки данного курса.

Дальше n-раз вызываем метод pop - внутри используется sift_down O(log(n)).

Чтобы сэкономить время при удалении последнего элемента из списка используется специальный счетчик длины списка, а перезапись происходит когда счетчик
становится в два раза меньше реальной длины хранящегося списка. Сложность - O(n*log(n)). Можно обойтись и без урезания длины внутреннего списка, скрипт
также успешно пройдет тесты, но я решил добавить для завершенности.

Таким образом общая сложность по времени:
 O(n) + O(n*log(n)) + O(n*log(n)) + O(n*log(n)) = O(n*log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Единственная нетривиальная дополнительная память которую я использую - внутренний список (массив) значений.
Его пространственная сложность соответсвует количеству элементов - O(n).

"""
from __future__ import annotations
import sys
from typing import Iterator, List
from dataclasses import dataclass
from collections.abc import Iterable


def main():
    n_competitors: int = int(read_line())
    competitors: Heap[ComparableCompetitor] = read_competitors_to_heap(n_competitors)
    competitor: ComparableCompetitor
    for competitor in competitors:
        print(competitor.name)


def test1():
    import random
    from datetime import datetime

    letters = tuple(chr(l_i) for l_i in range(ord('a'), ord('z')+1))
    competitors_list: List[Competitor] = []
    for _ in range(100000):
        name_len = random.randint(1, 20)
        name = ''.join([random.choice(letters) for _ in range(name_len)])
        solved_tasks = random.randint(1, 10**9)
        penalty = random.randint(1, 10**9)
        competitor: ComparableCompetitor \
            = ComparableCompetitor(name=name, solved_tasks=solved_tasks, penalty=penalty)
        competitors_list.append(competitor)

    time1 = datetime.now()
    competitors_heap: Heap[ComparableCompetitor] = Heap(competitors_list)
    time2 = datetime.now()
    print((time2 - time1).total_seconds() * 1000)  # total miliseconds

    time1 = datetime.now()
    competitor: ComparableCompetitor
    for competitor in competitors_heap:
        pass
    time2 = datetime.now()
    print((time2 - time1).total_seconds() * 1000)  # total miliseconds


@dataclass
class Competitor:
    name: str
    solved_tasks: int
    penalty: int


class ComparableCompetitor(Competitor):
    def __eq__(self, other: ComparableCompetitor):
        return self.name == other.name \
            and self.solved_tasks == other.solved_tasks \
            and self.penalty == other.penalty

    def __gt__(self, other: ComparableCompetitor):
        return self.solved_tasks > other.solved_tasks \
            or (self.penalty < other.penalty and self.solved_tasks == other.solved_tasks) \
            or (self.name < other.name and self.solved_tasks == other.solved_tasks and self.penalty == other.penalty)

    def __lt__(self, other: ComparableCompetitor):
        return other > self

    def __ge__(self, other: ComparableCompetitor):
        return self > other or self == other

    def __le__(self, other: ComparableCompetitor):
        return other > self or self == other


class Heap(Iterable):
    def __init__(self, lst=None):
        if lst is None:
            self._heap_list = [None]
            self._heap_length = 1
        else:
            self._heap_list = lst
            self._heap_length = len(self._heap_list)
            for reversed_i in range(len(self._heap_list) - 1, 0, -1):  # O(n*log(n)) or O(n) ???
                self.sift_down(reversed_i)

    # def add(self, elem):
    #     self._heap_list.append(elem)                    # O(1)
    #     self._heap_length += 1
    #     idx = self._heap_length - 1
    #     if self._heap_length > 1:
    #         idx = self.sift_up(idx)                     # O(log(n))
    #         idx = self.sift_down(idx)                   # O(log(n))

    def pop(self):
        if self._heap_length == 1:
            return None
        elem = self._heap_list[1]                       # O(1)
        # self._heap_list = self._heap_list[:-1]        # O(n)? cause time-limit-error
        last_heap_elem_index = self._heap_length - 1
        self._heap_list[1] \
            = self._heap_list[last_heap_elem_index]     # O(1)
        self._heap_length -= 1
        self.sift_down(1)                               # O(log(n))

        half_heap_list_index = len(self._heap_list) // 2
        if self._heap_length < half_heap_list_index:
            self._heap_list = self._heap_list[:half_heap_list_index+1]
        return elem

    def __iter__(self) -> Iterator:
        elem = self.pop()
        while elem is not None:
            yield elem
            elem = self.pop()

    def sift_down(self, sift_idx: int) -> int:
        left_idx = 2*sift_idx
        right_idx = left_idx + 1

        if self._heap_length <= left_idx:
            return sift_idx

        if self._heap_length <= right_idx:
            max_idx = left_idx
        else:
            max_idx = max([left_idx, right_idx], key=lambda idx: self._heap_list[idx])

        if self._heap_list[sift_idx] >= self._heap_list[max_idx]:
            return sift_idx
        else:
            self._heap_list[sift_idx], self._heap_list[max_idx] = self._heap_list[max_idx], self._heap_list[sift_idx]
            return self.sift_down(max_idx)

    def sift_up(self, sift_idx: int) -> int:
        if sift_idx <= 1:
            return sift_idx

        parent_idx = sift_idx // 2

        if self._heap_list[parent_idx] < self._heap_list[sift_idx]:
            self._heap_list[parent_idx], self._heap_list[sift_idx] = self._heap_list[sift_idx], self._heap_list[parent_idx]
            return self.sift_up(parent_idx)
        else:
            return sift_idx


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


def read_competitor() -> ComparableCompetitor:
    name, solved_tasks, penalty = read_line().split()
    solved_tasks = int(solved_tasks)
    penalty      = int(penalty)
    return ComparableCompetitor(name=name, solved_tasks=solved_tasks, penalty=penalty)


def read_competitors_to_heap(n_competitors) -> Heap[ComparableCompetitor]:
    competitors_list: List[ComparableCompetitor] = (n_competitors + 1) * [None]
    for i in range(1, n_competitors + 1):
        competitor: ComparableCompetitor = read_competitor()
        competitors_list[i] = competitor
    competitors_heap: Heap[ComparableCompetitor] = Heap(competitors_list)
    return competitors_heap


if __name__ == '__main__':
    main()
    # test1()  # local debug of max execution time

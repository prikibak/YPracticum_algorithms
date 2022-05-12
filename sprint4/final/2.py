# 58694452
"""
-- ПРИНЦИП РАБОТЫ --

 Реализация Хеш-Таблицы методом цепочек.

 Особенности реализации:
 - каждая ячейка - динамический массив
 - при удалении элементы заменяются на пустые пары
 - если при добавлении есть пустые пары - первую пустю пару заменяем на новую

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Интерфейс коллекции соответсвуюет тому условии что описан в условии.
 Все описанные в условии нюансы реализованы требуемым образом.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

При хорошей Хеш-Функции и естественном поступлении ключей
 (или, другими словами, при равномерном расперделении ключей по таблицам)
 Сложность операций в будет равна O(1 + N/M), где N - количество элементов в таблице,
 M - количество ячеек. С помобщью операций рехеширования и масштабирования соотношение N/M
 стараются поддерживать в заданном диапазоне, соответственно при оценке асимптотики им можно
 принебречь. В данном конкретном случае размер таблицы фиксирован, поэтому при увеличении
 количества уникальных ключей скорость операций будет падать соотношение N/M будет все сильнее
 влиять на асимптотику.

При этом для любой Хеш-функции теоритически можно подобрать последовательность
 ключей так, что сложность операций будет равна O(N) - когда все ключи попадают в одну ячейку.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Пространственную сложность можно оценить как O(N), где N - количество элементов в таблице.

"""
import sys


MAX_HT_SIZE = 10**5


def main():
    hash_table = HashTable(size=MAX_HT_SIZE)

    n_requests = int(read_line())
    for _ in range(n_requests):
        request = read_line().split()
        method, args = request[0], request[1:]
        if method == 'put':
            key, value = args
            hash_table.put(int(key), value)
        elif method == 'get':
            key, = args
            print(hash_table.get(int(key)))
        elif method == 'delete':
            key, = args
            print(hash_table.delete(int(key)))


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


class HashTable:
    def __init__(self, size, hash_power=127) -> None:
        self._size = size
        self._hash_power = hash_power
        self._table = [None] * self._size

    def hash(self, num: int):
        return (num * self._hash_power) % self._size

    def put(self, key: str, value):
        table_i = self.hash(key)
        if self._table[table_i] is None:
            self._table[table_i] = [(key, value)]
        else:
            empty_j = None
            for j, (ex_key, _) in enumerate(self._table[table_i]):
                if key == ex_key:
                    self._table[table_i][j] = (key, value)
                    return
                elif key is None and empty_j is None:
                    empty_j = j
            if empty_j is None:
                self._table[table_i].append((key, value))
            else:
                self._table[table_i][empty_j] = (key, value)

    def get(self, key: str):
        table_i = self.hash(key)
        if self._table[table_i] is not None:
            for ex_key, ex_value in self._table[table_i]:
                if key == ex_key:
                    return ex_value
        return None

    def delete(self, key: str):
        table_i = self.hash(key)
        if self._table[table_i] is not None:
            for j, (ex_key, ex_value) in enumerate(self._table[table_i]):
                if key == ex_key:
                    self._table[table_i][j] = (None, None)
                    return ex_value
        return None


if __name__ == '__main__':
    main()

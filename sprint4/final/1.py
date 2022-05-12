# 58698243
"""
-- ПРИНЦИП РАБОТЫ --

Сначало происходит считывание всех документов и построение поискового индекса на их основе.

Поисковой индекс представляется из себя Хеш-таблицу, первичным ключом в которой явлется
 слово, а вторичным - номер документа. Первичное значение - хеш-таблица, вторичное - количество
 вхождений слова в конкретный документ.

Далее на основе этого индекса для каждого запроса выполняется ранжирование документов по приципу
 суммирования количества вхождений каждого уникального слова в документы, в которых оно встречается.

Учтен и оптимизирован кейс с повторяющимися документами.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

Принцип ранжирования реализован согласно требованием в условии задачи. Программа проходит тесты
 удовлетворяя лимиты скорости и памяти.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Итерируемся по документа O(D)
    Ищем документ в таблице поторений O(1)
        Итерируемся по словам O(Wi)
            Проверяем в индексе ли слово O(1)
            Проверяем в индексе ли номер документа для этого слова O(1)

Таким образом сложность по времени для построения индекса - O(D*W), где D - количество
 документов, W - среднее количество слов в документе (можно расписать подробнее через сумму).

Итерируеся по запросам O(R)
    Находим уникальные слова в запросе O(Vi)
    Итерируемся по уникальным словам запроса O(uVj)
        Достаем индекс для слова O(1)
        Итерируемся по всем документам в индексе слова O(Tj)
            Суммируем в общий скор по документам O(1)
    Сортируем список релевантностей документов. Средний случай - O(U*log(U))

Таким образом сложность по времени для ранжирования всех запросов
 O(R*(V + uV*T + U*log(U))), где R - количество запросов, V - среднее количество слов в запросе,
 uV - среднее количество уникальных слов в запросе, T - среднее количество документов в поисковом индексе
 для слова, U - среднее количество документов пересекающихся с запросом.

Общая сложность по времени:
O(D*W) + O(R*(V + uV*T + U*log(U)))
O(D*W + R*(V + uV*T + U*log(U)))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

words_index - посковой индекс.
 O(uW * T), где uW - количество уникальных слов во всех документах вместе, T - среднее количество документов
 в поисковом индексе для слова.

doc_to_score - локальная Хеш-таблица, которая хранит для каждогу документа его скор для слов из запроса.
 O(U), где U - среднее количество документов пересекающихся с запросом.

Выдача хранит O(5) = O(1) наиболее релевантных документов.

Общая пространственная сложность:
O(uW*T + U + 1) = O(uW*T + U)

"""
import sys

TOP_N = 5


def main():

    n_docs = int(read_line())
    words_index = read_and_build_words_index(n_docs)

    n_requests = int(read_line())
    # requests = read_lines_to_arr(count=n_requests)

    for _ in range(n_requests):
        request = read_line()
        ranking = rank_docs(request, words_index, top_n=TOP_N)
        print(' '.join(ranking) if len(ranking) > 0 else '')


def read_line():
    return sys.stdin.readline().replace('\n', '')  # remove \n


def read_and_build_words_index(n_docs):
    words_index = dict()
    for doc_i in range(n_docs):
        doc = read_line()
        for word in doc.split():
            if word not in words_index:
                words_index[word] = {doc_i: 1}
            else:
                count = 1
                if doc_i in words_index[word]:
                    count += words_index[word][doc_i]
                words_index[word][doc_i] = count
    return words_index


def nth_largest_linear(top_n, request_words_set, words_index):
    doc_to_score = dict()
    for word in request_words_set:
        if word not in words_index:
            continue
        for doc_i, count in words_index[word].items():
            if doc_i in doc_to_score:
                count += doc_to_score[doc_i]
            doc_to_score[doc_i] = count

    doc_and_scores = list(doc_to_score.items())
    doc_and_scores.sort(key=lambda item:  (item[1], -item[0]), reverse=True)
    return doc_and_scores[:top_n]


def rank_docs(request, words_index, top_n):
    request_words_set = set(request.split())
    return [
        str(doc_i + 1) for doc_i, _ in
        nth_largest_linear(top_n, request_words_set, words_index)]


if __name__ == '__main__':
    main()

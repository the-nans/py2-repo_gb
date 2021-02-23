"""
Определение количества различных подстрок с помощью хэшфункции . Пусть на вход функции дана строка. Требуется вернуть
количество различных подстрок в этой строке

* В сумму не включаем пустую подстроку и строку целиком
* Без использования функций для вычисления хэша(sha1, hash или любой другой из модуля hashlib, задача считается
не решённой
"""
import hashlib


def substrings(s: str):
    assert len(s) > 1, 'Строка должна быть длиннее одного символа'

    subs = {}

    len_s = len(s)
    # подсчитаем количество однобуквенных подстрок
    # с ними всё понятно, делаем это просто для скорости
    for i in s:
        subs[i] = s.count(i)

    # от скукотищи отмазались, давайте хэшить!

    n_len = 2  # длина минимально интересной нам подстроки
    pointer = 0  # курсор

    while pointer < len_s:
        while n_len < len_s:
            needle = hashlib.md5(s[pointer: pointer + n_len].encode('utf-8')).hexdigest()
            if s[pointer:pointer + n_len] in subs:  # чтобы не плодить дубли, проверим, не встречали ли мы такой
                break  # подстроки раньше. Если встречали - выходим из цикла
            subs[s[pointer:pointer + n_len]] = 0  # новое слово в словаре результатов
            for i in range(pointer, len_s):
                if needle == hashlib.md5(s[i:i + n_len].encode('utf-8')).hexdigest():  # чёт нашли
                    subs[s[pointer:pointer + n_len]] += 1
            n_len += 1  # увеличиваем длину искомой подстроки на один
        n_len = 2
        pointer += 1  # сдвигаем курсор на одну позицию левее по строке

    return subs


s = input('Введите произвольную строку: ')
# s = 'sobakasobaka'
print('В этой строке есть следующие подстроки:')
for k, v in substrings(s).items():
    print(f'{k} встречается {v} раз')

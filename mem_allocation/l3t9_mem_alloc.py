import sys
"""
Тестировалось на Linux Ubuntu, x64
"""

'''
lesson3 task 9 - исходный код
'''
from random import randint  # для ленивый


def minimax_matrix(cols, rows):
    arr_spread = 100
    spam, res = [], []
    ex = arr_spread
    matrix = [[randint(1, arr_spread) for i in range(rows)] for k in range(cols)]
    for line in matrix:
        for item in line:
            print(f"{item:<4}", end='')
        print()
    max_ = 0
    for i in range(cols):
        min_ = matrix[0][i]
        for j in range(rows):
            if matrix[j][i] < min_:
                min_ = matrix[j][i]
        if max_ < min_:
            max_ = min_
    print(sum([sys.getsizeof(k) for k in [cols, rows, arr_spread, spam, res, ex, matrix, i, line, item, max_, min_, ]]),
          'bytes used')
    return (max_)


print(minimax_matrix(15, 15))

"""
РЕЗУЛЬТАТ 1:
minimax_matrix(5, 5)
576 bytes used
minimax_matrix(15,15)
704 bytes used
"""

'''
lesson3 task 9 - после устранения промежуточных переменных и превращения матрицы в кортеж
'''


def minimax_matrix1(cols, rows, arr_spread):
    matrix = tuple([tuple([randint(1, arr_spread) for i in range(rows)]) for j in range(cols)])
    max_, min_ = 0, arr_spread
    for i in range(cols):
        for j in range(rows):
            if matrix[j][i] < min_:
                min_ = matrix[j][i]
        if max_ < min_:
            max_ = min_
    for i in matrix:
        for j in i:
            print(f"{j:<4}", end='')
        print('')

    print(sum([sys.getsizeof(k) for k in [matrix, max_, min_, cols, rows, arr_spread, i, j]]), 'bytes used')
    return (max_)


print(minimax_matrix1(15, 15, 100))

"""
РЕЗУЛЬТАТ 2:
minimax_matrix1(5,5,100)
328 bytes used
minimax_matrix1(15, 15, 100)
488 bytes used

итого выигрыш в 43 % занимаемой памяти для матрицы 5х5 и в 30% для матрицы 15х15

"""

"""
На уровне измерения места, занимаемого переменной, оптимизация по памяти сводится в устранении промежуточных
переменных и выборе минимально ресурсоёмких структур данных - как здесь, например, в оптимизированном варианте
выбран кортеж кортежей вместо списка списков. Более сложную оптимизацию имеет смысл делать уже профайлерами. 
"""
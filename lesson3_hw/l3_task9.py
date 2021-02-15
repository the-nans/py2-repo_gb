"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint # для ленивый
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
    return(max_)


"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint # для ленивый
cols = 5
rows = 5
arr_spread = 100
spam, res = [], []
ex = arr_spread
matrix = [[randint(1, arr_spread) for i in range(rows)] for k in range(cols)]
for line in matrix:
    for item in line:
        print(f"{item:<4}", end='')
    print()
# =================================
# for i in range(cols):
#     for line in matrix:
#         spam.append(line[i])
#     for j in spam:
#         ex = j if j < ex else ex
#     res.append(ex)
#     spam.clear()
#     ex = arr_spread
# ex = 0
# print(f'Column minimums are {res}')
# for i in res:
#     ex = i if i > ex else ex
# print(f'Max element of column minimums is {ex}')

# ==================================
max_ = 0
for i in range(cols):
    min_ = matrix[0][i]
    for j in range(rows):
        if matrix[j][i] < min_:
            min_ = matrix[j][i]
    if max_ < min_:
        max_ = min_
print(max_)
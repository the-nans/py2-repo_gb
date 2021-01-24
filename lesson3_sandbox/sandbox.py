# def to_camel_case(text: str):
#     q = text[0] + text.replace("-", "_").replace("_", " ").title().replace(" ", "")[1::]
#     return q
#
# print(to_camel_case('the_stealth_warrior'))
# def eratosphen(n: int):
#     numbers = list(range(n+1))
#     numbers[1] = 0
#     for i in numbers:
#         if numbers[i] != 0:
#             j = i*2
#             while j < n:
#                 numbers[j] = 0
#                 j += i
#     result = [i for i in numbers if i != 0]
#     return result
#
# def solve(a,b):
#     q = range(a,b)
#
"""
подсчёт суммы строк и столбцов матрицы
"""
from random import randint
matrix = [[randint(0,10) for _ in range(5)] for _ in range(5)]
for line in matrix:
    for item in line:
        print(f"{item:<4}", end='')
    print()
#
#
# sum_column = [0] * len(matrix[1])
# for line in matrix:
#     sum_line = 0
#     for i, item in enumerate(line):
#         sum_line += item
#         sum_column[i] += item
#         print(f"{item:<4}", end='')
#     print(f"   |{sum_line}")
print('-' * len(matrix) * 5)
# for s in sum_column:
#     print(f"{s:<4}", end='')
"""
обмен главных диагоналей матрицы
"""
for i, lines in enumerate(matrix):
    lines[i], lines[-i-1] = lines[-i-1], lines[i]

for line in matrix:
    for item in line:
        print(f"{item:<4}", end='')
    print()
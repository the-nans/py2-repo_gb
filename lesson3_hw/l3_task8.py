"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
# from random import randint # для ленивый
matrix = [[0 for i in range(5)] for k in range(4)]
for i in range(4):
    summ = 0
    for j in range(4):
        # matrix[i][j] = randint(1,10) # для ленивых
        matrix[i][j] =  int(input("Enter next element: "))
        summ += matrix[i][j]
    matrix[i][len(matrix[i])-1] = summ

for line in matrix:
    for item in line:
        print(f"{item:<4}", end='')
    print()
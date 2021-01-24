"""
 В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import randint
arr_spread = 10
arr_size = 10
arr = [randint(-1*arr_spread, arr_spread) for _ in range(arr_size)]
max_neg = arr_spread
for i in arr:
    if i < 0 and abs(max_neg) > abs(i):
        max_neg = i
print(arr)
print(max_neg)
print(arr.index(max_neg))
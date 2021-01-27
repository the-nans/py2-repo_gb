"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint
arr_spread = 100
arr_size = 4
arr = [randint(1, arr_spread) for _ in range(arr_size)]
print(arr)
m, k = 0, 0
for i in range(len(arr)):
    m = i if m < arr[i] else m
    k = i if k > arr[i] else k
arr[m], arr[k] = arr[k], arr[m]
print(arr)

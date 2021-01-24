"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint
arr_spread = 100
arr_size = 20
arr = [randint(1, arr_spread) for _ in range(arr_size)]
print(arr)
m, k = 0, arr[0]
for i in arr:
    m = i if m < i else m
    k = i if k > i else k
arr[arr.index(m)], arr[arr.index(k)] = arr[arr.index(k)], arr[arr.index(m)]
print(arr)

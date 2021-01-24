"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба минимальны), так и различаться.
"""
from random import randint
arr_spread = 100
arr_size = 10
arr = [randint(1, arr_spread) for _ in range(arr_size)]
print(arr)
for _ in range(2):
    m1 = arr_spread
    for i in arr:
        m1 = i if m1 > i else m1
    print(arr.pop(arr.index(m1)))

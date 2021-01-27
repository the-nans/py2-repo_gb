"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint
arr_spread = 10
arr_size = 10
arr = [randint(1, arr_spread) for _ in range(arr_size)]
print(arr)
lim1, lim2 = 0, arr_spread+1
lower_index, upper_index = 0, 0
for i in arr:
    lim1 = i if lim1 < i else lim1
    lim2 = i if lim2 > i else lim2
lower_index, upper_index = (arr.index(lim2), arr.index(lim1)) if arr.index(lim1) > arr.index(lim2) \
    else (arr.index(lim1), arr.index(lim2))
if lower_index == upper_index-1:
    print(f"Max and min elements are ajdacent({lower_index} and {upper_index}), sum will be zero")
else:
    summ = 0
    for j in arr[lower_index+1:upper_index]:
        summ += j
    print(f'Summ of elements between arr[{lower_index}] and arr[{upper_index}] = {summ}')

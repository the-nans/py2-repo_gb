"""
Определить, какое число в массиве встречается чаще всего.
"""
from random import randint
arr = [randint(0, 10) for _ in range(10)]
res = {i: arr.count(i) for i in list(set(arr))}
max_repeat = -1
repeated_num = [-1, ]
for x, y in res.items():
    if y > max_repeat:
        repeated_num.clear()
        repeated_num.append(x)
        max_repeat = y
    elif y == max_repeat:
        repeated_num.append(x)

print(arr)
print(f'Наибольшая встречаемость - {max_repeat} у {repeated_num}')

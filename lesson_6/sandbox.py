from collections import deque
import copy

dict_16 = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

x = list(input('Введите первое шестнадцатеричное чисело: '))
y = list(input('Введите второе шестнадцатеричное чисело: '))

#Подставляю нули в списки, чтобы удобнее было считать
if len(x) < len(y):
    div = len(y) - len(x)
    for i in range(div):
        x.insert(0, 0)
else:
    div = len(x) - len(y)
    for i in range(div):
        y.insert(0, 0)
x.insert(0, 0)
y.insert(0, 0)
print(x, y, sep='\n')
x = deque(x, maxlen=len(x))
copy_x = copy.copy(x)
y = deque(y, maxlen=len(y))
copy_y = copy.copy(y)

# Буквы в числа
for el in x:
    if el in dict_16.keys():
        copy_x.append(dict_16[el])
    else:
        copy_x.append(int(el))
for el in y:
    if el in dict_16.keys():
        copy_y.append(dict_16[el])
    else:
        copy_y.append(int(el))
print(copy_x, copy_y, sep='\n')

# Сложение
c = list(map(int, list('0' * (len(x)))))
i = len(copy_x) - 1

while i >= 0:
    ad = copy_x[i] + copy_y[i]
    if ad > 15:
        div = abs(ad - 16)
        c[i - 1] += 1
        c[i] += div
    else:
        c[i] += copy_x[i] + copy_y[i]
    i -= 1
print(c)
if c[0] == 0:
    del c[0]

# Перевод в шестнадцатеричное чисело
for el in c:
    for key, value in dict_16.items():
        if el == value:
            c[c.index(el)] = key
print(c)
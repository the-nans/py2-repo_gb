"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15,
6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно
в этих позициях первого массива стоят четные числа.
"""
arr1 = [int(k) for k in input("Введите набор целых чисел, разделённых пробелами: ").split()]
arr2 = []
for i in arr1:
    if i % 2 == 0:
        arr2.append(arr1.index(i))
        arr1[arr1.index(i)] = -1
print(arr2)

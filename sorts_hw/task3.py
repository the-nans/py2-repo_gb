"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
from random import shuffle, randint, choice
from functools import reduce


def median(arr):
    """
    функция работает только для массива без повторений. Не годится для реальных данных
    :param arr: set, притворяющийся массивом
    :return:
    """

    for i in arr:
        x, y = 0, 0
        for j in arr:
            if j <= i and x <= len(arr) // 2 and y <= len(arr) // 2:
                x += 1
            elif j >= i and x <= len(arr) // 2 and y <= len(arr) // 2:
                y += 1
        if x == y:
            return i


"""
===================
"""


def silly_median(l):
    """
    Очень топорная функция поиска медианы, перебирает вообще все элементы массива.
    Могла бы быть поразборчивее
    :param l: массив
    :return:
    """
    for i in l:
        lows = [el for el in l if el < i]
        highs = [el for el in l if el > i]
        pivots = [el for el in l if el == i]

        # print(lows, pivots, highs)                # наглядное представление логики программы
        # print(abs(len(lows) - len(highs)), len(pivots))
        if abs(len(lows) - len(highs)) < len(pivots):
            return i
    return False

"""
------------------------
"""
def better_median(l=[]):
    """
    Очевидно, что если массив элементов больших и меньших выбранного равны друг другу, мы нашли медиану
    В прочих случаях, если медиану мы не нашли, эти два массива точно разного размера.
    При этом медиана всегда находится в бОльшем массиве, потому что такой массив содержит саму медиану и ту ВСЮ
    ПОЛОВИНУ исходного массива, которая меньше/больше медианы.
    Соответственно, как бы мы ни выбрали исходное i, далее поиск имеет смысл сужать в сторону
    бОльшей части обрабатываемого массива.
    :param l:
    :return:
    """
    i = l[-1]
    while True:
        lows = [el for el in l if el < i]
        highs = [el for el in l if el > i]
        pivots = [el for el in l if el == i]

        # print(lows, pivots, highs)                # наглядное представление логики программы
        # print(abs(len(lows) - len(highs)), len(pivots))

        if abs(len(lows) - len(highs)) < len(pivots):
            return i
        else:
            i = list(set(lows))[-1] if len(lows) > len(highs) else list(set(highs))[0]


"""
*******************
"""
import cProfile
spread = 3000

ar = [randint(0, spread) for i in range(0, spread * 2 + 1)]
# print(ar)

cProfile.run('silly_median(ar)')
cProfile.run('better_median(ar)')

"""
Воркбенчить это задачка для терпеливых, ибо рандом велик. Но всё же better_median должна отрабатывать получше,
в силу хоть какого-то отсева ненужных значений
"""
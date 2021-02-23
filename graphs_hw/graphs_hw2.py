'''
 Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
 которые необходимо обойти.
'''
from collections import deque

def deixtra(graph, start):
    length = len(graph)  # длина графа
    is_visited = [False] * length  # соотношение вершина - посещённость
    cost = [float('inf')] * length  # цена пути до каждой вершины
    parent = [-1] * length  # через какую вершину куда попали
    path = {x: deque() for x in range(length)}  # полные пути до каждой вершины
    path[start].append(-1)
    cost[start] = 0  # цена достижения вершины, от которой идём в этой итерации
    min_cost = 0  # переменная для остановки цикла

    while min_cost < float('inf'):
        is_visited[start] = True  # делаем текущую вершину посещённой
        for i, next_vertex in enumerate(graph[start]):  # начинаем цикл по её соседям
            if next_vertex != 0 and not is_visited[i]:  # если сосед ещё не посещён и к нему есть ребро
                if cost[i] > next_vertex + cost[start]:  # проверяем - не нашли ли мы путь подешевле
                    cost[i] = next_vertex + cost[start]  # если "да" - обновляем значение стоимости пути
                    parent[i] = start  # и пишем текущую вершину родительской для соседа
        min_cost = float('inf')  # пробуем завершить цикл
        for i in range(length):  # обходим все вершины графа
            if min_cost > cost[i] and not is_visited[i]:  # хоть одна непосещённая и с небесконечной ценой
                min_cost = cost[i]  # делаем новый обход цикла
                start = i  # начиная с неё

    for i in range(length):
        j=i
        while j != -1:
            if parent[j] != -1:
                path[i].appendleft(parent[j])
            j = parent[j]
        if path[i] and path[i] != deque([-1]):
            path[i].append(i)

    print(path)

    print(parent)
    return cost


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

print(deixtra(g, 0))

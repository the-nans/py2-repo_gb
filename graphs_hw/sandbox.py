"""
Поиск в ширину по невзвешенному графу

1. Добавить в очередь вершину
2. Если вершина нужная - ура, мы её нашли.
2.1. если нет - добавить в очередь всех её соседей
3. Если очередь пуста - наши полномочия всё
"""
from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True
    while len(deq) > 0:
        current = deq.pop()

        if current == finish:
            # return parent
            break
        for i, vertex in enumerate(graph[current]):

            if vertex == 1 and not is_visited[i]:

                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)

    else:
        print(f"Нет пути из {start} в {finish}")
    print(parent)
    print(is_visited)
    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]
    cost += 1
    way.appendleft(start)
    return way, cost

print(bfs(g, 0,5))

'''
Алгоритм Дейкстры
1. Выбрать начальную вершину
2. Путь до остальных вершин предположить бесконечным
3. Вычислить пути до соседей выбранной вершины:
3.1 выбрать вершину-соседа 
3.2 вычислить путь до неё
3.3 если вычисленный путь короче существующего - предыдущий путь забыть, а этот запомнить

'''

g = [
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0]
]

def deixtra(graph, start):
    length = len(graph)
    is_visited = [False]*length
    cost = [float('inf')]*length
    parent = [-1]*length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    print(parent)
    return cost



s = 0

print(deixtra(g, s))
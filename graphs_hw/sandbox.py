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


#
# s = 0
#
# print(deixtra(g, s))

'''
Поиск в глубину - код препода. Он прикольный и я решила его сохранить
'''

def dfs(graph, start):
    path = []
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    def _dfs(vertex):
        is_visited[vertex] = True
        path.append(vertex)

        for item in graph(vertex):
            if not is_visited[item]:
                parent[item] = vertex
                _dfs(item)
                path.append(vertex)
        else:
            path.append(-vertex)
    _dfs(start)

    return parent, path

'''
домашки
'''
def dijkstra(graph, start):
    #----------------------------------------ДЗ ON
    def get_parents(i, parents):
        if parents[i] == -1:
            return []

        else:
            return get_parents(parents[i], parents) + [parents[i]]


    #----------------------------------------
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = [float('inf')] * lenght
    parent = [-1] * lenght

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost= float('inf')
        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    #----------------------------------------
    ways = {i: get_parents(i, parent) + [i] if cost[i] != float('inf') else None for i in range(lenght)}

    return cost, ways


# s = int(input('От какой вершины идти:  '))
# c, w = dijkstra(g, s)
#
# print(f'Путь от вершины {s}: ')
# for i in range(len(g)):
#     if i != s:
#         if c[i] == float('inf'):
#             print(f' - до вершины {i}: маршрута нет')
#             continue
#         print(f' - до вершины {i}: стоимость {c[i]}, маршрут: {w[i]}')

'''
 ^ 
/|\
 |
прикольный алг, сделан by Vol4oks 
'''
"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random
from collections import deque


def create_graph(num):
    g_lst = {}  # здесь будет наш список смежности
    v_lst = [None] * num  # здесь будем накапливать список вершин, с которыми есть связь
    d = deque([el for el in range(num)])  # создадим очередь, по ней мы будем генерить связи

    for i in range(num):  # организуем цикл создания связей для каждой вершины
        n = random.randint(1, num - 1)  # узнаем сколько связей имеет данная вершина
        v_lst[i] = set()  # создаем пустое множество для заполнения списком вершин

        k = 0
        while k < n or len(v_lst[i]) == 0:  # узнаем, с какими вершинами связана данная
            vertex = random.choice(list(d)[1:])  # случайно выберем вершину для связи из очереди, исключая саму себя
            one_way = random.choice([True, False])  # зададим тип связи - односторонняя или двусторонняя
            if vertex > i:
                v_lst[i].add(vertex)  # если вершина (vertex) больше текущей, добавляем в список связи без вопросов
            elif i not in g_lst[vertex]:
                v_lst[i].add(vertex)  # для вершин, меньше текущей, при отсутствии связи - добавляем в список
            elif not one_way:
                v_lst[i].add(vertex)  # если связь уже есть, проверяем тип связи, если односторонняя - пропускаем
            elif one_way:
                    print(f'One way: вершины {i} и {vertex}. one way = {one_way}')
            k += 1

        g_lst[i] = v_lst[i]  # заполняем список смежности
        d.rotate(-1)
    return g_lst

"""
Алгоритм "Поиск в глубину"
1. Начинаем обход с точки старта. 
2. Помещаем точку старта в список посещенных
3. Обходим в цикле все смежные вершины, исключая посещенные
4. Для каждого эелемента в цикле рекурсивно повторяем шаги 1 - 3, помещая в точку старта данные элемент
"""


def dfs(graph, start, visited=None):  # функция вернет список доступных вершин из точки старта
    if visited is None:
        visited = set()
    visited.add(start)  # добавляем вершину в посещенные
    for next in graph[start] - visited:  # рассматриваем только не посещенные элементы
        dfs(graph, next, visited)  # помещаем в точку старта рассматриваемый элемент, и рекурсивно вызываем функцию
        # поиска
    return visited


n = int(input('Задайте количество вершин: '))
g = create_graph(n)
print('*' * 50)
print(f'Наш ориентированный граф с количеством вершин {n}: ')
for k, v in g.items():
    print(f'{k}: {v}')

print('*' * 50)
# visited = dfs(g, 1)
print()
for i in range(n):
    print(f'Список доступных вершин из вершины {i}: {dfs(g, i)}')
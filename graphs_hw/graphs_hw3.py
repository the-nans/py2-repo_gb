"""
Написать программу, которая обходит невзвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
from random import choices, randint


def dograph(n):
    """
    Генератор ориентированного графа, в котором все вершины связаны - т.е. нет изолированных вершин, и нет петель -
    т.е. ни одна дуга не ведёт в ту же вершину, из которой выходит.

    Проще всего сделать связным граф, задав условие, чтобы у каждой вершины была хотя бы  одна дуга.
    :param n: int
    :return: {vertex1 : [edge1, edge2...], vertex2 : [edge...], .. vertexN [edgeM, edgeK..] }
    """
    g = {x: [randint(0, n - 1) for _ in range(randint(1, n // 3))] for x in range(0, n)}
    for i in range(n):
        if i in g[i]:
            g[i].remove(i)
        g[i] = list(set(g[i]))
    return g


def walk_dfs_colors(graph, vertex, has_color):
    """
    Рекурсивный обходчик графа по методу поиска в глубину - Depth-First-Search
    Отвечает на вопрос "все ли вершины достижимы?"
    :param graph: {vertex1 : [edge1, edge2...], vertex2 : [edge...], .. vertexN [edgeM, edgeK..] }
    :param vertex: int
    :param has_color: white or black
    :return: has_color = ['w', 'w', 'b'... 'w'] - 'w' - для недостижимых вершин, 'b' - для достижимых
    """
    if has_color[vertex] == 'b':  # если вершина уже посещена
        return has_color  # возвращаем топологию
    else:
        has_color[vertex] = 'b'  # помечаем вершину как посещённую
        for i in graph[vertex]:  # берём всех её соседей

            if has_color[i] == 'w':  # если вершина не посещена
                has_color = walk_dfs_colors(graph, i, has_color)  # посещаем и обновляем топологию
    return has_color


def vertex_check(graph, point1, point2):
    """
    Проверить, существует ли путь до вершины
    :param graph:
    :param point:
    :return:
    """
    colors = ['w' for _ in range(len(graph))]
    path = walk_dfs_colors(graph, point1, colors)
    if path[point2] == 'b':
        return True
    return False


def walk_dfs(graph, vertex, has_color=None, path=[]):
    """
    Рекурсивный обходчик графа по методу поиска в глубину - Depth-First-Search
    Возвращает все вершины, доступные из vertex в порядке обнаружения
    :param graph - {v1 : [e1, .., en], .. , vm : [e1m, .. ekm]}
    :param vertex - int
    """
    if has_color is None:
        has_color = ['w' for _ in range(len(graph))]
        path.append(vertex)

    if has_color[vertex].isdecimal():  # если вершина уже посещена
        # path.append(int(has_color[vertex]))
        return path  # возвращаем топологию
    else:
        # помечаем вершину как посещённую
        for i in graph[vertex]:  # берём всех её соседей
            has_color[vertex] = str(i)  # пишем в вершину, куда из неё пошли

            if has_color[i] == 'w':  # если вершина не посещена
                path.append(i)
                path = walk_dfs(graph, i, has_color, path)  # посещаем и обновляем топологию
    return path


n = 10

g1 = dograph(n)

print('Работаем с таким вот графом: \n', g1)

print('Достижимость его вершин из нулевой точки: w - недостижима, b - достижима: \n',
      walk_dfs_colors(g1, 0, ['w' for _ in range(0, len(g1))]))

k = int(input("Введите точку, для которой мы хотим узнать все достижимые узлы графа:"))

print(f'Посмотрим порядок обнаружения вершин в графе из точки {k} \n', walk_dfs(g1, 3))

k1 = [int(x) for x in input('Введите через пробел пару точек. Проверим можно ли из первой добраться во вторую: ')
    .split(' ')]

print(f'Достижимость вершины {k1[1]} из {k1[0]}: \n', vertex_check(g1, k1[0], k1[1]))

def friends(n: int):
    """
    1. создать строчку матрицы смежности для друга №n, заполнить нулями
    2. заполнять единицами только элементы строки, большие n
    3. посчитать количество единиц в матрице

    :param n:
    :return:
    """
    g = [[0 for _ in range(n)] for __ in range(n)]
    handshakes = 0
    for i in range(n):
        for j in range(i):
            g[i][j] = 1
            handshakes += 1
        print(g[i])
    return handshakes

n = int(input('Сколько вас там? '))
print(f'Всего {friends(n)} рукопожатий для {n} друзей')

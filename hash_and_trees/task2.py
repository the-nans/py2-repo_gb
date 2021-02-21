"""
Закодировать любую строку по алгоритму Хаффмана
"""

"""
Алгоритм Хаффмана - теория 

Самый редкий символ в последовательности самый большой код
самый частый - самый короткий код

1. посчитать вхождение символов в строку
2. создать листья бин. дерева для каждого знака и добавить в очередь,
указав частоту в качестве приоритета, по возрастанию
3. делаем дерево
3.1. два левых узла объединяем в новый, его приоритет - сумма 
двух исходных, они теперь его потомки
3.2. заново сортируем очередь по возрастанию
3.3. берём следующие два крайних левых узла и делаем 3.1. 

В дереве Хаффмана буквы хранятся в листьях, а не в узлах!

4. Обходим дерево по алгоритму бинарного поиска, получаем для каждого
символа цепочку нулей(шаг влево) и единиц(шаг вправо). Закодировали.

Код символа не может оказываться _префиксом_ кода другого символа, 
иначе возникнет конфликт
"""
from collections import deque
class Node:
    # как нас и просили - не трогаем модуль bstree
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def haffman(s):
    """
    Кодируем фразу по алгоритму Хаффмана
    :param s: - строка
    :return: - тоже строку
    """
    def haffmantree(q1: deque):
        """
        Принимаем на вход очередь символов, на выход выдаем дерево
        :param q1:
        :return:
        """
        if len(q1) == 1:
            return q1[0]
        spam1 = q1.popleft()
        spam2 = q1.popleft()
        new_node = Node((spam1.data[0]+spam2.data[0], spam1.data[1]+spam2.data[1]), spam1, spam2)
        q1.appendleft(new_node)
        q1 = deque(sorted(q1, key=lambda x: x.data[1]))
        return haffmantree(q1)

    def walk_tree(b_tree: Node, letter: str, path=''):
        """
        проверить, буква в дате первая?
        если есть - оторвать букву из даты и идти налево
        если нет - идти направо
        :param b_tree: data = ('oprsat', 25) left(data('opr', 11)) right(data('sat', 14)))
        :param letter = 'a'
        :param path:
        :return:
        """
        if not b_tree.left and not b_tree.right:
            encoded[letter] = path
        else:
            if letter in b_tree.left.data[0]:
                path = f'{path}0'
                tree = b_tree.left
                walk_tree(tree, letter, path)
            elif letter in b_tree.right.data[0]:
                path = f'{path}1'
                tree = b_tree.right
                walk_tree(tree, letter, path)

    letters = {x: s.count(x) for x in s}  # частота вхождений символов
    letters = sorted(letters.items(), key=lambda letters: letters[1])
    print(letters)
    queue = deque()
    for i in letters:
        queue.append(Node(i, None, None))
    tree = haffmantree(queue)
    encoded = {x: '' for x in s}
    for i in encoded.keys():
        walk_tree(tree, i)
    rez = ''
    for i in list(s):
        rez = f'{rez} {encoded[i]}'

    return rez

# s = input('Введите строку, которую будем кодировать: ')
s = 'satoporepotenetoperarotas'
print(f'Закодировали, теперь это выглядит так: {haffman(s)}')

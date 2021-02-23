from binarytree import tree, bst, Node, build


class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = tree(4, is_perfect=False)
# print(a)

b = bst(height=3, is_perfect=True)
# print(b)

c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
# print(c)

d = build([7, 3, 11, 1, 5, 9, 13, None, 2, 4])
# print(d)

"""
Бинарный поиск
"""

from binarytree import bst


def bintree(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return (f'Needle {number} found in {path} {number}')
    else:
        path = f'{path} {str(bin_search_tree.value)}'
        if number < bin_search_tree.value and bin_search_tree.left is not None:
            return bintree(bin_search_tree.left, number, path)
        elif number > bin_search_tree.value and bin_search_tree.left is not None:
            return bintree(bin_search_tree.right, number, path)
    return 'Lolwut?'


bt = bst(height=5, is_perfect=True)
print(bt)
# needle = int(input('Enter int needle: '))
# print(bintree(bt, needle))

"""
Алгоритм Хаффмана - теория 

Самый редкий символ в последовательности самый большой код
самый часты - самый короткий код

1. посчитать вхождение символов в строку
2. создать узлы бин. дерева для каждого знака и добавить в очередь,
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

'''
Хэш-функции
'''
h_list = [None] * 26


def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)


a = 'carrot'
my_append(a)


def my_index(value):
    letter = 26
    index = 0
    size = 10000
    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i
    return (index % size)


print(my_index('apricot'))
print(my_index('apple'))

import hashlib

print(hashlib.sha1(b'SecretWordKnownBy' + b'Hello').hexdigest())
"""
sha-1

псевдокод
"""


def sha(data):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    length = len(data)
    data = data << 1 + 1
    if len(data) % 521 > 448:
        data = data << 64

    data = data << (448 - len(data) % 512)
    data = data << 64 + length

    for part_512 in data:
        w = []
        for i in range(16):
            w[i] = part_512[:32]
            part_512 = part_512[32:]
        for i in range(16, 80):
            w[i] = (w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]) << 1

        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = (a << 5) + f + e + k + w[i]
            e = d
            d = c
            c = b << 30
            b = a
            a = temp
        h0, h1, h2, h3, h4 = h0 + a, h1 + b, h2 + c, h3 + d, h4 + e
    hash = f'{h0}{h1}{h2}{h3}{h4}'
    return hash

"""
практика
"""

def is_eq( a: str, b:str, verbose = False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'кто-то пуст'
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
    if verbose:
        print(ha)
        print(hb)
    return ha == hb

print(is_eq('aaa', 'bbb', True))

"""
Поиск подстроки в строке, алг. Рабина-Карпа
"""

def Rabin_Karp(st: str, subs: str) -> int:
    assert len(st) > 0 and len(subs) > 0, 'Кто-то пуст'
    assert len(subs) <= len(st), 'Подстрока должна быть короче или равна строке'

    len_subs = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(st) - len_subs + 1):
        if h_subs == hashlib.sha1(st[i:i+len_subs].encode('utf-8')).hexdigest():

            if st[i:i+len_subs] == subs:
                return i
    return -1

#
# haystack = "Hello world"
# needle = 'wo'
# print(Rabin_Karp(haystack, needle))


class TreeNode:
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None


def two_minimal_numbers_array(array):
    first_min = second_min = None
    maximum = max(array)

    for index, number in enumerate(array):
        if number <= maximum:
            maximum = number
            first_min = (number, index)

    maximum = max(array)
    for index, number in enumerate(array):
        if index != first_min[1]:
            if number <= maximum:
                maximum = number
                second_min = (number, index)

    return first_min, second_min


def create_bin_codes(main_node, bin_codes, code):
    if main_node.has_left_child():
        code += "0"
        if isinstance(main_node.left_child, str):
            bin_codes[main_node.left_child] = code
            code = code[:-1]
        else:
            create_bin_codes(main_node.left_child, bin_codes, code)
            code = code[:-1]

    if main_node.has_right_child():
        code += "1"
        if isinstance(main_node.right_child, str):
            bin_codes[main_node.right_child] = code
            code = code[:-1]
        else:
            create_bin_codes(main_node.right_child, bin_codes, code)
            code = code[:-1]


def huffman_encode(source: str) -> str:
    letters = {}
    frequency = []

    for i in source:
        if not letters.get(i):
            letters[i] = 0
        letters[i] = letters[i] + 1

    for i in letters:
        frequency.append(letters[i])

    for i in range(len(letters)-1):
        minimals = two_minimal_numbers_array(frequency)
        key_first = list(letters.keys())[minimals[0][1]]
        key_second = list(letters.keys())[minimals[1][1]]
        node_key = key_first + key_second

        frequency.remove(minimals[0][0])
        frequency.remove(minimals[1][0])
        frequency.append(minimals[0][0] + minimals[1][0])

        if len(key_first) > 1 and len(key_second) > 1:
           letters[node_key] = TreeNode(0, node_key, letters[key_first], letters[key_second])
        elif len(key_first) > 1:
           letters[node_key] = TreeNode(0, node_key, letters[key_first], key_second)
        elif len(key_second) > 1:
           letters[node_key] = TreeNode(0, node_key, key_first, letters[key_second])
        else:
           letters[node_key] = TreeNode(0, node_key, key_first, key_second)

        letters.pop(key_first)
        letters.pop(key_second)

    final_tree = letters[next(iter(letters))]

    del frequency, letters

    bin_codes = {}
    code = ""
    create_bin_codes(final_tree, bin_codes, code)

    del final_tree, code

    final_bin_string = ""
    for letter in source:
        final_bin_string += f'{bin_codes[letter]} '

    return final_bin_string


print(huffman_encode('satororepotenetoperarotas'))
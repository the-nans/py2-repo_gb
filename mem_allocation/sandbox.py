# import sys
# l = (3, 12.3, 'Hello, world!', 55555)
# a = 5
# b = 12
# c = 'Hellp'
# s = set(l)
# d = {2:1, 4: 3, 62:1, 42: 3, '2':1, '4': 3, '33':1, 11: 3, 22:1, 12: 3, 0:1, 8: 3, 5:1, 6: 3,}
# def sh_size(x, level=0):
#     print('\t'*level, f"{x.__class__} size = {sys.getsizeof(x):>5} obj = {x}")
#
#     if hasattr(x, '__iter__'):
#         if hasattr(x, 'items'):
#             for xx in x.items():
#                 sh_size(xx, level+1)
#         elif not isinstance(x, str):
#             for xx in x:
#                 sh_size(xx, level+1)
#
# sh_size(a)
# sh_size(b)
# sh_size(d)
#
# '''
# id
# '''
# import ctypes, struct
# print(id(b))
# print(sys.getsizeof(b))
# print(id(int))
# print(struct.unpack('LLLi', ctypes.string_at(id(b), sys.getsizeof(b))))


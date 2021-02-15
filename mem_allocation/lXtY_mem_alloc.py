import collections
from functools import reduce
import sys, struct, ctypes


def sh_size(x, level=0):
    print('\t' * level, f"{x.__class__} size = {sys.getsizeof(x):>5} obj = {x}")

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                sh_size(xx, level + 1)
        elif hasattr(x, '_fields'):
            for xx in x._fields:
                sh_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                sh_size(xx, level + 1)



company_amount = int(input('Enter amount of companies: '))
company = collections.namedtuple('Company', ['name', 'profit_1qt', 'profit_qt', 'profit_3qt', 'profit_4qt', 'year'])
sep = collections.deque('|')
spam = []
companies = []
for i in range(0, company_amount):

    for j in company._fields[:-1:]:
        spam.append(input(f'Enter company {j}: '))

    spam.append(reduce(lambda x, y: int(x) + int(y), spam[1::]))
    companies.append(company(*spam))
    spam.clear()

avg_year = reduce(lambda x, y: x + y.year, [0, *companies]) / len(companies)

for i in companies:
    if i.year <= avg_year:
        sep.appendleft(i)
    else:
        sep.append(i)

print(sep)
print(sum([sys.getsizeof(i) for i in [company, company_amount, sep, spam, companies, avg_year]]), 'bytes used')

'''
print(sum([sys.getsizeof(i) for i in [company, company_amount, sep, spam, companies, avg_year]]))
1716 bytes used

sh_size(company)

 <class 'type'> size =   896 obj = <class '__main__.Company'>
	 <class 'str'> size =    53 obj = name
	 <class 'str'> size =    59 obj = profit_1qt
	 <class 'str'> size =    58 obj = profit_qt
	 <class 'str'> size =    59 obj = profit_3qt
	 <class 'str'> size =    59 obj = profit_4qt
	 <class 'str'> size =    53 obj = year

'''

"""
давайте попробуем не выпендриваться с удобными структурами данных
"""
#
# company_amount = int(input('Enter amount of companies: '))
#
#
# class Company:
#
#     def __init__(self, name, q1, q2, q3, q4):
#         self.profit_year = (q1 + q2 + q3 + q4)
#         self.name = name
#
#
# companies = []
# i, avg = 0, 0
# while i < company_amount:
#     companies.append(Company(input('Enter company name'),
#                              int(input('1st quarter profit')),
#                              int(input('2nd quarter profit')),
#                              int(input('3d quarter profit')),
#                              int(input('4d quarter profit'))))
#     i += 1
#     avg += companies[-1].profit_year / company_amount
# print('less than avg            more than avg')
# for i in companies:
#     if i.profit_year > avg:
#         print(f'{i.name:>40}')
#     else:
#         print(f'{i.name}')
#
# print(sum([sys.getsizeof(i) for i in [companies, i, avg, company_amount, Company]]), 'bytes used')

"""
для того же объёма данных:
print(sum([sys.getsizeof(i) for i in [companies, i, avg, company_amount, Company]]), 'bytes used')
1252 bytes used 
"""

"""
Вывод - удобные структуры данных, улучшающие читабельность кода, имеет смысл придирчиво проверять на прожорливость 
в плане памяти
"""
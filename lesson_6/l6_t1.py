import collections
from functools import reduce

"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого 
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования 
предприятий, чья прибыль выше среднего и ниже среднего.
"""

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

avg_year = reduce(lambda x, y: x + y.year, [0, *companies])/len(companies)

for i in companies:
    if i.year <= avg_year:
        sep.appendleft(i)
    else:
        sep.append(i)

print(sep)
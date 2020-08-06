# code for python3
from itertools import groupby

lst = [1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 9, 9, 10, 20, 99, 99, 99, 100, 100]
dic = {}

for k, g in groupby(lst, key=lambda x: (x - 1) // 10):
    dic['{}-{}'.format(k * 10 + 1, (k + 1) * 10)] = len(list(g))

print(dic)

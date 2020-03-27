import random

l = [random.randint(1, 100) for i in range(10)]
d = dict()
for num in l:
    d[num] = d.get(num, 0) + 1
for k, v in d.items():
    print(k, v, sep=",")
    print("helll")

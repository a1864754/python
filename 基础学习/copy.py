import copy

a = [1, 2, 3, 4, [0, 0, 0]]
b = a.copy()
c = copy.deepcopy(a)
print(c)

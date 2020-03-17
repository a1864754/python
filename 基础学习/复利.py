import copy

sum1 = 1000
day = 1
while day <= 365:
    if day % 30 == 0:
        sum1 += 500
    sum = sum1 * (1 + 2.78 / 100)
    day += 1
print("结果为: ", sum1)
print("")
one = [1, 2, 3]
two = copy.deepcopy(one)
print(two)

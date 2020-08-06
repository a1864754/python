"""
2. 编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果。
"""
import random

a = [random.randint(0, 10) for i in range(20)]
print("原列表为: ", a)
b = a[:10]
c = a[10:]
print(b)
print(c)
b.sort()
c.sort(reverse=True)
print(b + c)

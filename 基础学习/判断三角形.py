"""编写一个程序，检查用户输入3条边能否构成三角形，如果可以构成，请判断三
角形的类型（锐角、钝角和直角以及等腰、等边）。
"""
bian = input("请输入三条边的长度,以空格为间隔: ").split()
a, b, c = map(float, bian)
print("三边长度分别为:%.2f  %.2f  %.2f" % (a, b, c))
if (a + b > c) and (a + c > b) and (b + c > a):  # 判断是否是三角形
    if a == b == c:
        print("这是一个等边三角形")
    elif (a == b or a == c or b == c):
        print("这是一个等腰三角形")
    elif (a * a + b * b == c * c) or (a * a + b * b == c * c) or (a * a + b * b == c * c):
        print("这是一个直角三角形")
    else:
        print("这是一个不规则三角形")
else:
    print("不是三角形")

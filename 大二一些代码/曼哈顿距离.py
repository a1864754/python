def hmd(x, y):
    return sum(map(lambda i, j: abs(i - j), x, y))


x = list(map(int, input("请输入第一个坐标(空格为间隔符): ").split()))
y = list(map(int, input("请输入第二个坐标(空格为间隔符): ").split()))
num = hmd(x, y)
print("{0}到{1}距离为: {2}".format(x, y, num))

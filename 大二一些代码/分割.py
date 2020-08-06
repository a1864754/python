"""
课后作业:
编写程序,用户输入一个列表和2个整数作为下标,
然后输入列表中介于2个下标这之间的元素组成的字列表.
例如用户输入[10,20,30,40,50]和2、4程序输出[30,40,50]
"""
one = input("请输入一个列表(以空格为间隔): ").split()
one = list(map(int, one))
print("您输入的列表为: ", one)
start = int(input("请输入开始的列表下标(按回车结束): "))
end = int(input("请输入结束的列表下标(按回车结束): "))

two = []
i = 0
while i < len(one):
    if start <= i <= end:
        two.append(one[i])
    i += 1
print("指定范围内的列表为: ", two)

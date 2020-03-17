import copy

one = input("请输入一个列表(以空格为间隔): ").split()
one = list(map(int, one))
print(one)
start = int(input("请输入开始的列表下标(按回车结束): "))
end = int(input("请输入结束的列表下标(按回车结束): "))

two = copy.deepcopy(one)

print(one)
print(o)

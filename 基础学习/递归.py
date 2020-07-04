"""有一个数列，形式为1 1 1 3 5 9 17 31…，请编写函数f(n)，求出该数列的第n项值，最后调用该函数进行测试。"""


def f(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return f(n - 1) + f(n - 2) + f(n - 3)


n = int(input("请输入n: "))
print("数列为: ", end=" ")
for i in range(1, n + 1):
    print(f(i), end=' ')
print("\n第n项为: ", f(n))

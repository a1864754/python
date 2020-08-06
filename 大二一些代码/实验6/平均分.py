"""（二）用户输入若干个分数，求所有分数的平均分。每输入一个分数后询问是否继续输
入下一个分数，回答“yes”就继续输入下一个分数，回答“no”就停止输入分数。请使用异
常处理机制来编写程序。"""
from numpy import *

listone = []
boolone = "yes"
while boolone == "yes":
    try:

        num = float(input("请输入一个数:"))
        listone.append(num)
        boolone = input("是否继续输入,继续请输入yes,结束输入no:")

    except(ValueError):
        print("输入有误,请重新输入")
pinjun = mean(listone)
print("平均值为:", pinjun)

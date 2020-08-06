"""（一）编写函数模拟猜数游戏。系统随机产生一个数，并且指定玩家最多可以猜的次数
和数字范围例如[1, 100)，系统会根据玩家的猜测进行提示，玩家则可以根据系统的提示对
下一次的猜测进行适当调整。请使用异常处理机制来编写程序。"""
import random

count = 0
x = random.randint(1, 99)
print(x)
while True:
    try:
        if count == 5:
            print("机会用完了，下次加油！")
            break
        y = int(input("请输入一个整数,范围是:[1,100),只能猜5次哦\n"))
        if x == y:
            count += 1
            print("猜对了！使用次数[%d]" % count)
            break
        elif x < y:
            print("太大了！剩余次数[%d]" % (4 - count))
        else:
            print("太小了！剩余次数[%d]" % (4 - count))
        count += 1
    except(ValueError):
        print("输入有误,请重新输入")

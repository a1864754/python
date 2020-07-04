"""请编写函数实现以下功能：输入三个实数序列，例如：[0.9,0.5,0.7]、[0.4,0.6,0.3]、[0.5,0.2,0.4]，
输出三个序列中各取一个相乘后最大值以及下标组合方式，如：最大值为0.9*0.6*0.5=0.27，下标组合为(0,1,0)。"""


def max_3(list1, list2, list3):
    num1 = max(list1)
    num2 = max(list2)
    num3 = max(list3)
    sum = num1 * num2 * num3
    list_zuobiao.append(list1.index(num1))
    list_zuobiao.append(list2.index(num2))
    list_zuobiao.append(list3.index(num3))
    return sum, num1, num2, num3


list_zuobiao = []
list1 = [0.9, 0.5, 0.7]
list2 = [0.4, 0.6, 0.3]
list3 = [0.5, 0.2, 0.4]
sum, num1, num2, num3 = max_3(list1, list2, list3)
print("最大值为: {0}*{1}*{2}={3}".format(num1, num2, num3, sum),
      "\n下标组合为:", list_zuobiao)

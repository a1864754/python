"""编写函数，接收一个字符串，分别统计大写字母、小写字母、数字、其它字符的个数，并以元组的形式返回结果，最后调用测试。"""


def countString(a):
    shuZi = 0
    xiaoZiMu = 0
    daZimu = 0
    ziFu = 0
    for i in a:
        if i.isdigit():
            shuZi += 1
        elif i.islower():
            xiaoZiMu += 1
        elif i.isupper():
            daZimu += 1
        else:
            ziFu += 1
    return daZimu, xiaoZiMu, shuZi, ziFu


a = input('请输入一个字符串：')
daZiMu, xiaoZiMu, shuZi, ziFu = countString(a)

print("在输入的字符串中\n大写字母有{0}个;小写字母有{1}个;数字有{2}个;其他字符有{3}个"
      .format(daZiMu, xiaoZiMu, shuZi, ziFu))

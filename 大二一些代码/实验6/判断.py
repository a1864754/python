"""（三）编写一个自定义异常类，程序执行过程如下：
判断输入的字符串长度是否小于5，如果小于5，例如输入长度为3，则输出“'The length
ofinputis3,expecting at least 5'”，如果大于5，则输出“'print success'”。"""


class ziDingYi(Exception):
    def __init__(self, str1):
        self.leng = len(str1)

    def panDuan(self):
        if self.leng < 5:
            return 'The input is of length %s,expecting at least 5' % self.leng
        else:
            return 'print success'


try:
    str_input = input("请输入一个字符串: ")
    raise ziDingYi(str_input)
except ziDingYi as e:
    print(e.panDuan())

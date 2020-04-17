"""编写程序，用户输入一个长度不小于6的字符串作为密码，检查并判断该密码的
安全强度。若输入密码仅包含数字，则密码强度为“weak”；若输入密码包含数字和小写字
母，则密码强度为“belowmiddle”；若输入密码包含数字、小写字母和大写字母，则密码强
度为“abovemiddle”；若输入密码包含数字、小写字母、大写字母和其它字符，则密码强度
为“strong”。例如，输入字符串“123456”则显示其密码强度为“weak”；输入字符串
“Xuluhui@021”则显示其密码强度为“strong”。
"""
import string


def check(pwd):
    if len(pwd) < 6:
        return "密码位数小于6,请重新输入."
    # 密码强度等级与包含字符种类的对应关系
    d = {1: 'weak', 2: 'belowmiddle', 3: 'abovemiddle', 4: 'strong'}
    # 分别用来标记pwd是否含有数字、小写字母、大写字母、其他字符
    r = [False] * 4
    for ch in pwd:
        if not r[0] and ch in string.digits:
            r[0] = True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        elif not r[3] and ch in string.punctuation:
            r[3] = True

    # 统计包含的字符种类，返回密码强度
    return d.get(r.count(True), "错误")


while True:
    choose = input("功能选择--1.进行密码强度判断;其他:退出程序\n")
    if choose == "1":
        pwd = input("请输入您的密码：")
        print("密码强度等级: ", check(pwd))
    else:
        print("程序已关闭,欢迎下次使用.")
        break

"""编写程序，生成指定长度的随机密码。要求用户指定密码长度，且密码由数字或字母组成。"""
import random
import string

sumzimu = string.ascii_letters
sumnum = string.digits
lenght = int(input("请指定长度: "))
passwd = "".join(random.sample(string.ascii_letters + string.digits, lenght))
print("生成的密码是:", passwd)

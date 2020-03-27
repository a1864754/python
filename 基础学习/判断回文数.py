num = input("请输入一个数字: ")
num_re = num[::-1]
if (num == num_re):
    print("你输入的数字是: %s 这是一个回文数" % num)
else:
    print("你输入的数字是: %s 这不是一个回文数" % num)

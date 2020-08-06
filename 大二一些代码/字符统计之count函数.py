"""编写程序，用户输入一段英文和一个指定字符，统计该字符出现的次数。"""
str1 = input("请输入一个字符串: ")
str2 = input("请输入要想要查询的字符: ")
count1 = str1.count(str2)
print("字符 %s 出现的次数为: %s" % (str2, count1))
print("字符 {0} 出现的次数为: {1}".format(str2, count1))

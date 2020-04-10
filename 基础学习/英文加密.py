"""编写程序，用户输入一段英文，实现对该字符串的加密，加密方法是将字母字符
改变为循环后移1个位置后的字母，数字和其它字符不予处理。例如，字符串“Iloveyou.”
加密后为“J mpwf zpv.”。"""
str1 = input("请输入一串字符: ")
str2 = ""
for i in str1:
    i = ord(i)
    i = i + 1
    i = chr(i)
    str2 += i
print(str2)

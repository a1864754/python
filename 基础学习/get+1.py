ll = tuple(input("请输入汉字: "))
d = dict()
for num in ll:
    d[num] = d.get(num, 0) + 1
for k, v in d.items():
    print(k, v, sep=":")

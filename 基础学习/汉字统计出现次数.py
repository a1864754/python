tongji = {}
achars = tuple(input("请输入一串汉字(可以用逗号为间隔): "))
for i in achars:
    if i in tongji or i in [",", "，"]:
        pass
    else:
        tongji[i] = achars.count(i)
print(sorted(tongji.items(), key=lambda item: item[1]))
print(0)

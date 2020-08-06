tongji = {}
achars = tuple(input("请输入一串汉字 "))
for i in achars:
        tongji[i] = achars.count(i)
print(sorted(tongji.items(), key=lambda item: item[1]))

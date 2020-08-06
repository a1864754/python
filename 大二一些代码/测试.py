xiaoming = {"jisuanji": 52, "yingyu": 76, "zhuanye": 59}
mike = {"jisuanji": 88, "yingyu": 94, "zhuanye": 86}
lucy = {"jisuanji": 77, "yingyu": 62, "zhuanye": 57}
rose = {"jisuanji": 84, "yingyu": 55, "zhuanye": 87}
datas = [xiaoming, mike, lucy, rose]

name = input()
fenshuxian = int(input())
print(datas.index(name))
indexs = datas.index(lucy)
a = datas[indexs]["jisuanji"]
b = datas[indexs]["yingyu"]
c = datas[indexs]["zhuangye"]
if a > 60 and b > 60 and a + b + c > fenshuxian:
    print("yes")
else:
    print("no")

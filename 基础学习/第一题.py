n, k = map(int, input().split())
lilunchengji_bianhao = {}
pinfen = []
pingjunfenshu = []
a = 1
b = 1
c = 0
d = 0
e = []
while a <= n:  # 个人理论成绩+队伍编号,这里用字典进行信息录入,成绩数据类型类型为字符串型,在后面会进行格式转换为int型
    e = (input().split())
    lilunchengji_bianhao[e[0]] = e[1]
    a = a + 1
while b <= k:  # 团队评分录入,录入为二维列表
    pinfen.append(list(map(int, input().split())))
    b = b + 1
for i in pinfen:  # 进行评分过滤,去掉不合格的评分并且计算出每一队的平均分
    sum1 = 0
    for ii in i:
        sum1 = sum1 + int(ii)
    pingjunfenshu.append(sum1 / (n / k))
    sum1 = 0
    for ii in i:
        count1 = 1
        if ii > (pingjunfenshu[c] + 15) or ii < (pingjunfenshu[c] - 15):
            del ii
        if count1 == 3:
            c += 1
            count1 = 0
    for ii in i:
        sum1 += ii
    pingjunfenshu.append(sum1 / len(i))

for k, v in lilunchengji_bianhao.items():  # 进行个人成绩分数计算,理论分+团队平均分*0.4
    count = 1
    k = int(k)
    k = k + pingjunfenshu[d] / 3 * 0.4
    if count == 3:
        d += 1
        count = 0
    print(k)
print(sorted(lilunchengji_bianhao.keys()))
for k, v in lilunchengji_bianhao.items():
    print(k, v)

"""已知有一个包含一些同学成绩的字典，现在需要计算所有成绩的最高分、最低分、
平均分，并查找所有最高分同学。
"""
scores = {"小一": 45, "小二": 78, "小三": 40, "小四": 96, "小五": 65,
          "小六": 90, "小七": 99, "小八": 99, "小九": 60}
highest = max(scores.values())
lowest = min(scores.values())
average = sum(scores.values()) / len(scores)
print("最高分:%d 最低分: %d 平均分: %.2f" % (highest, lowest, average))
highestPerson = [name for name, score in scores.items() if score == highest]
print("最高分有: ", end=" ")
for hp in highestPerson:
    print(hp, end=",")

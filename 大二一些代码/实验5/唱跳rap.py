class Person:
    def __init__(self, name):
        self.name = name

    def sing(self):
        return "唱"

    def dance(self):
        return "跳,"

    def rap(self):
        return "rap"

    def wangzhe(self):
        return "王者"


kunkun = Person("kunkun")
print("大家好我是练习时长两年半的个人练习生{0}，喜欢{1},{2},{3},{4},music，鸡你太美～".format(kunkun.name, kunkun.sing(),
                                                                   kunkun.dance(), kunkun.rap(), kunkun.wangzhe()))

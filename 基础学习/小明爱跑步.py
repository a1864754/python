class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print("%s爱跑步,锻炼身体能减肥" % self.name)

    def eat(self):
        self.weight += 1
        print("%s爱吃零食,吃完零食再减肥" % self.name)

    def __str__(self):
        return "我是%s,我的体重是:%s" % (self.name, self.weight)


xiaomin = Person("小明", 75)
xiaomin.eat()
xiaomin.run()
print(xiaomin)

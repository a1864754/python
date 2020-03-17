class Cat:
    def __init__(self, new_name):
        self.name = new_name

    def __str__(self):
        return "我是%s" % self.name


tom = Cat("Tom")
print(tom)

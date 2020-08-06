class Animal:
    def show(self, who):
        who.show()


class Cat:
    def show(self):
        print("猫咪：早安喵~")


class Dog(Cat):
    def show(self):
        print("哈士奇：哇呜~")


class Tiger(Cat):
    def show(self):
        print("辛巴：吼~")


a = Animal()
a.show(Cat())
a.show(Dog())
a.show(Tiger())

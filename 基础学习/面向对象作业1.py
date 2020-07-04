"""
编写程序，有两个类，类A继承自类B，两个类都实现了handle()方法，在类A的handle()方法实现中调用类B的handle()方法，
并创建类A的对象进行测试。
"""


class B:
    def handle(self):
        print("B")


class A(B):
    def handle(self):
        super().handle()
        print("A")


a = A()
a.handle()

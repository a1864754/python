"""编写一个队列类myQueue，完成队列的初始化、删除、入队和出队等操作。"""


class myQueue:
    # 初始化
    def __init__(self):
        self.content = []

    # 从右侧入队
    def right_append(self, v):
        self.content.append(v)

    # 从左侧入队
    def left_append(self, v):
        self.content.insert(0, v)

    # 从左侧出队
    def left_out(self):
        i = self.content.pop(0)
        return i

    # 从右侧出队
    def right_out(self):
        i = self.content.pop(-1)
        return i

    # 队列的删除
    def clear(self):
        self.content = []
        self.current = 0

    # 打印
    def __str__(self):
        return "队列为:" + str(self.content)


# 测试
if __name__ == '__main__':
    one = myQueue()
    for i in range(1, 10):
        one.right_append(i)
    print("现在---", one)
    one.right_append(666)  # 右入队
    print("'666'从右进来---", one)
    one.left_append(999)  # 左入队
    print("'999'从左进来---", one)
    one.right_out()  # 右出队
    print("'666'从右出去---", one)
    one.left_out()  # 左出队
    print("'999从左出去'---", one)

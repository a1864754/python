"""编写程序，模拟打字练习程序的成绩评定。假设origin为原始内容，userInput为
用户练习时输入的内容，要求用户输入的内容长度不能大于原始内容的长度，如果对应位置
的字符一致则认为正确，否则判定输入错误。最后成绩为：正确的字符数量/原始字符串长
度，按百分比输出，要求保留2位小数。"""


def daZi():
    origin = "liurui好帅啊"  # 练习的内容
    print("用户练习的内容：")
    print(origin)
    while True:
        try:
            useInput = input("请输入:")
            assert len(useInput) <= len(origin)  # assert断言：可以理解为“这里一定是成立的”，如果表达式不成立（False），则抛出异常。
        except:
            print("输入的长度有误,请再次输入")
        else:
            count = 0  # 对正确的进行计数
            for i, m in zip(useInput, origin):  # 对每一个字符进行比较
                if i == m:
                    count = count + 1
                else:
                    continue
            result = round(count / len(origin) * 100, 2)
            print("正确率:{}%".format(result))
            break  # 跳出while这循环


daZi()

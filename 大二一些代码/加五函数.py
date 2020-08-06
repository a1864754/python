def jiawu(list1, num):
    list2 = []
    for i in list1:
        list2.append(i + num)
    return list2


list1 = input("请输入一个列表(以空格为间隔符): ").split()
num = int(input("请输入要加的数字: "))
list1 = list(map(int, list1))
list2 = jiawu(list1, num)
print("修改后的列表为:", list2)

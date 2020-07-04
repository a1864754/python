def shui_xian_hua(num):
    list_sum = 0
    num_list = list(map(int, num))
    num = int(num)
    for i in num_list:
        list_sum += (i ** len(num_list))
    if list_sum == num:
        return num, "是"
    else:
        return num, "不是"


numin = input("请输入一个数字: ")
numout, bools = shui_xian_hua(numin)
print("{0}{1}一个水仙花数".format(numout, bools))

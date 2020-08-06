with open('data[复件].txt', 'r') as fp:
    data = fp.readlines()
print("复件文件:", data)

with open('data.txt', 'w') as fp:
    fp.writelines(data)

with open('data.txt', 'r') as fp:
    data = fp.readlines()
print("拷贝后文件:", data)

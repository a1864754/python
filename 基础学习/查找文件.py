import os

id1 = input('请输入待查找的初始目录:')
name = input('请输入需要查找的目标文件:')


def seek_files(id1, name):
    """根据输入的文件名称查找对应的文件夹有无改文件，有则输出文件地址"""
    for root, dirs, files in os.walk(id1):
        if name in files:
            # 当层文件内有该文件，输出文件地址
            print('{0}/{1}'.format(root, name))


seek_files(id1, name)

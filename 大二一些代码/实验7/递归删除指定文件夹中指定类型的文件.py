import os
import os.path
import stat


# 获取文件后缀名
def get_file_extension(filename):
    return os.path.splitext(filename)[1]


a = input("指定类型")
rootdir = r"liurui"  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        real_path = os.path.join(parent, filename)
        if get_file_extension(filename) == a:
            os.chmod(real_path, stat.S_IWRITE)
            os.remove(real_path)
            print("delete:" + real_path)

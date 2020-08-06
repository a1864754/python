import os

from PIL import Image


def is_jpg(filename):
    data = open(filename, "rb").read(3)
    if data[:3] != b"\xff\xd8\xff":
        return False
    return True


path0 = r"C:\Users\vayne\Desktop"
dir = os.listdir(path0)
for i in dir:
    path1 = os.path.join(path0, i)
    if path1.endswith('.jpg'):
        print("打开", path1)
        if is_jpg(path1):
            img = Image.open(path1)
            img.show()

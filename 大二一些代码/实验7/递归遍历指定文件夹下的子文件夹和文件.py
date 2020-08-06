from os import listdir
from os.path import join, isfile, isdir


def listDirDepthFirst(directory):
    for subPath in listdir(directory):
        path = join(directory, subPath)
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listDirDepthFirst(path)


listDirDepthFirst("liurui")

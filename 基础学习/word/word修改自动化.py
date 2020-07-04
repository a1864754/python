import win32com
from win32com.client import Dispatch

w = win32com.client.Dispatch('Word.Application')

# 后台运行，不显示，不警告
w.Visible = 0
w.DisplayAlerts = 0

for i in range(1, 29):
    print("开始第", i, "份")

    i = str(i)

    a = "C:\\Users\\vayne\\Desktop\\新建文件夹 (2)\\至诚书院大学生综合素质教育考核表(" + i + ").docx"

    # 打开新的文件
    doc = w.Documents.Open(FileName=a)

    # 正文文字替换
    w.Selection.Find.ClearFormatting()
    w.Selection.Find.Replacement.ClearFormatting()
    w.Selection.Find.Execute("孙亚博", False, False, False, False, False, True, 1, True, "刘锐", 2)
    w.Selection.Find.Execute("180809011075", False, False, False, False, False, True, 1, True, "180808011022", 2)
    w.Selection.Find.Execute("☑", False, False, False, False, False, True, 1, True, "□", 2)

    # 关闭
    doc.Close()
    # w.Documents.Close(wc.wdDoNotSaveChanges)
print("替换完成!")
w.Quit()

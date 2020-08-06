import time

import pyautogui
import pyautogui as auto

# a=input("请输入要输入的文章：")
time.sleep(5)  # 延迟5秒
a = "liyitongwoaini "
for i in range(1, 100):
    # pyautogui.typewrite(a, '0.05')
    pyautogui.typewrite(a + str(i), '0.001')
    auto.hotkey('enter')

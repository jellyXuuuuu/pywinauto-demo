import pywinauto
import time, os
from pywinauto.application import Application
from pywinauto import Desktop

chrome_dir = r"D:\\computer\\tools\\googlechrome73\\Google Chrome\\chrome.exe"
app = Application(backend="uia").start(\
    chrome_dir + \
    ' --force-renderer-accessibility'\
    + ' https://map.1tyun.ink:8903/newtest"', # timeout=20,
    wait_for_idle=False)

# time.sleep(6.5)  # wait in case if mouse click events happens before the window(chrome page) started

# app.window_(title='New Tab')

# app_new_tab = Application(backend='uia').connect(\
#     path='D:\\computer\\tools\\googlechrome73\\Google Chrome\\chrome.exe',\
#      title_re='New Tab')
# print('app_new_tab', app_new_tab)


# print("================1==================")
# NewTab = Desktop(backend="uia").window(title='1tvideo - Google Chrome')
NewTab = Desktop(backend="uia").window(title_re='1tvideo')


''' print all identifires '''
# NewTab.print_control_identifiers() # prints UI elements subtree
NewTab.maximize()

# print("================2==================")
# NewTab.window_text()

# print("================3==================")
# print(NewTab.from_point(10, 660))
# print(NewTab.from_point(10, 660).friendly_class_name())

# print("================4==================")
# print(NewTab.from_point(1270, 660))
# print(NewTab.from_point(1270, 660).friendly_class_name())

# 定位到树控件
# win_tree = NewTab.child_window(class_name = "")
# # 定位树结构里的管理模板节点
# win_tree.get_item('\ue917').click()


# print("================5==================")
# NewTab.maximize()


''' mouse event '''

pywinauto.mouse.click(button='left', coords=(1900, 110))   # close 右上角询问为正常关闭

time.sleep(2.5)  # wait in case if mouse click events happens before the window(chrome page) started

pywinauto.mouse.click(button='left', coords=(500, 270))

time.sleep(0.5)  # wait 
pywinauto.mouse.click(button='left', coords=(850, 950))   # mute yourself
pywinauto.mouse.click(button='left', coords=(1050, 950))   # video

time.sleep(1)  # wait 
pywinauto.mouse.click(button='left', coords=(680, 850))   # close the tip window
time.sleep(0.5)
pywinauto.mouse.click(button='left', coords=(680, 870))   # close the tip window
time.sleep(0.5)
pywinauto.mouse.click(button='left', coords=(680, 870))   # close the tip window
# pywinauto.mouse.click(button='left', coords=(450, 600))

''' several click test as follows: '''

# pywinauto.mouse.double_click(button='left', coords=(500, 60))  # effect the link district
# pywinauto.mouse.double_click(button='left', coords=(500, 50))  # effect: to minimize since double click tab nav

# pywinauto.mouse.click(button='left', coords=(850, 950))   # mute yourself
# pywinauto.mouse.click(button='left', coords=(1700, 950))   # invite other people to attend the meeting
# pywinauto.mouse.click(button='left', coords=(50, 950))  # to share your screen ----


''' key board event '''
pywinauto.keyboard.send_keys('^s') # (Ctrl+S), full-screen screening
# pywinauto.mouse.click(button='left', coords=(1450, 820))  # click 'u取消' in case save html
# saver = app.window_(title=u'另存为')
# saver.print_control_identifiers()
time.sleep(0.5)
pywinauto.keyboard.send_keys('{ESC}')


''' close current process '''
# taskkill /f /im chrome.exe /t  # (shell cmd, to kill all chrome process..)
# print(os.getpid())
# os.system('taskkill /f /im chrome.exe /t')  # (shell cmd, to kill all chrome process..)

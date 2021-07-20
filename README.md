# pywinauto-demo
a simple demo for pywinauto to auto click gui in win10 on chrome 73

Task: to use auto tool(pywinauto) to close all the tip windows when started the jitisi website(https://map.1tyun.ink:8903/new)

1. firstly successfully installed pywinauto and use it:

face problem - cannot found module pywinauto even already installed using pip (Python)

bc pywinauto have bug when using python 3.8 (上网查了原因是pywinauto有bug，Python之后的版本都会报错，所以尝试用python3.7运行，但是可能pip安装也不对，所以就用了pipenv这个不同版本协调的类似pip工具 - 

https://www.zhihu.com/question/368411359)

2. use desktop() method to successfully recognize handle, others failed

```python
Desktop(backend="uia").window(title_re='1tvideo') # success
''' fail1 '''
# app.window_(title='New Tab') 
''' fail2 '''
# app_new_tab = Application(backend='uia').connect(\
#     path='D:\\computer\\tools\\googlechrome73\\Google Chrome\\chrome.exe',\
#      title_re='New Tab')
```



3. always have problem:

```shell
C:\Users\16593\.virtualenvs\juiti-QRFUgQcO\lib\site-packages\pywinauto\application.py:1076: RuntimeWarning: Application is not loaded correctly (WaitForInputIdle failed)
  warnings.warn('Application is not loaded correctly (WaitForInputIdle failed)', RuntimeWarning)
```

solution:

```python
chrome_dir = r"D:\\computer\\tools\\googlechrome73\\Google Chrome\\chrome.exe"
app = Application(backend="uia").start(\
    chrome_dir + \
    ' --force-renderer-accessibility'\
    + ' https://map.1tyun.ink:8903/new"', # timeout=20,
    wait_for_idle=False)
```



- Add another parameter 'wait_for_idle=False' 


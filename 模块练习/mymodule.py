# from distutils.core import setup
# setup(name='压缩包的名字',version='1.0',author='李彦达',py_modules=['my_package.module1'])


# 导入这个模块要把这个模块放到python shell相同目录下 才会找到
# 在python exe环境导入一个模块：python解释器寻找：
# 1.当前目录 2.如果不在那么去PYTHONPATH下的每个目录去寻找 3.如果还不在就去查看默认路径(每个系统不一样)
# def say_hi():
#     print("这是我的第一个模块")
# __version__='0.1'
import os
for dir in os.walk('d:\\a'):
    print(dir)
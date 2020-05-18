# 最开始前言部分 涉及计算机组成的知识了 这学期就学了hh
# # 同步IO:  等结果，不复杂
#   异步IO:  不等结果，复杂

# # 基本概念：input， output，stream
# 存在问题：输入和接收速度不匹配
# 解决方法：同步、异步(回调--好了叫我，轮询---好了没...好了没(他复杂的两种体现))
# 收获新知：编程语言都会把操作系统提供的低级C接口封装起来方便使用

# 本章我们所讲的都是同步IO



# 文件读写。python内置了读写文件的函数，用法和C是兼容的。
# 对写文件前 我们必须先了解一下 在磁盘上读写文件的功能是由操作系统提供的
# 操作系统绝不允许普通的程序直接操作磁盘 
# 所以读写文件就是程序请求操作系统打开一个文件对象 然后通过操作系统从这个文件对象中读取数据(或者把数据写入这个文件对象)

f=open('d:/Python程序/算法.txt','r')
# 标识符'r'表示读 这样我们就成功打开了一个文件 f指向这个文件对象
print(f.read())
# 调用read方法可以一次读取文件的所有内容 python将读取的内容读到内存,用一个str对象表示
f.close()
# 调用close()方法关闭文件。文件使用完毕必须关闭,因为文件对象会占用操作系统的资源

# 由于文件读写时都可能产生IOError,一旦出错 后面的f.close()就不会被调用。
# 所以为了保证无论是否出错都能正确地断臂文件 我们使用try..catch..finally
try:
    f=open('d:/Python程序/算法.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
# 但是总是这么写太不方便 python引入了with语句来自动帮我们调用close()方法
with open('d:/Python程序/算法.txt','r') as f:
    print(f.read())
# 这和前面的try...finally结构是一样的,但是代码更加简介,并且不必调用close()方法
# read()一次性读取文件的全部内容；read(size)最多读取size个字节的内容；
# readline()每次读取一行内容；readlines()一次读取所有内容并且按行返回list
# 不能确定文件大小 反复调用read(size)比较保险；如果是配置文件，调用readlines()比较方便
f=open('d:/Python程序/算法.txt','r')
for line in f.readlines():
    print(line.strip())
    # strip函数末尾的'\n'去掉
    # strip函数用于移除字符串头尾指定的字符(默认为空格或换行符)
    # str='00000323RUNNqs01000'
    # print(str.strip('0'))
    # 把首尾的零都除去
    # print(str2.strip('12'))
    # 只要头尾包含指定字符序列中的字符就除去


#feel-like Object 
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。？下节课讲这个



# 二进制文件
# 前面默认的都是文本文件,使用UTF-8编码的文本文件。
# 如果读取二进制文件 比如图片 视频等 用'rb'模式打开文件
# f=open('D:\Python程序\IMG_6679.JPG','rb')
# print(f.read())

# 读取非UTF编码的文本文件 需要open()传入encoding参数
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# >>> f.read()
# 比如读取GBK编码的文件
# 但是又有可能遇到有些编码不规范的文件可能遇到UnicodeDecodeError
# 因为在文本文件中可能夹杂一些非法编码的字符。遇到这种情况,open()函数还接收一个errors参数
# 如果遇到编码错误 直接忽略
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')




# 写文件 传入w表示写文本文件 传入wb表示写二进制文件
f=open('d:/Python程序/算法.txt','w')
f.write('Hello world!')
f.close()

with open('d:/Python程序/算法.txt','w') as f:
    f.write('Hello world')
    # 啊这是覆盖原来文件重新写一个文件
    # # 我们希望追加到文件末尾怎么办？可以传入'a'以追加模式写入
    # f=open('d:/Python程序/算法.txt','w')
    # f.write('Hello world!')
    # f.close() 酱紫
# 要写入特定编码的文本文件 请给open()函数传入encoding参数,将字符串自动转化成指定编码


#with原理补充: with后面的语句会被求值 返回对象的__enter__()方法被调用
# 这个方法的返回值被赋给as关键字后面的变量,当with后面的代码块全部被执行后
# 将调用前面返回对象的__exit__()方法
# with语句最关键的地方在于被求值对象必须有__enter__() 和__exit__()方法,那么我们
# 就可以自己实现这两个方法来自定义with语句处理异常
# 例子：
class Sample():
    def __enter__(self):
        print('in__enter__')
        return 'Foo'
    def __exit__(self,exec_type,exc_val,exc_tb):
        # 后三个三个参数  第一个：错误的类型
        # 第二个：错误类型对应的值 第三个：代码中错误发生的位置
        print('in__exit__')
# 例子二：
# def get_sample():
#     return Sample()
# with get_sample() as f:
#     print('Sample:',f)

# class Sample():
#     def __enter__(self):
#         print('in enter')
#         return self
#     def __exit__(self,exec_type,exc_val,exc_tb):
#         print('type:',exec_type)
#         print('val:',exc_val)
#         print('tb:',exc_tb)
#     def do_something(self):
#         bar=1/0
#         return bar+10
# with Sample() as f:
#     f.do_something()


# 实现一个新的上下文管理器的最简单方法就是使用contexlib模块中的@contextmanager装饰器
# 下面例子实现了代码块计时功能的上下文管理器例子：
import time
from contextlib import contextmanager
@contextmanager
def timethis(labl):
    start=time.time()
    try:
        yield
    finally:
        end=time.time()
        print("{}:{}".format(labl,end-start))
with timethis('counting'):
    n=10000000
    while n>0:
        n-=1
# timethis()函数中 yield之前的代码会在上下文管理器中作为__enter__()方法执行
# 所有在yield之后的代码会作为__exit__()方法执行。如果出现了异常会在yield那里抛出


# 练习：请将本地一个文本文件读为一个str并打印出来
# 较简单  同上面一样
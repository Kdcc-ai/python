#~~contextlib~~（实现上下文管理器）
# python中 1.读写文件这样的资源要特别注意必须在使用完毕后正确关闭他们（可以使用try...finally）
#          2.或者使用with语句方便使用资源 不必担心资源没被关闭（前提是这个对象的实现的上下文管理器）


# 并不是只有open函数返回的fp对象才能使用with语句
# 实际上任何对象 只要正确实现了上下文管理，就可以用于with语句



# 1.
# 通过__enter__和__exit方法实现上下文管理
class Query(object):
    def __init__(self, name):
        self.name = name
    #     enter负责进入代码块的准备工作 进入前被调用
    def __enter__(self):
        print('Begin')
        return self
    #      exit负责离开代码块的善后工作 离开后被调用
    #      发生异常 python会把异常的三项信息传递给exit方法
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('Query info about %s...' % self.name)
with Query('Bob') as q:
    q.query()

class File(object):
    # 自定义的用于处理文件的类
    # （相当于open函数）
    def __init__(self,filename,method):
        self.fileobj = open(filename,method)
    def __enter__(self):
        return  self.fileobj
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fileobj.close()
#         试想这个File类是不是就是和那个open方法差不多呢？
with File('demo.txt','w') as f:
    # with语句首先 调用__enter__方法
    #__enter__方法返回打开的文件对象给with语句
    # 打开的文件对象被传递给f参数
    f.write('Hello')
    # .write来写文件
    #  with语句调用__exit__方法来关闭文件



# 2.@contextmanager
#   利用@contextmanager装饰使用生成器函数完成一个上下文管理器
from contextlib import contextmanager
class Query(object):
    def __init__(self,name):
        self.name=name
    def query(self):
        print('Query info about %s...' % self.name)
@contextmanager
def create_query(name):
    # 生成器函数creat_query函数再yield之前的代码等同于上下文管理器中的__enter__函数
    print('Begin')
    q = Query(name)
    # __enter__函数的返回值等同于yield的返回值
    yield  q
    # yield之后的语句相当于__exit__函数 此时发生的任何异常都可以再次通过yield函数返回
    print('End')
with create_query('Bob') as f:
    # with语句首先执行 63 64行代码（相当于__enter__函数）
    # __enter__函数返回的对象为q 传递给f参数
    f.query()
    # 调用.query方法
    # with语句执行68行代码（相当于调用__exit__方法）


# 2.希望再某段代码执行前后自动执行某段代码（这个应该可以用于测试之类的）
#   也可以用@contextmanager
@contextmanager
def tag(name):
    print("</%s>"%name)
    yield
    print('</%s>'%name)
with tag('h1'):
    print('hello')
    print('world')


# 3.@closing
# closing()把一个任意对象变为上下文对象
# （其实closing对象就是一个经过@contextmanager装饰的生成器）
# ！！如果一个对象没有实现上下文，我们就不能把他作为ith语句！！
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


# closing对象的源码  所以说closing上下文管理器仅用于具有close()方法的资源对象
class closing(object):
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()


# 装饰器？？ 函数也是一个对象而且函数对象可以被赋值给变量
def now():
    print("2020")
f=now
print(f())
print(f.__name__)
# 得到函数的名字

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# decorator本质上是一个返回函数的高阶函数
def log(func):
  def wrapper(*args,**kw):
     print('call %s()' % func.__name__)
     return func(*args,**kw)
  return wrapper
# log接收一个函数作为参数 并返回一个函数
@log
def now():
    print("2020-2-10")
now()
print(now.__name__)
#  21行输出call now() 2020-2-10
#  22行输出wrapper 这块我们输出的是wrapper因为now指向了wrapper函数了
#  把@log放到now()函数的定义处 相当于执行了语句：now=log(now)
# 个人理解：log()函数返回函数 18行返回了一个函数 所以执行语句之后

# 斗记住这句话斗中了
# now()函数仍然存在 只是现在同名的now变量指向了新的函数（可以理解为对象我觉得），于是调用now（）将执行新函数wrapper

# 在wraaper（）函数可以接收任意参数的调用 在wrapper内首先打印日志 紧接着调用原始函数




# 三层嵌套是什么呢？？？
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2020-2-10')
# 把@log放到now('execute')函数的定义处 相当于执行了now = log('execute')(now)
# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。最终返回值是wrapper函数

# 斗记住这句话斗中了
# now指向了新的函数（可以理解为对象我觉得） 所以调用now（）将执行新函数wrapper函数

# 故针对25行的内容 我们要把原始函数的_name_等属性复制到wrapper函数中，那么我们怎么复制呢？

# 利用Python内置的functools.wraps
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s()"%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print("2020-2-10")
now()
print(now.__name__)
# 61行输出call now() 2020-2-10
# 62行输出now



import time
# 练习：请设计一个decorator 他可以作用于任何函数上 并打印该函数的执行时间
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start=time.time()
        fn(*args,**kw)
        end=time.time()
        print("%s executed in %.4f ms" % (fn.__name__,end-start))
        return fn(*args,**kw)
    return wrapper
@metric
# 拿78行语句说明 执行完78行 相当于执行语句fast=metric(fast(x,y))
# metric(fast(x,y))返回一个函数 所以执行完这行语句fast(x,y)函数仍然存在 只是同名的fast变量指向了新的函数wrapper（对象）于是调用新函数fast(x,y)指向新函数wrapper
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
# print(f, s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。


# 小结 设计一个decorator，能在函数调用前后打印出'begin call'和'end call'
# 并且同时支持带参的和不带参的 即在函数前面既可以写@log又可以写@log（）
def log02(func1):
    if isinstance(func1,str):
    # 如果说第一个传入的不是个函数 那么传入的是个str类型变量
    # 那么，因此if下面为两次函数，这样与一般带参数的三层函数一样运行
      def decorator(func):
          @functools.wraps(func)
          def wrapper(*args,**kw):
             print("bigin call")
             return func(*args,**kw)
          return wrapper
      return decorator

    else:
    # 那么第一个被传入的func1必定是函数，
    # 函数是不会被判断成字符串类型的，这样与一般不带参数的两层函数一样运行
     @functools.wraps(func1)
     def metric3(*args,**kw):
       print("end call")
       return func1(*args,**kw)
     return metric3
@log02
# 执行完这个log02之后
def test3(n):
    print('这里是%sexecuted log测试' % n)
@log02('executed')
def test4(n):
    print('这里是%sexecuted log测试' % n)
# 结果检验
test3('无')
test4('有')



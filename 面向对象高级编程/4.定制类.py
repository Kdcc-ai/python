# 定制类 
# 看到类似__slots__这种形如__×××__的变量或者函数名就要注意 这种在python中是有特殊用途的

# 这节讲用python这种有特殊用途的函数名  变量 来帮助我们 定制类 吗？
class Student(object):
    def __init__(self,name):
        self.name=name
print(Student('liyanda'))
# 怎样才能打印的好看呢？ 只需要定义好__str__()方法,返回一个好看的字符串就行了
# 相当于Java中的toString方法？
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name : %s)'%self.name
print(Student('liyanda'))
s=Student('liyanda')
print(s)


# __iter__()方法
# 如果一个类想被用于for...in循环 就必须实现__iter__()方法 该方法返回一个迭代对象
# 然后 python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    # 实例本身就是迭代对象  故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration
        return self.a


# __getitem__方法
# Fib实例虽然能作用于for循环,但他是个迭代器 直接把它当成list来使用还是不行
# 要表现的想list那样照下标取出元素 需要实现__getitem__（）方法
class Fib(object):
    def __getitem__(self,n):
        a,b,=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib()
print(f[10])
# 我们可以看到 这种就是变得可以像list一样按下标取元素了
# 我们想如何实现list当中的切片方法呢？slice
class Fib2(object):
    def __getitem__(self,n):
      if isinstance(n,int):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
      if isinstance(n,slice):
    # n是切片
         start=n.start
         stop=n.stop
         if start is None:
             start=0
         a, b = 1 , 1
         L=[]
         for x in range(stop):
             if x>=start:
                 L.append(a)
             a,b=b,a+b
         return L
f=Fib2()
print(f[:5])
# 但是我们并没有对负数之类的进行处理
# 拓展 把对象看成dict 如果__getitem__()的参数可能是一个可以作key的object，比如str

# 学到这忘了python动态语言的""鸭子类型"了
# 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# 总之 通过上面的方法 我们可以把自己定义的类表现的想python自带的list tuple dict没什么区别
# 比如上面那个Fib2()类我们定义的就像一个list差不多了
# 其实这完全归功于动态语言的"鸭子类型"不用强制继承某个接口



# __getattr__（）方法 动态返回一个属性。。
class Student(object):
    def __init__(self):
        self.name='liyanda'
    def __getattr__(self,attr):
        if attr=='score':
            return 100
s=Student()
print(s.score)   

# 动态返回一个函数
class Student(object):
    def __getattr__(self,attr):
        if attr=='age':
           return  lambda : 25
s=Student()
print(s.age())
print(s.aa)
# 101行会返回None
# 那么要让class只响应特定的几个属性,我们就要按照规定,抛出AttributeError的错误
class Student(object):
    def __getattr__(self,attr):
        if attr=='age':
           return  lambda : 25
        raise AttributeError(' \'Student\' object has no attribute \'%s\'' % attr)
# 这实际上把一个类的所有属性和方法调用全部动态化处理了....

# 利用完全动态的__getattr__,我们可以写一个链式调用：
# SDK软件工具开发包
class Chain(object):
  def __init__(self, path=''):
    self._path = path

  def __getattr__(self, path):
    return Chain('%s/%s' % (self._path, path))

  def __str__(self):
    return self._path

  __repr__ = __str__

print(Chain().status.user.timeline.list)
# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，
# 而且，不随API的增加而改变！

# # 还有些REST API会把参数放到URL中，比如GitHub的API：
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
# Chain().users('michael').repos






# # __call__()方法
# # 这个有特殊用途的方法可以帮助我们对实例 进行调用
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __call__(self):
#         print('My name is %s.' % self.name)
# s=Student('liyanda')
# s()
# # 输出 My name is liyanda.
# # self 参数不要传入
# print(s())
# # 输出 My name is liyanda.
# #      None  为什么呢

# # 对实例进行调用就好比对一个函数进行调用一样
# # 可以把函数看成对象 对象看成函数 没啥大区别
# # 如果把对象看成函数 那么函数本身和累的实例一样也可以在运行期动态创建出来

# # 那么怎么判断一个变量是 对象 还是 函数
# # 其实我们是为了知道他能不能被调用。。
# # 利用callable()函数 能被调用的对象就是一个Callable对象
# print(callable(Student('liyandazs')))
# print(callable(max))
# # li=[1,2,3]
# # print(li(1))
# # 输出 TypeError: 'list' object is not callable 懂了懂了
# print(callable([1,2,3]))
# print(callable(None))
# print(callable('str'))





# # 我们了解了python中的一些可定制的方法

# # 实现Chain().users('michael').repos
# # 输出/users/michael/repos
# class Chain(object):
#     def __init__(self, path=''):
#        self.__path = path
#     def __getattr__(self, path):
#        return Chain('%s/%s' % (self.__path, path))
#    def __call__(self, path):
#        return Chain('%s/%s' % (self.__path, path))
#    def __str__(self):
#        return self.__path

#    __repr__ = __str__
# ## 链式调用没太理解。。下面这一串是什么东西？？
# print(Chain().users('michael').repos)
# # 先进行分解
# #第一步： urls=Chain() urls等于空 定义了默认值path=''
# #第二步   urls=urls.users 没找到定义的属性 故用__getattr__方法返回一个函数调用
# #def __getattr__(self, path):
# #     return Chain('%s/%s' % (self._path, path))
# # 这一步调用Chain()而且要把查找的属性users作为参数传递了进去
# # 也就是得到了Chain(users) 最后返回的是/users
# # 第三步：urls=urls('machael')
# # 我们知道类的实例化对象不能被直接调用 __call__是为了让实例化对象一样和函数都可以被调用
# # 第三步抽象理解为 他得到了一个实例化对象 但我们要对他进行调用 就必须用那个__call__函数
# # 第三步抽象理解为class urls(Chain):
# #     def __init__(self, path='/users'):
# #        self.__path = path
# #    def __getattr__(self, path):
# #        return urls(('%s/%s' % (self.__path, path)))
# #     def __call__(self, path):
# #        return urls(('%s/%s' % (self.__path, path)))
# #    def __str__(self):
# #        return self.__path
# #    __repr__ = __str__
# # 第四步:urls=urls.repos 进行打印

 
             
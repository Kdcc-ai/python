# Python的函数定义非常简单
# ，但灵活度却非常大。
# 除了正常定义的必选参数外，
# 还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 位置参数：就是我们通常所理解的参数



# No1 默认参数：：
# 默认参数：比如power函数 power(5)默认返回25(5的平方),默认参数为2
# 必选参数:比如power函数  必选参数是第一个 默认参数是第二个

# 如何设置默认参数呢？
# 当函数有多个参数时，
# 把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
  # 先定义一个函数，传入一个list，添加一个END再返回：
  # def add_end(L=[]):
  #     L.append('END')
  #     return L
  # 当你正常调用时，结果似乎不错：
  # >>> add_end([1, 2, 3])
  # [1, 2, 3, 'END']
  # >>> add_end(['x', 'y', 'z'])
  # ['x', 'y', 'z', 'END']
  # 当你使用默认参数调用时，一开始结果也是对的：
  # >>> add_end()
  # ['END']
  # 但是，再次调用add_end()时，结果就不对了：
  # >>> add_end()
  # ['END', 'END']
  # >>> add_end()
  # ['END', 'END', 'END']
  # 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

# 这是什么原因呢？？
# 首先要记住什么时候会调用默认参数,比如上面会在参数为空的时候调用默认参数
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了

# !! 定义默认参数要牢记一点：默认参数必须指向不变对象！ !
# 修改例子:
def add_end(L=None):
    if L==None:
        L=[]
    L.append("end")
    return L
print(add_end())
print(add_end())   
# 无论调用多少次都不会有错误,要理解为什么要设计一个不变对象！



# 可变参数：：：：
# 传入函数的参数的个数是可变的,可以是0 1 2....
# 首先可以传入tuple或者list：
def calc(numbers):
      sum = 0
      for n in numbers:
          sum = sum + n * n
      return sum
print(calc([1,2,3]))
# 但是调用的时候，需要先组装出一个list或tuple：
# >>> calc([1, 2, 3])
# 14
# >>> calc((1, 3, 5, 7))
# 84

# 还可以进行简化：
# 所以，我们把函数的参数改为可变参数：
def calc2(*numbers):
     sum = 0
     for n in numbers:
         sum = sum + n * n
     return sum
print(calc2(1.0,2.0))
# 定义可变参数和定义一个list或tuple参数相比，
# 仅仅在参数前面加了一个*号。就是这样规定的
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
#  calc()
#  输出0
# 但是如果我们简化了,我们如果有一个list中的数据需要统计该怎么办呢？？
# 为此只需要这样做：
num=[1,2,3]
print(calc2(*num))
#传入的list或者tuple前面加个*,表示将这个list 中的所有元素作为可变参数传进去



#关键字参数 ：：：
# 而关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name,age,**kw):
     print("name:",name,"age:",age,"other:",kw)
print(person("Michale",30))
print(person('Bob', 35, city='Beijing'))
print(person('Adam', 45, gender='M', job='Engineer'))
# 关键字参数可以拓展函数的功能,例如这个person,调用者传入更多的参数利用关键字参数可以满足用户的一些需求

extra={"city":"beijing","job":"engineer"}
print(person("jack",24,**extra))
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#  kw将获得一个dict(记住这块是获得一个dict)，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。



# 命名关键字参数：:::
# 用来限制关键字的名字：只接收city和job作为关键字参数
print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))
def person2(name,age,*,city,job):
    print(name,age,city,job)
print(person2('Jack', 24, city='Beijing', job='Engineer'))
# 和关键字参数**kw不同，
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了:
def person3(name,age,*args,city,job):
    print(name,age,args,city,job)
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# >>> person('Jack', 24, 'Beijing', 'Engineer')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() takes 2 positional arguments but 4 were given
# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。

# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name,age,*,city="beijing",job):
    print(name,age,city,job)
print(person4('Jack', 24, job='Engineer'))

# ！！使用命名关键字参数时，
# 要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：



# 参数组合：：：：
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# 在函数调用中,Python解释器自动按照参数位置和参数名把对应的参数传进去
# 还有一些例子 理解就好 不用太深





# 作业:
def product(*number):
    total=1
    length=len(number)
    if length==0:
      raise TypeError("请传入正确的参数")
    for i in number:
      total*=i
    return total
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# 小结：*args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。

# 可变参数既可以直接传入：func(1, 2, 3)，
# 又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，
# 又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
def hello(greeting,*args):
    if(len(args)==0):
        print("%s!" % greeting)
    else:
        print("%s,%s"%(greeting,"-".join(args)))
        print("%s,%s"%(greeting,",".join(args)))
hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')
names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')

def print_scores(**kw):
    print("       Name  Score")
    print("..................")
    print(kw)
    for name,score in kw.items():
        print("%10s  %d"%(name,score))
    print()
print_scores(Adam=99,Lisa=88,Bart=77)


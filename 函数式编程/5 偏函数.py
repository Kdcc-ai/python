# 温习本章内容 主要讲了函数式编程 函数式编程是一种抽象程度很高的编程范式
# 函数式编程特点呢:允许函数本身作为参数传入 又允许返回一个函数

# 偏函数：Python的functools模块提供了很多有用的功能 2.5以后引用的

# 意指根据二进制进行转换 故传入的字符串中只能有0 1字符否则会报错
def int2(x, base=2):
    return int(x, base)
print(int2('0'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
# 可以直接使用下面的代码创建一个新的函数int2：符合函数式编程思想 确实是的返回一个函数
import functools
int2=functools.partial(int,base=2)
print(int2('1000001'))

# 简单来说这个partial函数有啥作用呢？？是不是把一个函数的某一部分固定住了
# 实际他可以接收一个函数对象 *args和**kw这3个参数
# 实际上固定了int()函数的关键字参数base

# 再者有
max2=functools.partial(max,10)
print(max2(5,6,7))
# 结果为10
slice2=functools.partial(slice,5,10)
print([slice2()])

# 偏函数的使用
# 类似于装饰器 也返回了一个新的函数嘻嘻
from functools import wraps
def sum_add(*args):
# 通过*args传入的是一个元组
    def decorator(func):
        # sum函数在这块传进来
        @wraps(func)
        def my_sum(*args2):
        # 注意参数要和原函数保持一致 *args传入的是函数的参数
            my_s=0
            for n in args:
                my_s=my_s+n
            return func(*args2)+my_s
        return my_sum
    return decorator

@sum_add(10,20)
def sum(*args):
    s=0
    for n in args:
        s=s+n
    return s
print(sum(1,2,3,4,5))
print(sum.__name__)
# 确实使用装饰器我们可以对函数进行功能的拓展


# def sum_add2(*args):
#     def decorator(fun):
#     # 得到一个函数
#         def sum3(*arg2):
#             my_s=0
#             for n in args:
#                 my_s=my_s+n
#             return fun(arg2)+

#     return decorator
# @sum_add2(10,20)
# def sum(*args):
#     s=0
#     for n in args:
#         s=s+n
#     return s
# print(sum(1,2,3,4,5))
# print(sum.__name__)
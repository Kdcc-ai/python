# #  程序编写有错误导致输出错误

# #  用户输入错误 比如输入email地址输入错误等

# #  无法在程序运行中预测的错误 写入文件得时候 磁盘满了 写不进去了
# #  抓取数据的时候网络断掉了 5，6行称之为异常 在程序中也是必须处理的

# # 我们还可以跟踪程序的执行 查看变量的值是否正确 这就是调试。python中的pdb可以让我们以单步方式执行代码
# # 最后编写测试也十分重要 测试可以在程序修改后反复运行 这是个新知识 如何编写测试呢？？

# # 错误处理
# # 和Java一样也是 try  catch finally的错误处理机制
# try:
#     print('try...')
#     r=10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')
# # 我们把认为可能出错的代码方法try里面 如果执行出错就直接跳转到except处理代码
# # 执行完except后,如果有finally语句块，则执行finally语句块 至此执行完毕

# # 有多种错误呢？
# try:
#     print('try...')
#     r=10/int('a')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ValueError:',e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')
# # python所有异常类都继承 BaseException类
# # 写异常感觉也是要从子类到父类这样子写

# # https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# # 和Java一样 可以在调用他的函数中捕获这个可能发生的异常
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')

# # 调用栈 如果错误没有被捕获 它就会一直往上抛 最后被python解释器捕获，打印出一个错误信息
# # python运行：内部将源代码->编译成字节码(保存为以.py为拓展名)
# # ->PVM运行引擎(运行脚本的组件)->运行
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     bar('0')
# main()
# # 和Java一样 出错的时候要分析错误的调用栈信息 才能定位错误的位置
# # 如果调用栈来捕获错误原因 那么程序也就结束了


# 记录错误 python内置的logging模块可以非常容易地记录错误信息 不会终止程序
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    # try:
        bar('0')
    # except Exception as e:
        # logging.exception(e)
        # pass
main()
print('END')
# 故思考使用logging可以把错误记录到日志文件里,方便事后排查


# # 抛出错误 因为错误是class 捕获一个错误就是捕获到该class 的一个实例。
# # 用raise？ 如果要抛出错误,首先根据需要可以定义一个错误的class 选择好继承关系
# # 然后用raise语句抛出一个错误的实例：
# class FooError(ValueError):
#     pass
# def foo(s):
#     n=int(s)
#     if n==0:
#         raise FooError('invalid value: %s'% s)
#     return 10/n
# foo('0')

# # 但其实 尽量使用python内置的错误类型。
# # 和Java一样 抛出的异常在调用它的那个函数进行捕获
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
# bar()
# # 这块是我们在捕获异常后 又抛出去了什么鬼？其实这块这个raise是把错误又原样抛出了

# # 还可以捕捉错误 然后把类型的错误转化成另一种类型：
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')
# # 但是绝不应该把一个IOErroe转换成毫不相干的ValueError
# # int()函数将一个和整数完全不相干的字符串转换成int型会抛出ValueErroe


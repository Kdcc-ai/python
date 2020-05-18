# 返回闭包要牢记一点 千万不要引用任何的循环变量
def createCounter():
    L=[0]
    def count():
      L[0]+=1
      return L[0]
    return count
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

def createCounter():
    s=0
    def counter():
        nonlocal s
        s+=1
        return s
    return counter
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


x='hhh'
# 对于该题以下思考：19行  global关键字修饰变量时不能直接赋值 必须先声明
def func():
    global x
    x='ccc'
    return None
    # 这个x和上面那个x一样的 不过 这样想这个global在这里是如果写的话标记的就是全局变量 如果没写标记的就是局部变量
func()
print(x)


# nonlocal关键字修饰变量
y='kkkk'
def fun2():
    y='aaa'
    # y是局部变量
    def ifun():
        y='ccc'
        # y还是局部变量 这样想 这种是一级一级的关系
        print(y)
    ifun()
    print(y)
fun2()

z='12345'
def fun3():
    x='123456'
    def fun4():
        nonlocal x
        # x是58行的x
        x='1234567'
    fun4()
    print(x)
fun3()

# global可以在任何地方修饰变量 而且被global修饰的变量表示为全局变量 改变这个变量的值会改变全局变量的
# nonlocal在嵌套函数中修饰的话 用于标识嵌套函数中的变量是包含该嵌套函数的函数中的同名变量，在嵌套函数中修改变量会影响函数中的变量

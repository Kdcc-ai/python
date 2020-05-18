# 判断对象类型 使用type()函数
print(type(123))
print(type('str'))
# 我们如何判断一个对象是否是函数呢？
import types
def fn():
    pass
# types(fn)=types.FunctionType
# types(fn)=types.BuiltinFunctionType
# type(lambda  x: x)=types.LambdaType
# type((x for x in range(10)))=types.GeneratorType

# 使用isinstance函数
isinstance([1,2,3],(list,tuple))
# 判断是否为list 或者 tuple

# 使用dir函数
print(dir("str"))
# 获取该对象的所有 属性 方法

# 类似__×××__类型的属性和方法在python中都是有特殊用途的
# 比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，
# 所以，下面的代码是等价的：
# len('ABC')
# 3
# >>> 'ABC'.__len__()
# 3
def mydog(object):
    def hh():
        pass
    def __len__(self):
        return 100
dog=mydog(object)
print(len(dog))


# 使用getattr() setattr() hasattr()
class myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=myobject()
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
setattr(obj,'y',19)
k=getattr(obj,'y')

print(hasattr(obj,'power'))
print(getattr(obj,'power'))
print(getattr(obj,'z',408))
# 如果有z返回z 如果没有返回408
fn=getattr(obj,'power')
fn()
# 以上理解就行得到某属性 设置某属性 是否有某属性
# 但我想 getattr其实本质不也是获取对象信息吗？？
# 我们直接写不好吗 其实只有在不知道对象信息的时候 我们才会去获取对象信息
# 如果可以直接写 sum=obj.x+obj.y就不要用getattr函数了
def readImage(fp):
    if hasattr(fp,'read')
        return readData(fp)
    return None
# 假如我们希望从文件流fp中读取图像 我们首先判断他有没有read方法 如果存在
# 那么该对象是一个流，如果不存在，则无法获取
# 但是上节课讲到 在python这种动态语言中 有read（）方法 并不代表fp对象是一个文件流 还可能是网络流 也可能是字节流
# 到只要read（）方法返回的是有效的图像数据就不影响读取图像的功能
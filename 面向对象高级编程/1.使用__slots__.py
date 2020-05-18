# 动态语言的灵活性 定义一个class 创建了一个class实例 
# 可以给该实例绑定任意的属性和方法
class Student(object):
    pass
s=Student()
s.name='hhh'
# 绑定一个方法
from types import MethodType
def set_age(self,age):
    self.age=age
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)
# 但是s2=Student() s2.set_age()是不正确的 他只是给了那个实例绑定了这个方法
Student.set_age=set_age
# 也可以这样
Student.set_age=MethodType(set_age,Student)
s2=Student()
s2.set_age(21)
print(s2.age)
# 这是动态语言 动态 绑定属性 方法


# 使用__slots__
# 我们用这个来限制实例的属性 比如只允许对Student实例添加name score属性
# 这是个变量 这个__slots__理解为以后我们创建Student实例后，
# 给实例添加方法，添加的这个方法里面也不能有除__slots__之外的变量

class Student(object):
    __slots__=('name','age','set_score')
# 用tuple表示允许绑定的属性名称

s=Student()
s.name='liyanda'
s.age=21
try:
    s.score=15
except AttributeError as e:
    print("AttributeError",e)
def set_score(self,score): 
    self.score=score
s.set_score=MethodType(set_score,s)
# s.set_score(100)
# 43行错误

Student.score=22
print(Student.score)
# 37 38行是正确的。。


# 使用__slots__要注意,__slots__定义的属性仅对当前类实例起作用 对继承的子类是不起作用的
class GraduateStudent(Student):
     pass
g=GraduateStudent()
g.score=999
# 33行是正确的 除非在子类中也定义__slots__ 子类实例允许定义的属性就是自身
# __slots__包含的和父类__slots__包含的

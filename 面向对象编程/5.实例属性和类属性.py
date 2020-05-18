# 实例属性？ 类属性？
# 实例属性就是创建实例的时候定义的hh
# 类属性就是某个类本身绑定的一个属性。可以在class中直接定义一个属性
class student(object):
    name='liyanda'
s=student()
print(s.name)
s.name='zhangmingyang'
print(s.name)
del s.name
print(s.name)
print(student.name)
# 这么理解 第八行实际上又创建了一个和类属性同名的实例属性
# 删除的是实例属性 故11 12行输出结果就可以知道了
# 所以实例属性和类属性别同名
class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
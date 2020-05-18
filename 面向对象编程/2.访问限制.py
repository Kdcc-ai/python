# python中如果要让内部属性 不被 外部访问 
# 可以把属性的名称前面加上两个下划线 代表private类型
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def __print(self):
        print("%s %s"%(self.__name,self.__score))

bart=Student("liyanda",100)
# print(bart.__name)
# 首先这个有了这个机制 外部代码不能随意更改对象内部的状态 比如这样没法更改__name属性了
# 想要访问我们就增加方法进行得到与修改
class Student2(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def __print(self):
        print("%s %s"%(self.__name,self.__score))
    def get_score(self):
        return self.__score
    def get_name(self):
        return self.__name
    def set_score(self,score):
        self.__score=score
    def set_score2(self,score):
        # 可以进行参数检查奥
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError("bad score")

# _单下划线开头的实例变量外部可以访问 但按照规矩 这种我们应该看做私有的 别随意访问
# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量
bart2=Student2("liyanda",100)
print(bart2.get_name())
# bart2.__name="hhh"
# print(bart2.get_name())
# print(bart2.__name) 这三句话我们这样理解 其实38行是我们新给bart2设置了一个__name变量
# 这个变量和class内部的__变量不是一个变量


# 练习
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def set_gender(self,gender):
        self.__gender=gender
    def get_gender(self):
        return self.__gender
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

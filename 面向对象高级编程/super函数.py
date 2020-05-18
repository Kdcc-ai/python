# 调用父类(超类)的方法！！ 在python中是为了解决多继承用的
class FooParent(object):
    def __init__(self):
        self.parent='I m the father'
        print("parent")

class Child(FooParent):
    def __init__(self):
        # super().__init__()
        # 输出
        print(self.parent)
        print('hhh')

Child()
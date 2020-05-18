class Student(object):
    # object代表他继承的那个类
    def __init__(self,name,score):
        # 第一个参数永远是self表示创建的实例本身
        # 因此在这个方法内部 就可以把各种属性绑定到self 因为self就指向创建的实例本身。
        self.name=name
        self.score=score
        # 有了这个方法 创建实例的时候就不能传入空的参数了
        # 必须传入与这个方法匹配的参数 但self不用传记好
        # 几号 在类中定义的参数第一个参数永远是实例变量self
    def print——score(self):
        print("%s %s"%(self.name,self.score))


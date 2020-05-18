class Mammal(object):
    pass
class Bird(object):
    pass

class Runnable(object):
    pass
class Flayable(object):
    pass

class Dog(Mammal,Runnable):
    def fly(self):
        print("Fliying....")

# Mixln  混入单重继承额外的功能 就使用多重继承
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
# 类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass


# 哈哈哈 Python自带的很多库使用了Mixln
# python自带了TCPServer和UDPServer这两类网络服务
# 而要同时服务多个用户就必须使用多进程或多线程模型 这两种模型由FoekingMinIn和ThreadingMixIn提供
# 通过组合 我们就可以创造出合适的服务来
# class MyTCPServer(TCPServer,ForkingMixIn):
#     pass
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass


class Base():
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__() # 1
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__() # 2
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__() # 3
        print('C.__init__')

if __name__ == '__main__':
    c = C()
# # 输出
# Base.__init__
# B.__init__
# A.__init__
# C.__init__
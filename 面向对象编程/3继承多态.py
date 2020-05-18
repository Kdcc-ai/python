# python中的继承
class animals(object):
    def __init__(self,gentawi):
        pass
    def run(self):
        print("woshi animals")
# class dog(animals):
#     pass
# class cat(animals):
#     pass
# 易


class Dog(animals):
    def run(self):
        print("woshi dog")
class Cat(animals):
    def run(self):
        print("woshi cat")
# 多态：多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
# 由于Animal类型有run()方法，
# 因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：

# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数


# 这很牛逼 对于静态语言如Java 如果5行传入animals类型 那么必须是animals类或者他的子类
# 但对于python这样的动态语言来说则不一定要传入animals类型 我们只需要保证传入的对象有一个run()方法就行
# 比如：
class timer(object):
    def run(self):
        print("start....")

def run_twice(animals):
     animals.run()
     animals.run()
#这样理解：def run_twice(animal):里面的animal理解不应该是class Animal,它实质就像是C语言中的形参，和class Animal没有半毛钱关系。
# 就像class people一样，只要有run方法的都可以被def run_twice(animal)调用。

   
# 对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。
# 许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
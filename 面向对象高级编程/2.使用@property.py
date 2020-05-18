# 在前几节对于属性绑定 只需要直接用比如s.score=100等
# 这样就直接暴露出去了

# 另外 前几节对于设置某一属性为私有属性在构造方法中我们可以用
# self.__name=name的形式

# 我们设置属性时 使用类中的函数设置属性能够进行参数的检查
class Student(object):
    def get_score(self):
         return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# s=Student()
# s.set_score(1111) 会报错咯




# @property装饰器就是负责把一个方法 变成 属性调用的
# 就是说你调用属性的时候实际上调用的是方法 例子如下
class Student(object):
     @property
    #  负责把getter方法变成属性
     def score(self):
        return self._score
     @score.setter
    #  负责把setter方法变成属性
     def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s=Student()
s.score=11
# 注意理解 score方法已经被变为属性了 故37行直接调用属性即可
# 实际上转化为s.set_score(60)
print(s.score)
# s实际上转化为s.get_score()

# 注意到这个神奇的@property，我们在对实例属性操作的时候，
# 就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

# 还可以定义只读属性 只定义getter方法 不定义setter方法
# 例如
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2015-self._birth

# @property调用者写出简短的代码 保证对参数进行必要的检验
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
       return self._height*self._width
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
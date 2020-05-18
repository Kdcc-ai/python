# 当我们需要定义常亮时 一个办法使用大写变量用过整数来定义。。
# 比如定义12个月 显得麻烦

# 所以有个好方法 是为这样的枚举类型定义一个class类型
# 每个常量都是class的唯一实例
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样 我们就获得了Month 类型 的 枚举类 可以直接用 Month.Jan来引用一个常亮
# 或者枚举他的所有成员：
print(Month.Jan)
print(Month['Jan'])
print(Month.Jan.value)
print(list(Month))
for name,member in Month.__members__.items():
    print(name,'=>',',',member.value)
# value属性则是自动 赋给 成员的int常量 默认从1开始计数

# Enum派生出自定义类
from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
# @unique装饰器帮助我们检查保证没有重复值
# 访问这些枚举类型有若干种方法
print(Weekday.Mon)
print(Weekday['Mon'])
print(Weekday(1))
print(Weekday.Tue.value)
for name,member in Weekday.__members__.items():
    print(name,'=>',member)



# 练习：
# 把Student的gender属性改造为枚举类型，可以避免使用字符串
@unique
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')



# 补充 枚举类型可以看做是一种标签或者是一系列常量的集合 
# 通常用于表示某些特定的有限集合
class Color:
    RED   = 1
    GREEN = 2
    BLUE  = 3
# 这样也可以呀！！！
# 不过这样有弊端  可以被修改对吧？
# 最好的方法：
from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
print(Color.red)
print(repr(Color.red))
print(type(Color.red))
print(isinstance(Color.red,Color))
#枚举类型不可实例化 不可更改

# 定义枚举 成员名不允许重复
# class Color(Enum):
#     red = 1
#     green = 2
#     red = 3    # TypeError: Attempted to reuse key: 'red'

# 成员值允许相同 第二个成员的名称被视作第一个成员的别名
class Color(Enum):
    red   = 1
    green = 2
    blue  = 1
print(Color.red)
print(Color.blue)
# 输出Color.red
print(Color.red is Color.blue)
# True
print(Color(1))
# Color.red

# 若不能定义相同的成员值，可以用unique装饰
# from enum import Enum, unique
# @unique
# class Color(Enum):
#     red   = 1
#     green = 2
#     blue  = 1  # ValueError: duplicate values found in <enum 'Color'>: blue -> red


# 枚举比较 枚举的成员可以通过is同一性 或通过==比较
# 不能进行大小比较

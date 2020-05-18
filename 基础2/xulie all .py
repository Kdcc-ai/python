# 列表，元组，和字符串都能分片 可以分片 统称为序列
# 一些方法都是共用的
#Python中的指向机制一定的理解好，对于某些方法我们才会懂得原理 


# list()方法,把一个可迭代对象转换成一个列表
# 没参数默认生成一个空列表. 每一次对过程重复称之为一次迭代，每一次迭代的结果都会成为下一次迭代的初始值
# tuple()方法,把一个可迭代对象转换成一个元组
# str() 方法

a=list()
print(a)
b="I love fishc"
b=list(b)
print(b)
print(max(1,2,3,4,5))
print(max(b))
# max() min() sum()方法中的参数类型是统一的,可以全部都是整形,浮点数，字符串，元组，序列！！！
a=[1,2,4,5,0]
b=[3,2]
print(max(a))
# 参数是两个列表的话只比较列表中的第一个元素的大小,min函数也一样的
print(max(a,b))
# c=[123,23,4,"A"]
# print(max(c)),24 25行代码错误
print(sum(a))
print(sum(a,8))
# 同样出现错误int str没法相加
# print(sum("123456"))

print(sorted(a))

# reversed() enumerate() zip()返回一个迭代器,转换成列表
# 35行代码之后a已经反转,之后再进行反转,记住区别
a.reverse()
print(a)
print(list(reversed(a)))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# 输出[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))       # 下标从 1 开始
# 输出[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
print(list(zip(a,b)))
# print(zip(a,b)),输出显示<zip object at 0x00000251DBEE9AC8>


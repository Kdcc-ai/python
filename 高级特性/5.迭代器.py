from collections.abc import Iterator
from collections.abc import Iterable
# 我们知道 可以直接作用于for循环数组类型
# 集合：list tuple dict set str
# generator：生成器和带yield的generator function
# 可以直接作用于for循环的对象成为可迭代对象：Iterable
# # 要理解：直接作用于for循环的对象成为可迭代对象
# 可以使用isinstance()判断一个对象是否是Iterable对象：
print(isinstance([],Iterable))
# .....

# 要理解：可以被next()函数不断返回下一个值的对象成为迭代器对象：Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象：
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([1,2,3],Iterator))
# 可迭代对象 迭代器有啥区别？？？？为什么list dict str等数据类型不是迭代器？？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

# 分享：未懂
from itertools import groupby as love #导入函数groupby 指定别名 love
def add(x): #定义一个函数
    if x > 180:
        return '高'
    elif x < 160:
        return '矮'
    else:
        return '中等'
a=[191,158,159,165,170,177,181,182,190] #创建一个列表
a=sorted(a,key=add) #排序列表
print(a)
c=love(a,key=add) #创建迭代器
print(c)
for x,y in c:
    print(x)
    print(list(y))


d = {'a': 1, 'b': 2, 'c': 3}
# iter each key:
print('iter key:', d)
for k in d.keys():
  print('key:', k)
# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)
# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [[1, 1], (2, 4), (3, 9)]:
    print(x, y)
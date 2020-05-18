# collections 集合模块 提供了很多 集 合 类

# 1.namedtuple (tuple变形)
from collections import namedtuple
# namedtuple是一个函数 用来创建一个自定义的tuple对象 并且规定了tuple元素的个数
# 通过属性名进行输出
Point=namedtuple('Point',['x','hhhh'])
Point2=namedtuple('Point2',['x','y','z'])
p2=Point2(1,2,3)
p=Point(1,2)
print(p.x)
print(p.hhhh)
print(p2.x)
print(p2.y)
print(p2.z)
# 我们想 这样用namedtuple很方便的定义一种数据类型
# 首先具备tuple的不变性 其次可以通过属性引用
Circle=namedtuple('Circle',['X','Y','Z'])

# 2.deque（list变形（list索引访问元素 插入删除元素很慢））
# (双向列表 适用于队列和栈)
from collections import  deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.pop()
q.popleft()
print(q)

# 3.defaultdict（dict变形（使用dict时 如果Key不存在 你还去引用它 会抛出KeyError））
# （Key不存在 返回一个默认值）
from collections import  defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])
# 输出'N/A' 默认值调用函数时返回 函数在创建defaultdict对象时传入
# 它只是dict的拓展 不传入默认值的时候跟dict一样

# 4.OrderedDict（有序的dict）
from collections import OrderedDict
# dict的key 是无序的
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# OrderedDict的key 是有序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# 例子 实现一个FIFO的dict（先进先出）容量超出限制，最早删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capccity=capacity
    def __setitem__(self, key, value):
        # 按一定的方式存储和key相关的value
        # __setitem__是在设置类实例属性(类似a['k']='kk'之类的)的时候调用的
        # __getitem__是在调用类实例属性(类似t=a['k']之类的)的时候被调用的
        # https://blog.csdn.net/weixin_42557907/article/details/81589691
        containsKey=1 if key in self else 0
        # 这语句真妙。。。 完全保证集合容量不超范围 并且对于下面添加元素也有帮助
        if len(self)-containsKey>=self._capccity:
            last=self.popitem(last=False)
            # 删除用popitem函数 并且设置参数last=False大概意思是删除第一个吧
            print('Romove',last)
        if containsKey:
            # 集合中有这个key-value 进行更新
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)

#5.ChainMap（一组dict串起来组成一个逻辑上的dict 它本身也是一个dict）
# （查找的时候 会按照顺序在内部的dict依次查找）
# （一连串的dict 这么理解）
# 应用程序往往需要传入参数 参数可以通过命令行传入 看可以通过环境变量传入 还可以有默认参数
# 使用ChainMap实现参数的优先级查找
# 先查找命令行参数->(如果没有传入)查找环境变量—>(如果没有)使用默认参数

# ChainMap用法详见 !!关于命令行.py!!

# 6.Counter（计数器 可以统计字符出现的个数）
# 本质也是dict的子类
from collections import Counter
d=Counter('aababc')
print(d)
c=Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
c.update("hello")
print(c)
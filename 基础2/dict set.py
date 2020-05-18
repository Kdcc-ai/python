# 在list中，我们是按一页一页的查字典样子进行查询的
# dict字典 用键-值存储,具有极快的查找速度.
# 例如:前边是键 后边是值

# 这种key-value存储方式，
# 在放进去的时候，必须根据key算出value的存放位置(内存地址 然后直接将95取出来)
# 这样，取的时候才能根据key直接拿到value。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 输出95

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
# d['Adam'] = 67
# d['Adam']
# 输出67

# 如果key不存在，dict就会报错：
# >>> d['Thomas']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Thomas'

# 要避免key不存在的错误,有两种方法,一是通过in判断
# 二是通过dict提供的get()方法
# >>> 'Thomas' in d
# 输出False
# >>> d.get('Thomas')
# >>> d.get('Thomas', -1)
# 输出-1

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
# >>> d.pop('Bob')
# 输出75
# >>> d
# 输出{'Michael': 95, 'Tracy': 85}

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# dict的key必须是不可变对象。因为我们要通过key计算value的存储位置(字符串 整数)
# 通过key来得到value的存储位置 然后将value值取出来

# list不能作为key
# >>> key = [1, 2, 3]
# >>> d[key] = 'a list'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'






# set和dict类似，也是一组key的集合，
# 但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：理解为set这个类型对于其包含的数据的一个形式上的要求，list中的元素作为了set的key
# >>> s = set([1, 2, 3])
# >>> s
#输出 {1, 2, 3} 无重复元素 重复元素自动过滤
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
# >>> s.add(4)
# >>> s
# 输出{1, 2, 3, 4}
# >>> s.add(4)
# >>> s
# 输出{1, 2, 3, 4}
# 通过remove(key)方法可以删除元素：

# set可以看作数学亿以上的无序和无重复元素的集合,所以两个set可以做交集并集操作


# set和dict的区别
# set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
a=set([1,2,3])
b=set((1,2,3))
print(b)
# 将list放入set,会出错, 比如a.add([1,2,3]),因为list是可变的








# 不可变对象：str是不可变对象 可变对象：list是可变对象
# >>> a = 'abc'
# >>> a.replace('a', 'A')
# 'Abc'
# >>> a
# 'abc'
# 虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'，应该怎么理解呢？
# 我们先把代码改成下面这样：
# >>> a = 'abc'
# >>> b = a.replace('a', 'A')
# >>> b
# 'Abc'
# >>> a
# 'abc'
# 要始终牢记的是，a是变量，而'abc'才是字符串对象！
# 有些时候，我们经常说，对象a的内容是'abc'，
# 但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：

# 当我们调用a.replace('a', 'A')时，
# 实际上调用方法replace是作用在字符串对象'abc'上的，
# 而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
# 相反，replace方法创建了一个新字符串'Abc'并返回，
# 如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：


# 练习：tuple虽然是不变对象，
# 但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
a=set([1,2,3])
# 将tuple这个不变对象放入set中 输出{1, 2, 3, (1, 2, 3)}，这是可以的
a.add((1, 2, 3))
print(a) 
# 将tuple=(1,list)装入a这个set,因为list可变,所以不能存入set中
# 故a.add((1, [2, 3]))报错

d={
    "a":95,
    "b":75,
    "d":65
}
# 这块要转义 记好咯 print("d[\"a\"]=",d["a"])
# 这块要转义 记好咯print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
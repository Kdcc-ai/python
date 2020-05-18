# itertools提供了非常多有用的用于操作 迭代对象 的函数
# 返回值是iterator 通过for循环得值

# 1. itertools提供的几个无限迭代器 count()
import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)
#  cycle()把传入的一个序列无线重复下去:
cs = itertools.cycle('ABC')
for c in cs:
    print(c)


#  2.repeat()负责把一个元素无限重复下去 提供第二个参数就可以限定重复次数
ns = itertools.repeat('A',3)
for n in ns:
    print(n)
# 迭代要理解 这个无限序列只是再for迭代时才会无线迭代下去 如果只是创建了一个迭代对象
#            它不会把无限个元素生成出来 事实上也不可能在内存中创建无限多个元素

# 3.takewhile()函数根据条件判断来截取一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))


# 4.chain()迭代器操作函数 可以把一组迭代对象串联起来 形成一个更大的迭代器
for c in itertools.chain('ABC','XYZ'):
    print(c)


#  5.groupby()把迭代器中相邻得重复元素挑出来放在一起
#  通过函数完成 ：作用于函数的两个元素返回的值相等
#                这两个元素就是在一组的 并且函数返回值作为组的key
for key,group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))
# 输出A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']
# 忽略大小写进行分组
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
     print(key, list(group))



# 练习 计算这个序列的前N项和
import itertools
def pi(N):
    natuals = itertools.count(start=1,step=2)

    odd = itertools.takewhile(lambda x:x<=2*N-1,natuals)

    sum = 0
    i = 1
    for od in odd:
        sum = sum +4/(od)*i
        i = i*(-1)
    return sum
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


# 如果给定一个list或tuple，
# 我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# Python的for循环不仅可以用在list或tuple上，
# 还可以作用在其他可迭代对象上。
# 只要是可迭代对象，无论有没有下标都可以迭代，比如dict就可以迭代

# 默认情况下，dict迭代的是key。
# 如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。


# 所以如何判断可迭代对象呢？？？
# >>> from collections import Iterable
# >>> isinstance('abc', Iterable) # str是否可迭代
# True
# >>> isinstance([1,2,3], Iterable) # list是否可迭代
# True
# >>> isinstance(123, Iterable) # 整数是否可迭代
# False

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

def findMinAndMax(L):
    if len(L)==0:
      return (None,None)
    i=L[0]
    j=L[0]
    for k in L:
        if k<i:
          i=k
        if j<k:
          j=k
    return (i,j)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# 通过列表生产式,可以创建一个列表
# 但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。


# 所以如果列表中的元素可以按照某种算法推算出来,
# 就可以在循环的过程中不断推算后续的元素


# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。


g = (x * x for x in range(10))
print(next(g))
print(g)
# 输出<generator object <genexpr> at 0x0000013BBDEAC9A8>
# g也是一个可迭代对象
for n in g:
    print(n)
# 所以，我们创建了一个generator后，基本上永远不会调用next()，
# 而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

# Python很美,收获：赋值方式
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
# a, b = b, a + b   相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
fib(5)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print("第一步")
    yield 1
    print("第二步")
    yield 2
    print("第二步")
    yield(5)
# 调用时 生产一个generator对象,然后用next()不断获得下一个返回值
# odd是一个生成器
for n in fib2(6):
    print(n)
# 但是这样子拿不到return语句的返回值~~！


# 作业 输出杨辉三角
def triangles():
    L=[1]
    while True:
        yield L
    
        L=[1]+[L[n]+L[n+1] for n in range(len(L)-1)]+[1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
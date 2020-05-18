from functools import reduce
# map()接收两个参数 一个是函数 一个是Iterable
def f(x):
 return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 返回的是一个Iterator
print(list(r))
# Iterator是惰性序列 因此通过list()函数计算出结果
# 这么理解 map作为高阶函数  事实上把运算规则抽象了,
# 因此,我们不但可以计算简单的f函数还可以极端任意复杂的函数

q=list(map(str,[1,2,3,4,5,6,7,8,9]))
print(q)
# 转换成字符串

# reduce函数吧一个函数作用在一个序列上,这个函数必须接收两个参数
def f2(x,y):
    return x*10+y
print(reduce(f2,[1,3,5,7,9]))
# 输出13579

# 继续思考 利用map,reduce将str转换为int
def fn(x,y):
    return x*10+y
def char2num(s):
    
    return digits[s]
print(reduce((fn),map(char2num,"13579")))


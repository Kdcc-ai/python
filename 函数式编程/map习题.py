from functools import reduce
# 第一题
def normalize(name):
    s=name[0].upper()+name[1:].lower()
    return s
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习二
def prod(L):
    def add(x,y):
        return x*y
    return reduce(add,L)
    # 每次作用list中的两个元素
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习三 编写str转换成float数据的函数
# 方法一：
s='123.456'
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,list(map(char2num,s)))
# 先返回整数形式
def str2float(s):
 L=[]
 po=0
 for char in s:
    if char=='.':
        po=len(s)-len(L)-1
        continue
    L.append(char)
 return str2int(L)/10**po
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS2 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}
# 方法二 太牛逼了
def str2float2(s):
    nums=map(lambda ch:DIGITS[ch],s)
    point=0
    def to_float(f,n):
        nonlocal point
        if n==-1:
            point=1
            return f
        if point==0:
            return f*10+n
        else:
            point=point*10
            return f+n/point
    # reduce函数也有一个默认参数
    return reduce(to_float,nums,0.0)
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))






def fn(x):
    return x*x
print(list(map(fn,[1,2,3,4,5,6,7,8,9])))
# 筛选回数
def is_palindrome(n):
    str1=str(n)
    return str1==str1[::-1]
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


# Python中的挨式筛法
# 思路 1 2不是素数 1.先构造一个生成器（惰性序列）用于表示全体自然数的集合，从3开始
# 2.其次需要一个筛选函数
# 3.最后再构造一个生成器用于返回下一个素数
def oddproduce():
    n=1
    while True:
        n=n+2
        yield n

def shaixuan(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it=oddproduce()
    while True:
        n=next(it)
        # 返回下一个数值
        yield n
        it=filter(shaixuan(n),it)

for n in primes():
    if n<1000:
        print(n) 
    else:
        break



def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))
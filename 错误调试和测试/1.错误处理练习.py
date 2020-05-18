# 小结：python通过内置的tye...except...finally来处理错误
# python可以主动抛出错误

# 练习根据一项信息进行分析 定位出错误源头 并且修复
# 方法一：
from functools import reduce
import logging
import json
def str2num(s):
    try:
     return int(s)
    except ValueError as e:
     return float(s)
def calc(exp):
    ss = exp.split('+')
    # 返回一个列表
    ns = map(str2num, ss)
    print(list(ns))
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
print(eval('100+5.6'))
# 方法二：使用json 将字符串自动转为最符合的数据类型
def str2num(s):
    return json.loads(s)
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)
def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
        logging.exception(e)
main()
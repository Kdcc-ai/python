# >>> [x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 就是生成一个列表。
# >>> [x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]
# 生成仅偶数的平方
# >>> [m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# 理解其实本质上就是二重循环

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir(".")])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s,str)])
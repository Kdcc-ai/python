# 啥是文档 文档里面有一些模块的示例代码
# 这些代码与 其他的说明什么的可以写在注释中 然后由一些工具来自动生成文档

# 那么如何执行卸载注释中的这些代码？
# python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并且执行
# doctest严格按照Python交互式命令行的 输入 和 输出 来判断测试结果是否正确。

# 那么我们来测试上次编写的Dict类：
# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
# 什么输出都没有 正确
# 把__getattr__函数注释掉 就会出现错误
# 当模块正常导入时 doctest不会被执行。因为__name__=='__main__'不成立 这个前面讲过了
# 故不用担心doctest在非测试环境下执行

# 练习 对函数fact(n)编写doctest并执行
def fact(n):
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
       ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# 这章讲了错误处理 调试(这之前接触过)
# 单元测试、文档测试要知道 会写简单的。要再写几个单元测试、文档测试练练手
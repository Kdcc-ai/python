# 单元测试 就是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作

# 比如对函数abs()，我们可以编写出以下几个测试用例：
# 输入正数，比如1、1.2、0.99，期待返回值与输入相同；
# 输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
# 输入0，期待返回0；
# 输入非数值类型，比如None、[]、{}，期待抛出TypeError。
# 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。（所以说 用来测试的不也是个类吗？)



# d = Dict(a=1, b=2)
# 下面我们编写一个Dict类 这个类的行为要和dict一样
# >>> d['a']
# 1
# >>> d.a
# 1 但是我们可以通过属性来访问 666
class Dict(dict):

    def __init__(self,**kw):
         super(Dict,self).__init__(**kw)
    def __getattr__(self,key):
         try:
            return self[key]
         except KeyError:
             raise AttributeError(r"'Dict' object has no attribute:%s" % key)
    def __setattr__(self,key,value):
         self[key]=value
        # 已经编写好了一个类

# 并且为了编写单元测试 我们需要引入python自带的unittest模块
# import sys
# sys.path.append('D:\\Python程序\\错误调试和测试\\MyDict.py')

import MyDict
import unittest
class TestDict(unittest.TestCase):
# 继承
    #  def setUp(self):
    #     print('setup...')
    #  def tearDown(self):
    #     print('tearDown...')
    # 这两个方法我放在这里了 取消注释通过输出结果发现者两对方法出现了4次
    # 也就意味着调用了4次调试方法。。节约代码
     def test_init(self):
         d=Dict(a=1,b='test')
         self.assertEqual(d.a,1)
         #断言函数判断返回的结果是否等于1
         self.assertEqual(d.b,'test')
         #断言函数判断返回的结果是否等于'test'
         self.assertTrue(isinstance(d,dict))
         #断言函数判断d是否是dict类  
         #初始化
     def test_key(self):
         d=Dict()
         d['key']='value'
         self.assertEqual(d.key,'value')
         #自己初始化后 断言函数判断d.key是否等于value  
     def test_attr(self):
         d=Dict()
         d.key='value'
         self.assertTrue('key' in d)
         self.assertEqual(d['key'],'value')
     def test_keyerror(self):
         d=Dict()
         with self.assertRaises(AttributeError):
            # 期待抛出指定类型的Error 通过d.empty访问不存在的key时 我们期待抛出AttributeError
             value=d.empty
            # 编写单元测试时 需要写一个测试类 继承unittest.TestCase
            # 并且要注意 以test开头的方法就是测试方法 不以test开头的方法不被认为是测试方法
            # 测试类测试类用来测试这个Dict功能是否正确的类
            # 所以说 我们将以test__×××()开头的方法看做是测试方法  对每一个用例都编写一个测试方法
            # 而测试方法中用unittset.TestCase提供的方法来进行判断
unittest.main()
# 这块要父类unittest.main()
# if __name__=='__main__':
#     unittest.main()

#一种重要的断言：期待抛出指定类型的Error 通过 d['empty']访问我们期待抛出KeyError
# with self.assertRaises(KeyError):
#     value=d['empty']
# 就这样写


# 运行单元测试 一旦编写好 我们用这个单元测试去测试那个类
# 好的 我们直接运行就可以了 输出OK 但是为社么没使用74 75行那种代码呢 岂不更严谨
# 主要还是vs code没法导入MyDict模块中的类 不知道为什么 就这样先替代了



# 在编写单元测试中有两个特殊的setUp()和tearDown()方法
# 这两个方法可以分别在每调用一个测试方法前后被执行
# 那么这两个方法有什么用呢？？设想你的测试需要启动一下数据库 那么我们
# 可以在setUp()中打开数据库  在tearDown()中关闭数据库 这样就不用重复相同的代码了。。。。
# 奥是这样子
# class TestDict(unittest.TestCase):
#     def setUp(self):
#         print('setup...')
#     def tearDown(self):
#         print('tearDown...')






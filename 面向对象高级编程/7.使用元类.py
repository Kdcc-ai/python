# 动态语言和静态语言最大的不同 就是函数和类的定义
# 不是编译时定义的 而是运行时动态创建的

# 举个例子是这样的
# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)

# 当python解释器载入hello模块的时候
# 是依次执行该模块的语句的
# # 执行结果就是动态创建出一个Hello的class对象
# >>> from hello import Hello
# >>> h = Hello()
# >>> h.hello()
# Hello, world.
# >>> print(type(Hello))
# <class 'type'>
# >>> print(type(h))
# <class 'hello.Hello'>

# type()函数既可以返回一个对象的类型 又可以创建出新的类型
# 比如：
# 通过type()函数创建出Hello类
def fn(self,name="World"):
    print('hello,%s' % name)
Hello=type('Hello',(object,),dict(hello=fn))
# 创建出Hello class
h=Hello()
h.hello()

# ?是意思呢？ 要创建一个class对象 type()函数依次传入3个参数：
# 1 class的名称；
# 2 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3 class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的,因为python解释器遇到class的时候也是调用type()函数创建出class的

# 动态语言和静态语言不同 是动态语言支持运行期创建类




# metaclass
# type()是动态创建类
# 41行名称叫元类
# 一般来说 定义类->创建实例

# 创建类:定义metaclass->创建类->创建实例
# 换句话说 你可以把类看做是metclass创建出来的实例

# 1.定义ListMetaclass
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # __new__()方法接收到的参数依次是：
        # 当前准备创建的类的对象；
        # 类的名字；
        # 类继承的父类集合；
        # 类的方法集合。
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
# 定义类的时候还要指明使用ListMetaclass来定制类
class MyList(list,metaclass=ListMetaclass):
    pass
# 有了关键字参数metaclass时魔术就生效了
# 他指示python解释器在创建MyList时通过ListMetaclass.__new__()来创建
# 并且！！！就在这(那个新的方法)我们就可以修改类的定义：加上新的方法等 返回修改后的定义


L=MyList()
print(L)
L.add(1)
print(L)
# 而普通的list就没得add方法
# ORM就是用metaclass修改类的定义的 ORM是对象-关系映射 
# ORM就是把关系数据库的一行映射为一个对象 也就是一个类对应一个表
# 所以我们要编写一个ORM框架 所有的类只能动态定义 
# 因为只有使用者才能根据标的结构定义处对应的类来。。理解好





# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，
# 剩下的魔术方法比如save()全部由metaclass自动完成。
# 虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。

class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
        # 数据库表的字段名和字段类型
    def _str_(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 子类重写__init__时 要继承父类的构造方法使用super关键字
# super(子类,self).__init__(参数1，参数2，...)
# 利用继承 定义各种类型的Field(字段)
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')
        # 可变长字符串
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
        # 长整型数字
# 编写最复杂的ModelMetaclass：
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print("Found model: %s" % name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print("Found mapping: %s ==> %s"%(k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings
        # 保存属性和列的映射关系
        attrs['__table__']=name
        # 假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)
# 基类Model
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    # 继承的是dicf类
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)' %(self.__table__,','.join(fields),','.join(params))
        print('SQL: %s'%sql)
        print('ARGS: %s'% str(args))

    #User类使用父类Model中定义的metaclass的ModelMetaclass来创建
    # metaclass可以隐式继承到子类


# 编写一个ORM框架
# 编写底层框架：1.先写出来调用接口 
# 比如使用者如果使用这个ORM框架 定义一个User类操作对应的数据库表User,我们期待他写出这样的代码
class User(Model):
    # 定义类的 属性 到 列 的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

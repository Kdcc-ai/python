# 程序运行过程中 所有的变量都是在内存中 这要明白

# d = dict(name='Bob', age=20, score=88) 这个类
# 我们在实例化这个类的时候 可以随时修改变量 比如把name改成bill
# 程序结束 变量所占用的内存被操作系统全部回收 如果没有吧bill存到磁盘上下次重新运行程序，变量又被初始化为Bob

# 我们把变量从内存中 变成 可以 存储或传输的过程 称之为序列化pickling
# python中叫pickling 序列化之后的内容可以写入磁盘或者通过网络传输到别的机器上
# 把变量内容从序列化的对象重新读到内存里称之为反序列化 unpickling


# python中使用pickle模块来实现序列化。
import pickle
d=dict(name='Bob',age=20,score=100)
# print(d)
print(pickle.dumps(d))
# 16行输出python字节类型的数据 结合前面知识,如果要保存到磁盘或者在网络上传输,必须使用字节为单位的数据
# pickle.dumps(d)方法把任意一个对象序列化成一个bytes
#  然后把bytes写入文件或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f=open('D:\\Python程序\\算法.txt','wb')
pickle.dump(d,f)
f.close()
# 总结步骤：1.实现序列化 2.用wb方式打开文件 3.调用方法写入文件 4.关闭文件对象
# 写进去了 但都是一些乱七八糟的内部信息 这些信息是python保存的对象内部信息

# 把对象从磁盘读到内存时(时刻记住程序在运行中 所有变量都是保存在内存中的),可以先把内容读到一个bytes,然后用pickle.loads()方法反序列化出对象。
# 或者直接使用pickle.load()方法从一个file-like Object中直接反序列化出对象
f=open('D:\\Python程序\\算法.txt','rb')
d=pickle.load(f)
f.close()
print(d)
# 总结步骤：1.用rb方式打开文件 2.调用方法反序列化出对象 3.关闭文件对象
# 通过输出发现变量的内容又回来了！ 这个变量≠原来的的变量 只是内容相同



# JSON。。？？JSON
# 如果我们要在不同的编程语言之间传递对象,就必须把对象序列化为标准格式,比如XML。
# 但更好的方法是序列化为JSON,因为JSON表示出来就是一个字符串。
# 可以被所有语言读取 (把对象转化为JSON表示) 可以方便地存储到磁盘或者通过网络传输

# JSON不仅是标准格式 而且比XML块 而且可以在Web界面中读取
# JSON表示的对象就是标准的js语言的对象
# JSON和python内置的数据类型有着一一对应的关系,比如说：
# {}(JSON类型)=>dict(python类型) []=>list "string"=>str 1234.56=>int或float true/false=>True/False null=>None


# 学习Python内置的json模块提供了非常完善的Python对象=>JSON格式的转换
# 接下来我们看看Python内置的json模块是如何将Python对象->JSON格式
import json
d=dict(name='Bob',age=20,score=88)
print(json.dumps(d))
# 这块dumps返回一个str 内容是标准的JSON格式！！

# JSON反序列化->python对象 用loads()方法：把JSON的字符串反序列化
# 用load()方法：从file-like Object中读取字符串并反序列化
json_str='{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str))

# 总结：由于JSON标准规定的JSON编码是UTF-8,所以我们总是能正确地在Python的str与JSON的字符串之间相互转化



# JSON进阶：通过上面我们知道了JSON的dict对象可以直接序列化为JSON的{}
# 如何用把用class类表示的对象序列化呢？
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
# print(json.dumps(s))
# 抛出异常Student对象不是一个可序列化为JSON的对象
# 通过观察dumps方法发现 可选参数default就是把任意一个对象 变成 一个可序列化为JSON的对象
# 我们只需要为Student专门写一个转换函数 再把函数传入进去即可
def student2dict(std):
    return{
        'name':std.name,
        'age' :std.age,
        'score':std.score
    }
    # 这样Student实例->被student2dict函数转换成dict->被序列化为JSON
print(json.dumps(s, default=student2dict))


# 这样子倒是对了：但是我们下次再遇到另外一个类的实例 是不是还得写个转化函数
# 所以偷懒用lanbda函数就行 利用class实例具有的__dict__属性(这就是特殊用途了吧hh),他就是一个dict(存储属性的字典)
# ！！！定义了__slots__的class没有__dict__属性 因为引入__slots__用来指定实例只具有固定的属性
print(json.dumps(s,default=lambda  obj: obj.__dict__))

# 如何把JSON反序列化为一个Student实例呢？
# loads()方法首先转换出一个dict对象
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))







# 本节总结：python语言特定的序列化模块是pick 如果把序列化搞得更通用、更符合Web标准,就可以使用json模块
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。
# 当我们使用时，只需要传入一个必须的参数。
# 但是，当默认的序列化或反序列机制不满足我们的要求时，
# 我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。









# 练习 对中文进行JSON序列化时，
# json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj)
print(s)
# 
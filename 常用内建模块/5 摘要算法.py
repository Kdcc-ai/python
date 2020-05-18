# encode: 以某种编码格式对某字符串进行编码 返回字节类型对象
# decode:以某种编码对某字符串进行解码  返回字符串类型对象


# 1.摘要算法
# 是通过哈希算法 散列算法.它通过一个函数把任意长度的数据->一个长度固定的数据串
# (用16进制的字符串表示)
# 摘要算法通过f()对任意长度的data->计算出固定长度的摘要digest
# (目的是为了发现原始data是否被人篡改过)
# 它能够指出原始data 因为计算出f(data)=digest容易 但是diget->data很难
#                   对原始数据做一个bit的修改 都会导致计算出的摘要完全不同

# 1.python中的hashlib模块提供了摘要算法MD5
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 分块多次调用也是可以的
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
print(len(md5.hexdigest()))
# 正好长度是32

# 2.python中的hashlib模块提供了摘要算法SHA1
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
# 用法类似
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 越安全的摘要算法 摘要长度更长 更慢

# 但是也有可能两个不同的数据 f(data)相等 但是很困难


# 讲了这么多 摘要算法有啥应用呢???
# 在数据库方面用的多 比如一个数据库表 数据库表中的元素用摘要如MD5保存 防止黑客窃取
# 用户登录->计算用户输入明文的MD5->对比就可以
# 但是采用MD5存储口令不一定就一定安全  。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？
# 但是(很多用户喜欢用123456 888888等密码)黑客可以计算出这些常用口令的MD5值 得到一个反推表

# 练习1(不安全的MD5编码)
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if md5.hexdigest() == db[user]:
        return True
    return False
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 练习2(更安全的MD5)
# 根据用户输入的用户名 口令模拟用户登录
import hashlib,random
db = {}
# 得到md5 字符串
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
# 每个人是一个类
class User(object):
    def __init__(self, username, password):
        self.username = username
        # chr函数用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
        # str函数把对象转换成字符串形式
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
#       加点盐
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')
def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')



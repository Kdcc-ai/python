# 和5节差不多 进行改进
# 第五节 我们再通过哈希算法计算MD5或SHA-1的时候 加了salt（为了避免黑客窃取）
# 这节课我们用Hmac代替我们自己的加salt算法（程序更安全 更标准）
# 如何代替的呢？ 把key混入计算当中（很巧妙）(其实和上一节差不多)

# 实例如下 key相当于上节课的secret
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
# 如果消息很长 调用h.update(msg)
print(h.hexdigest())

# hmac 和上一节的 hash算法类似
# 输出的长度和原始哈希算法长度一致
# 传入的一定要是bytes类型 str->bytes类型
import random
def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()
class User(object):
    def __init__(self,username,password):
        self.username = username
        self.key = ''.join([chr(random.randint(48,122)) for i in  range(20)])
        self.password=hmac_md5(self.key,password)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

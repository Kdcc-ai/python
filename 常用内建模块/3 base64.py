# Base64是一种用64个字符来表示二进制数据的方法
# 我们知道 记事本打开二进制文件（产生乱码）
#          因为二进制文件包含很多无法显示和打印的字符
# 如果我们希望记事本能处理二进制数据 就需要一个二进制->字符串的转换方法

# Base64是一种常见的！！二进制编码方法！！

# 原理
# 廖雪峰博客讲了 还不错 https://www.liaoxuefeng.com/wiki/1016959663602400/1017684507717184
# python内置的base64可以直接进行base64的编解码
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# 我们知道标准的Base64编码后可能会出现字符+ / 在URL中就不能作为参数
# 所以又出现了一种"url safe"的base64编码 就是把字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

#      由于=字符也可能出现在Base64编码中 =在URL Cookie里面会造成歧义
#      所以很多Base64在编码后会把=去掉
print(base64.b64encode(b'abcd'))
# 去掉=后怎么阶码呢? 因为Base64是把3个字节->4个字节
# 所以Base64编码的长度永远是4的倍数 所以加上=把Base64字符串长度变为4的倍数



# 小结 Base64是一种通过查表得编码方式 不能用于加密
#      Base64适用于小段内容的编码 比如数字证书签名 Cookie的内容等
#      Base64是一种任意二进制 -> 文本字符串的编码方法 用于URL Cookie 网页中传输少量数据

# （）练习（）
def safe_base64_decode(s):
    if len(s) %4 == 0:
        return base64.b64decode(s)
    else:
        s2 = str(s,encoding='utf-8')
        newlength=(len(s)//4+1)*4
        for i in range(newlength-len(s)):
             s2=s2+'='
        return  base64.b64decode(s2)
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')



# 验证email地址
import re
def is_valid_email(addr):
    if re.match(r'[a-z\.]+@[a-z\.]+\.com',addr)!=None:
        return True
    else:
        return False
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
# 评论区方法:末尾为.com 邮箱最后一个字符包含\w
mailaddr=re.compile('^\w[\w\_\.]*\w@\w+\.com&')


# 提取出带名字的Email地址
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
findandspi=re.compile('^<([a-zA-Z\s]+)>\s*\w+@([a-zA-Z]+)\.org$')
findandspi2=re.compile('([a-zA-Z]+)@([a-zA-Z]+)\.org$')
def name_of_email(addr):
    if findandspi.match(addr):
        return findandspi.match(addr).group(1)
    if findandspi2.match(addr):
        return findandspi2.match(addr).group(1)
    return None
   
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
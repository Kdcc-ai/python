#  3节 4节都是讲一些编码方面的知识的 对以后肯定有帮助的
# 3节 二进制(按字节存的)->(通过Base64法则)文本字符串
# 4节 二进制(按字节存的)—>其他数据类型（字符 64位整数...）
# b' '代表二进制数据 所以字节数组==b' ' 对吧

# python把32位无符号正数->字节（4个长度的bytes）
# 这么写
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# python提供了一个struct模块：bytes和其他二进制类型的转换
# 1.pack函数把任意数据类型变成bytes
import struct
print(struct.pack('>I',10240099))
# >I 是处理指令
#   >表示字节顺序是big-endian 也就是网络序
#   I表示4字节无符号整数
# 2.unpack把bytes变成相应的数据类型
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
#  >IH 是处理指令
#  I表示4字节无符号整数
#  H表示2字节无符号正数
# https://docs.python.org/3/library/struct.html#format-characters


# 练习1 文件夹中存在以BMP文件 另外BMP格式文件的存储头文件是有规律的
# 反正就是存储了30个字节的字节数据
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH',s))

# 练习2 检查文件是否是位图文件 如果是 打印图片大小和颜色数
import base64,struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
def bmp_info(data):
    info=struct.unpack('<ccIIIIIIHH', data[:30])
    if info[0]==b'B' and info[1]==b'M':
        infoma={}
        infoma['color']=info[9]
        infoma['width']=info[6]
        infoma['height']=info[7]
        return infoma
    return {
        'width': 200,
        'height': 100,
        'color': 24
    }
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')


# 小结：sys模块（sys.argv：存储命令行参数）
#       os模块（os.environ：环境变量）



# 1.sys模块有一个argv变量，用list存储了命令行的所有参数。
# argv至少有一个元素，因为第一个参数永远是该.py文件的名称
# argv存储了命令行参数
# inport sys 进行查找

#
# 2.argparse基本用法
# argparse 是python自带的命令行参数解析包，
# 可以用来方便地读取命令行参数。它的使用也比较简单。
# 先上代码
# import argparse
# def main():
#     parser=argparse.ArgumentParser(description='Demo of argparse')
#     parser.add_argument('-n','--name',default='Li')
#     parser.add_argument('-y','--year',default='20')
#     args=parser.parse_args()
#     print(args)
#     name=args.name
#     year=args.year
#     print('Hello {} {}'.format(name,year))
# if __name__=='__main__':
#     main()
# 参考博客 https://blog.csdn.net/yy_diego/article/details/82851661

# ChainMap与argparse
from collections import ChainMap
import os, argparse

# 缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}
# 命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
# vars() 函数返回对象object的属性和属性值的字典对象。
# namespace<->("user"=..,"color"=...) 字典生成器
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:（！ChainMap就是这么用的！详见dollections1.py文件）
# 第一个是命令行参数 第二个是环境变量 第三个是缺省参数
combined = ChainMap(command_line_args, os.environ, defaults)
# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
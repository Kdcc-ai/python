# 在程序的时候我们需要通过一些变量值是什么
# 来调试自己的程序
# 1.使用print函数


# 2.断言 凡使用print来辅助查看的地方都可以使用断言(assert)来代替
# def foo(s):
#     n=int(s)
#     assert n!=0,'n is zero'
#     return 10/n
# def main():
#     foo('0')
# # assert的意思就是 表达式n!=0应该是True 否则根据程序运行后面的程序会出现错误
# # 如果断言失败 assert语句本身就会抛出AssertionError异常
# main()
# 不过如果程序到处都有assert也不太好看 
# 不过，启动Python解释器时可以用-O参数来关闭assert：
# 记住断言的开关是-O 是英文大写字母O而不是0


# 3.logging, 在前一节我们知道logging可以记录错误信息 并不会终止程序
import logging
logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
# logging允许我们指定记录信息的级别 有debug info warning error
s='0'
n=int(s)
print(logging.info('n=%d'%n))
print(10/n)


# pdb python调试器pdb让程序以单步方式运行，可以随时查看运行状态


# 拓展

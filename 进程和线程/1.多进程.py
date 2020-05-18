# 进程是什么？多进程是什么
# 单核CPU多进程如何执行？单核CPU无法执行并行多进程
# 多核CPU：并行多进程

# 一个进程(任务)可包含多个线程
# 单核CPU多线程如何执行？单核CPU无法执行并行多线程(不知道有没这个名词)

# 多任务的实现：多进程模式 多线程模式 多进程多线程模式
# python支持多进程和多线程 这章我们会讨论如何编写这两种多任务程序


# 小结：进程->线程(最小的执行单位)
# ！！另外我们还要明白！如何调度进程和线程完全由操作系统决定 程序自己不能决定



# 多进程：multiprocessing
# 了解操作系统相关知识：
# Unix/Linux操作系统提供了一个fork函数系统调用：
# 调用fork()一次,返回两次;因为操作系统自动把当前进程(父进程)复制了一份(子进程)
# 然后分别在父进程和子进程内返回。子进程返回0 父进程返回子进程的ID
# 为什么这么做呢？？一个父进程可以fork出很多子进程,父进程记下了每个子进程的ID,子进程调用getppid()方法拿到父进程的ID
# 这样就是啥都满足了是吧！！

# 只能在Linux/Unix/Mac执行：
import os
# print('Process (%s) start...' % os.getpid())

# pid = os.fork()
# os.wait() 等待子进程结束释放资源
# if pid == 0: 子进程 返回0 getpid()方法拿到自己的ID 父亲的ID
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else: 父进程 返回子进程ID getpid方法拿到自己ID pid为子进程ID
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 第一次调用返回父进程,而父进程返回子进程的ID 执行33行代码
# 第二次调用返回子进程,而子进程返回0 执行31行代码
# 结果：
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.




# 在Windows上python也提供了多进程支持！！
# mutiprocessing模块提供了一个Process类 代表一个进程对象 所以Process对象不是进程
# 例子：启动一个子进程->等待其结束
from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 得到父进程ID(识别码)
    p=Process(target=run_proc,args=('test',))
    print(str(p.pid),str(p.ident))
    # 创建子进程,传入一个 执行函数(理解好这个名词 调用对象) 和 函数(调用对象)的参数
    # 后面args就是函数的参数 由于run_proc只有一个参数故我们传入一个元组
    # 如果传入的args='test' 会报错,因为run_proc只允许有一个参数
    # Procsee进程创建 子进程将主进程的对象完全复制一份 这样在主进程和子进程各有一个Process对象
    # p.start()启动的是子进程 主进程中的Process对象作为一个静态对象存在 不执行
    print('Child process will start')
    print(p.is_alive())
    p.start()
    print(p.is_alive())
    # join方法:等待子进程结束 继续向下进行
    # 和Java那个差不多 如果把这个join函数注释掉 可能会先输出64行(父进程这行)
    # 然后再输出子进程
    p.join()
    print('Chile process end.')



# 如果要启动大量的子进程 可以用进程池的方式批量创建子进程:
from multiprocessing import Pool
import os,time,random
# 什么鬼？？

def long_time_task(name):
    print('Run task %s (%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.'% os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
        # 主进程自己跑 不管子进程
        # 非阻塞式方法
    # 打印说明在跑进程
    print('Waiting for all subprocesses done...')
    p.close()
    # 对Pool对象调用join()方法会等待所有子进程执行完毕(用于阻塞父进程)
    # 调用join()方法之前必须先调用close()方法(否则会抛出错误Pool is still running) 并且调用close()之后就不能继续添加新的Process了
    # 并且如果不调用91行join()方法 输出的一直都是：
#     Parent process 1656.
#     Waiting for all subprocesses done...
#     All subprocesses done.
#    这说明子进程压根没执行到 父进程一直向下执行直到程序结束
    p.join()
    print('All subprocesses done.')
# 注意输出结果会发现task0 1 2 3 4是立即执行的,
# 而task4要等待前面4个task完成后执行。

# 这是因为我设置了Pool大小为4 提供4个进程提供用户使用
# 当有新的请求提交到Pool时,该请求等待,直到池中有进程结束,才会床创建新的进程
# Pool默认大小是CPU的核数



# # 子进程：刚才我们无论用Process还是Pool创建的都是程序本身的子进程。
# # 但有的时候子进程并不是本身 而是一个外部进程
# # subprocessing模块可以让我们非常方便地启动一个子进程 然后控制其输入和输出
# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# # 如果子进程还需要输入 则可以通过communicate()方法输入
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)







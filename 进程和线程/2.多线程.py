# # 启动一个线程就是把函数传入并创建Thread实例 然后调用start方法
# import time,threading

# # 新线程执行：把函数传入并创建Thread实例 调用start()方法

# def loop():
#     print('thread %s is running...'%threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s >>> %d'%(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended'%threading.current_thread().name)


# print('thread %s is running...'%threading.current_thread().name)
# # threading模块的current_thread()函数
# # 它永远返回当前线程的实例
# # 并且 主线程实例的名字叫MainThread 子线程的名字在创建时候指定,我们用LoopThread命名子线程

# t=threading.Thread(target=loop,name='LoodThread')
# t.start()
# t.join()
# print('thread %s end' % threading.current_thread().name)
# # 任意进程默认就会启动一个线程 我们把线程成为主线程 


# # 多进程和多线程的区别：理解多进程中同一个变量各有一份拷贝在每个进程中，互不影响
# #                      而多线程，所有变量由所有线程共享,任何一个变量都可以被任何一个线程修改
# # 记住线程之间的共享数据
# balance=0

# def change_it(n):
#     # 先存后取 结果应该为0
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for i in range(1000000):
#         change_it(n)
#     # 确实当n比较小的时候 运算出的balance就是0
#     # 但是由于线程的调度由操作系统决定
#     # t1 t2交替执行时,循环次数足够多,balance的结果就不一定了
# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# # 这样子输出结果不为0 为什么呢？
# # 高级语言的一条语句在CPU执行时 具体步骤 拿balance=balance+n来说
# # 1.计算balance+n 存入到临时变量x(我就说他是x)中
# # 2.将临时变量的值赋给balance
# # x=balance+n balance=x(x是局部变量 两个线程各有自己的x)
# # 但是！操作系统是交替执行的

# # 可能：初始值 balance = 0
# # t1: x1 = balance + 5  # x1 = 0 + 5 = 5
# # t2: x2 = balance + 8  # x2 = 0 + 8 = 8
# # t2: balance = x2      # balance = 8
# # t1: balance = x1      # balance = 5
# # t1: x1 = balance - 5  # x1 = 5 - 5 = 0
# # t1: balance = x1      # balance = 0
# # t2: x2 = balance - 8  # x2 = 0 - 8 = -8
# # t2: balance = x2   # balance = -8 当然这种情况需要在循环很多次可能出现
# # 比较少见
# # 其实就是 在执行修改balance的语句的时候 线程可能中断 从而导致多个线程把同一个对象的内容改乱了



# # 同样 和Java一样 可以使用锁:例如上面给各个线程的执行函数
# # 当我们给一个线程的change_it()函数上一把锁后
# # 另外一个线程执行change_it()时候 只能等待锁被释放后 获得该锁之后才能改
# # 锁 只有 一个！
# balance=0
# lock=threading.Lock()
# # 通过这个方法
# def run_thread(n):
#     def i in range(100000):
#         # 先获得锁
#         lock.acquire()
#         try:
#             # 放心更改
#             change_it(n)
#         finally:
#             # 锁一定要释放
#             lock.release()
# # 保证了某段关键代码只能由一个线程从头到尾地执行 
# # 但是坏处也很多 阻止了多线程并发执行,因为包含锁的某段代码实际上只能以单线程模式执行 效率大大降低
# # 其次 由于可以存着多个锁不用线程有不同的锁  当试图获取对方持有的锁时,可能会造成死锁 所有线程全部挂起
# # 导致多个线程全部挂起 既不能执行 也无法结束 只能靠操作系统强行终止



# 多核CPU
#用python写一个死循环线程 会%100占用一个CPU
# 如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
import threading,multiprocessing
def loop():
    x=0
    while True:
        x = x ^ 1
        
for i in range(multiprocessing.cpu_count()):
    t=threading.Thread(target=loop)
    t.start()
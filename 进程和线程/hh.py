import os
from multiprocessing import Process
def runpp(name):
    print ('Child process %s (%s) worked ' % (name,os.getpid()))
def mm() :
    print("Hello world! ")
    
mm()
if __name__ == '__main__':
    print('Mother process %s.' % os.getpid())
    for i in range(3):
        p = Process(target=runpp,args=('no'+str(i),))
        print ('Process %d will start.' % i)
        p.start()
    p.join()
print('End')
# 信号量

import  threading, time


semaphore = threading.BoundedSemaphore(5) #最多允许5个线程同时运行


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread: %s',n)
    semaphore.release()


for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()
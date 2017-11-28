import multiprocessing
import time


def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(3,))
   # 因子进程设置了daemon属性，主进程结束，它们就随着结束了。
    #p.daemon = True
    p.start()
    print("p.pid:", p.pid)
    print("p.name:", p.name)
    print("p.is_alive:", p.is_alive())
    print('end')
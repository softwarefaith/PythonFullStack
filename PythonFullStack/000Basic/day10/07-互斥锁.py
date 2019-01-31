#由于资源竞争
#子线程和主线程会产生资源竞争
#创建互斥锁:保证同一时刻,只有一个线程去执行代码
#这样全局便变量不会存在资源竞争问题
import threading
g_num = 0

#创建一个互斥锁
lock = threading.Lock()
#100000
def AA():
    #上锁
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    #释放锁
    lock.release()
    print("AA:",g_num)

#2000000
def BB():
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    lock.release()
    print("BB:", g_num)

if __name__ == '__main__':
    #创建两个线程
    first_thread = threading.Thread(target=AA)
    second_thread = threading.Thread(target=BB)

    first_thread.start()
    second_thread.start()



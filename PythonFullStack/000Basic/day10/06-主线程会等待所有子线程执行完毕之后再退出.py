import threading
import time

def AA():
    print("AA", threading.current_thread())
    print("AA,这个代码是在子线程中执行的")
    while True:
        print("AA")
        time.sleep(0.2)


if __name__ == '__main__':
    print("main",threading.current_thread())

    #创建子线程执行AA函数
    #daemon创建的时候就是守护线程
    t1 = threading.Thread(target=AA)
    #线程相关设置,都要放在线程启动之前
    #设置守护线程需要放在线程执行的代码之上,要不会出问题
    t1.setDaemon(True)

    t1.start()
    #设置守护线程,主线程退出会直接销毁不存在执行对应的代码

    time.sleep(1)
    print("over")


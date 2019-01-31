import multiprocessing
import time


def show(name):
    #这里的代码是在子进程里面执行的
    print("show:",multiprocessing.current_process())
    print(name)
    while True:
        print("哈哈")
        time.sleep(0.2)



if __name__ == '__main__':
    #这是在主线程中执行的
    print("main:", multiprocessing.current_process())
    sub_process = multiprocessing.Process(target=show,args=("张三",))
    #设置守护线程
    # sub_process.daemon = True
    sub_process.start()
    time.sleep(2)
    #让子进程终止,销毁子进程
    sub_process.terminate()
    print("over")



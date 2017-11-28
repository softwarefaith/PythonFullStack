from multiprocessing import Process
import time


class MyProcessing(Process):

    def __init__(self):
        super(MyProcessing, self).__init__()

    def run(self):
        print('hello', time.ctime())
        time.sleep(1)


if __name__ == "__main__":
    my = MyProcessing()
    my.start()
    my.join()
    print("p.pid:", my.pid)
    print("p.name:", my.name)
    print("p.is_alive:", my.is_alive())
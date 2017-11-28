"""
Queue和pipe只是实现了数据交互，并没实现数据共享，
即一个进程去更改另一个进程的数据。





"""

from multiprocessing import Process, Manager


def f(d, l, n):
    d[n] = n
    d["name"] = "xuyaping"
    l.append(n)

    # print("l",l)


if __name__ == '__main__':

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))
        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)


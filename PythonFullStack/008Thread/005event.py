import  threading
import  time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)


def worker(event):
    logging.debug("waiting")
    while not event.isSet():
        logging.debug("等待连接")
        event.wait(3)

    logging.debug("ready go")
    time.sleep(1)


def main():
    event = threading.Event()

    t1 = threading.Thread(target=worker,args=(event,))
    t1.start()
    t2 = threading.Thread(target=worker,args=(event,))
    t2.start()

    logging.debug("Checking")
    time.sleep(6)

    event.set()


if __name__ == '__main__':
    main()
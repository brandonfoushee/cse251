import multiprocessing as mp
import time
#from queue import Queue
from multiprocessing import Queue, Value
#from multiprocessing import Manager.list
import ctypes


def sender(count, q):
    for i in range(count):
        q.value = i
        time.sleep(.1)

def receiver(count, q):
    for i in range(count):
        print(q)
        time.sleep(.1)


def main():
    q1 = mp.Manager().Value(ctypes.c_uint64, 0)
    #q2 = Queue()
    l =[]

    sender_p = mp.Process(target=sender, args=(10, q1))
    receiver_p = mp.Process(target=receiver, args=(10, q1,))

    sender_p.start()
    receiver_p.start()

    sender_p.join()
    receiver_p.join()


if __name__ == "__main__":
    main()

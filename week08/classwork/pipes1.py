import multiprocessing as mp
from multiprocessing.connection import PipeConnection
import time
import queue
import ctypes

def sender(conn, queue_mp: mp.Queue):
    for i in range(5):
        conn.send(i)
       # queue_mp.put(i)
    conn.send(None)
   # queue_mp.put(None)

def receiver(conn, queue_mp: mp.Queue, mp_value, count):
    print(f'{mp.current_process().name}')
    while True:
        item = conn.recv()
       # queue_item = queue_mp.get()
        if item == None:
            return
        print(f'{item=}')
        mp_value.value += 1
        count += 1

def main():
    
    queue1 = mp.Queue()
    queue_non_mp = queue.Queue()
    
    mp_list = mp.Manager().list()
    mp_value = mp.Manager().Value(ctypes.c_int, 0)
    count = 0
    
    pipe1, pipe2 = mp.Pipe(False)
    sender_p = mp.Process(target=sender, args=(pipe2, queue1))
    receiver_p = mp.Process(target=receiver, args=(pipe1, queue1, mp_value, count))
    
    receiver_p.start()
    time.sleep(3)
    sender_p.start()
    
    receiver_p.join()
    sender_p.join()
    
    print(f'{mp_value.value}')
    print(f'count={count}')


if __name__ == "__main__":
    main()
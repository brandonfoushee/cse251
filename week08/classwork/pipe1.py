import multiprocessing as mp
from multiprocessing.connection import PipeConnection
import time
import queue
import string


def sender(conn: PipeConnection, q: queue.Queue):
    letters = string.ascii_lowercase

    for l in letters:
        conn.send(l)
        q.put(l)
    conn.send(None)
    conn.close()

def receiver(conn: PipeConnection):
    
    while True:
        item = conn.recv()
        if item == None:
            conn.close()
            break
        print(f'{item=}')



def main():

    pipe_send, pipe_recv = mp.Pipe()
    
    q = mp.Queue()

    process_sender = mp.Process(target=sender, args=(pipe_send, q))
    process_recv = mp.Process(target=receiver, args=(pipe_recv, ))
    
    process_recv.start()
    process_sender.start()
    
    process_sender.join()
    process_recv.join()


if __name__ == '__main__':
    main()

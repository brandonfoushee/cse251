import multiprocessing as mp
from multiprocessing.connection import PipeConnection
import time

def sender(conn):
    for i in range(5):
        conn.send(i)
    conn.send(None)

def receiver(conn):
    print(f'{mp.current_process().name}')
    while True:
        item = conn.recv()
        if item == None:
            break
        print(f'{item=}')

def main():
    
    queue1 = mp.Queue()
    
    pipe1, pipe2 = mp.Pipe(False)
    sender_p = mp.Process(target=sender, args=(pipe2,))
    receiver_p = mp.Process(target=receiver, args=(pipe1,))
    
    receiver_p.start()
    time.sleep(3)
    sender_p.start()
    
    receiver_p.join()
    sender_p.join()


if __name__ == "__main__":
    main()
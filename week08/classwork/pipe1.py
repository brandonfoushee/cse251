import multiprocessing as mp
from multiprocessing.connection import PipeConnection
import time

def sender(count, conn: PipeConnection):
    o = object()
    conn.send(o)
    with conn as c:
        for i in range(count):
            c.send(i)
        conn.send(None)
        #conn.send(10)
        #conn.close()

def receiver(conn: PipeConnection):
    with conn as c:
        while True:
            item = conn.recv()
            print(item)
            if item == None:
                time.sleep(1)
                break
    #conn.recv()
    #conn.close()

def main():
    p1, p2 = mp.Pipe()
    
    sender_p = mp.Process(target=sender, args=(10, p1))
    receiver_p = mp.Process(target=receiver, args=(p2,))
    
    sender_p.start()
    receiver_p.start()
    
    sender_p.join()
    receiver_p.join()

if __name__ == "__main__":
    main()
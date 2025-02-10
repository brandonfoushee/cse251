import threading
import time
import random

import queue

MAX_Q_SIZE = 10

class NonBlockingQueue():
    def __init__(self) -> None:
        self.items = []
    
    def get(self):
        return self.items.pop(0)
    
    def put(self, item):
        self.items.append(item)
    
    def size(self):
        return len(self.items)

def producer(q: NonBlockingQueue, sem_1: threading.Semaphore, sem_2: threading.Semaphore):
    for i in range(50):
        sem_2.acquire()
        time.sleep(random.uniform(0.001, 0.0001))
        q.put(i)
        sem_1.release()
    q.put("ALL DONE")
    sem_1.release()

def consumer(q: NonBlockingQueue, sem_1: threading.Semaphore, sem_2: threading.Semaphore):
    while True:
        sem_1.acquire()
        print(f'{q.size()}')
        item = q.get()
        #time.sleep(random.uniform(0.001, 0.0001))
        sem_2.release()
        
        # Sentinel 
        if item == "ALL DONE":
            break
            

def main():
    q = NonBlockingQueue()
    lock = threading.Lock()
    sem_1 = threading.Semaphore(0)
    sem_2 = threading.Semaphore(MAX_Q_SIZE)
    
    producer_t =  threading.Thread(target=producer, args=(q, sem_1, sem_2))
    consumer_t =  threading.Thread(target=consumer, args=(q, sem_1, sem_2))
    
    producer_t.start()
    consumer_t.start()
    
    producer_t.join()
    consumer_t.join()
    
    python_queue = queue.Queue()
    python_queue.get()
    
if __name__ == '__main__':
    main()
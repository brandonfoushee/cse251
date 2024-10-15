import threading
import time

MAX_QUEUE_SIZE = 10

class NonBlockingQueue():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

def consumer(q: NonBlockingQueue, sem_empty: threading.Semaphore,
             sem_full: threading.Semaphore):
    while True:
        #print(f'{threading.current_thread().name}: calling acquire on sem_empty')
        sem_empty.acquire()
        #print(f'{threading.current_thread().name}: acquired sem_empty')
        item = q.get()
        sem_full.release()
        if item == None:
            break
        print(f'{item}, size={q.size()}')

def producer(q: NonBlockingQueue, sem_empty: threading.Semaphore,
             sem_full: threading.Semaphore):
    for i in range(20):
        sem_full.acquire()
        q.put(i)
        sem_empty.release()
    q.put(None)
    sem_empty.release()
        
def main():
    
    q = NonBlockingQueue()
    sem_full = threading.Semaphore(MAX_QUEUE_SIZE)
    sem_empty = threading.Semaphore(0)
    
    t1 = threading.Thread(target=consumer, args=(q, sem_empty, sem_full))
    t2 = threading.Thread(target=producer, args=(q, sem_empty, sem_full))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
import queue
import threading

def consumer(q: queue.Queue):
    while True:
        item = q.get()
        if item == None:
            break
        print(f'{item=}')

def producer(q: queue.Queue):
    for i in range(10):
        q.put(i)
    q.put(None)
        
def main():
    
    q = queue.Queue()
    
    t1 = threading.Thread(target=consumer, args=(q,))
    t2 = threading.Thread(target=producer, args=(q,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
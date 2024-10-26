import queue
import threading
import time
import random

def test_with_barrier(q: queue.Queue, b: threading.Barrier):
    time.sleep(random.uniform(0.1, 1.0))
    print(f'{threading.current_thread().name}: AFTER SLEEP time={time.time()}\n', end="")
    
    # Add a barrier
    b.wait()
    q.put(time.time())

if __name__ == "__main__":
    
    NUMBER_OF_THREADS = 4
    
    q = queue.Queue()
    b = threading.Barrier(NUMBER_OF_THREADS)
    l = threading.Lock()
    
    threads = []
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=test_with_barrier, args=(q, b, l))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
        
    print("DONE")
    
    for _ in range(q.qsize()):
        print(f'{q.get()}')
        
import threading
import time
import random

def test_with_barrier(barrier: threading.Barrier):
    time.sleep(random.uniform(1, 6))    
    print(f'{threading.current_thread().name}: done sleeping - {time.time()}\n', end="")
    barrier.wait()
    print(f'{threading.current_thread().name}: after barrier - {time.time()}\n', end="")

NUMBER_OF_THREADS = 4
barrier = threading.Barrier(NUMBER_OF_THREADS)

threads = []
for _ in range(NUMBER_OF_THREADS):
    t = threading.Thread(target=test_with_barrier, args=(barrier,))
    t.start()
    
for t in threads:
    t.join()
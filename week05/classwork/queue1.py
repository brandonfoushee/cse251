import queue
import threading
import time

MAX_QUEUE_SIZE = 1


class NonBlockingQueue():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        self.items.append(item)

    def get(self):
        # if(len(self.items) == 0):
        #     raise Exception("You are trying to pop an item from your queue, but your queue is empty!\nYou must use a semaphore.acquire to block to prevent this from happening. Call semaphore.release after you put a spaceship on the queue, this will unblock the semaphore.acquire.")
        return self.items.pop(0)


def read(q: NonBlockingQueue, sem_empty: threading.Semaphore, sem_full: threading.Semaphore):
    while True:
        print(f'{threading.current_thread().name}\n', end="")
        sem_empty.acquire()
        print(f'{threading.current_thread().name}\n', end="")
        print('Reading item from queue\n', end="")
        item = q.get()
        print(f'{item=}\n', end="")
        if item == None:
            break
        sem_full.release()


def write(q: NonBlockingQueue, sem_empty: threading.Semaphore, sem_full: threading.Semaphore):
    for i in range(10):
        print(f'{threading.current_thread().name}: calling acquire\n', end="")
        sem_full.acquire()
        print(f'{threading.current_thread().name}: called acquire\n', end="")
        print(f'Putting {i} to queue\n', end="")
        q.put(i)
        sem_empty.release()

    # send the Sentinel
    q.put(None)
    sem_empty.release()


def main():
    q = NonBlockingQueue()

    # protect from reading queue when empty
    sem_empty = threading.Semaphore(0)

    # protect from writing to queue when full
    sem_full = threading.Semaphore(MAX_QUEUE_SIZE)

    t1 = threading.Thread(target=read, args=(q, sem_empty, sem_full))
    t2 = threading.Thread(target=write, args=(q, sem_empty, sem_full))
    t2.start()
    t1.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

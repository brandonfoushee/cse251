import threading
import time
import random
from threading import Lock

VALUE = 10


def adder(amount: int, repeat_amount: int, lock: Lock):
    global VALUE
    for _ in range(repeat_amount):
        with lock:
            tmp = VALUE
            tmp += amount
            time.sleep(random.uniform(0.0001, 0.001))
            VALUE = tmp


def subtractor(amount: int, repeat_amount: int, lock: Lock):
    global VALUE
    for _ in range(repeat_amount):
        with lock:
            tmp = VALUE
            tmp -= amount
            time.sleep(random.uniform(0.0001, 0.001))
            VALUE = tmp


def main():
    lock = threading.Lock()

    t_adder = threading.Thread(target=adder, args=(1, 1000, lock))
    t_subtr = threading.Thread(target=subtractor, args=(1, 1000, lock))

    t_adder.start()
    t_subtr.start()
    t_adder.join()
    t_subtr.join()

    print(f'\n{VALUE=}')


if __name__ == '__main__':
    main()

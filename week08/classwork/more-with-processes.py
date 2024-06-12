'''
Requirements
1. Write a multithreaded/multiprocessing program that counts the number of prime numbers 
   contained within a data file.
2. Create one thread to read each number from the data file and put the number on the queue.
3. Create n number of processes, where n is equal to the number of cpu/cores on your computer.
4. The processes will pop each number off of the queue and check if it is prime. If it is
   prime increment a "counter" (use an appropriate multiprocessing data structure).
5. Assert that the number of prime numbers found is correct.

Questions:
1. Does increasing the number of processes beyond your cpu count decrease the time it takes
   to find the prime numbers? Why or why not?
2. What are some of the advantages and disadvantages of using processes over threads?
'''

import multiprocessing as mp
import threading
import time


def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def read_thread(q: mp.Queue, filename):
    with open(filename) as f:
        for line in f:
            q.put(int(line.strip()))
    q.put(None)

def prime_process(q: mp.Queue, primes):
    while True:
        num = q.get()
        
        if num == None:
            q.put(None)
            break
        if is_prime(num):
            primes.append(num)
            #print(f'{num=}')
        


def main():
    """ Main function """

    filename = 'data.txt'

    # Start a timer
    begin_time = time.perf_counter()

    # Get number of processes to create based on cpu count
    cpu_count = mp.cpu_count() * 2

    # Create shared data structures
    q = mp.Manager().Queue()
    primes = mp.Manager().list()

    # create reading thread
    reader_t = threading.Thread(target=read_thread, args=(q, filename))
    reader_t.start()

    # create prime processes
    processes = []
    for _ in range(cpu_count):
        p = mp.Process(target=prime_process, args=(q, primes))
        p.start()
        processes.append(p)

    # wait for them to complete
    reader_t.join()
    for p in processes:
        p.join()

    total_time = "{:.2f}".format(time.perf_counter() - begin_time)
    print(f'Total time = {total_time} sec')

    # Assert the correct amount of primes were found.
    assert len(primes) == 321, "You should find exactly 321 prime numbers"


if __name__ == '__main__':
    main()

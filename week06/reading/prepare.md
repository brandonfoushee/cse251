![](../../banner.png)

# 06 Prepare: Thread Synchronization: Barriers

**Things you should know or know how to do that you learned from last week**
(if not, then please ask---see [Matthew 7:7-8](https://www.churchofjesuschrist.org/study/scriptures/nt/matt/7?lang=eng))
1. Explain what a queue is and how to use it.
2. Explain what a sentinel is and now to use it.
3. Explain what a semaphore is and how to use it.

<ins>Key Concepts in this week's reading:</ins>
1. What thread synchronization is.
2. What a barrier is.
3. When to use a barrier.

## Overview

This week's lesson is on Python processes and Introduction to Analyzing programs for parallelism.

## Synchronization

One of the advantages for using threads is to improve the time it takes to complete tasks. We can divide up the tasks and assign them to multiple threads. However, if the order of one or more tasks matters, then we need a way to synchronize (or order) these tasks (see [Thread synchronization](https://en.wikipedia.org/wiki/Synchronization_(computer_science)#Thread_or_process_synchronization)). We have used locks and semaphores to provide a way to protect critical sections of code from executing when we don't want. Another consideration is that we may want to not execute a section of code until all threads have completed certain tasks. 

## Barrier

We introduce a new thread and process synchronization control called a **barrier**.  Here is the [documentation](https://docs.python.org/3/library/threading.html#barrier-objects) on barriers.


> Barrier objects in python are used to wait for a fixed number of thread to complete execution before any particular thread can proceed forward with the execution of the program. Each thread calls wait() function upon reaching the barrier. The barrier is responsible for keeping track of the number of wait() calls. If this number goes beyond the number of threads for which the barrier was initialized with, then the barrier gives a way to the waiting threads to proceed on with the execution. All the threads at this point of execution, are simultaneously released.

> Barriers can even be used to synchronize access between threads. However, generally a barrier is used to combine the output of threads. A barrier object can be reused multiple times for the exact same number of threads that it was initially initialized for.

[Above quoted from geeksforgeeks.org](https://www.geeksforgeeks.org/barrier-objects-python/)

### Example 1
In this example, we will have three threads working on finding primes in a range of values.  Each thread will take a different amount of time to complete.  A barrier can be used to force all of the threads to wait until all of them are finished before moving on.

```python
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


def thread_function(thread_id, barrier, start_value, end_value):
    start_time = time.perf_counter()
    primes = []
    for i in range(start_value, end_value + 1):
        print(f'Thread {thread_id} checking number {i}\n', end="")
        if is_prime(i):
            primes.append(i)
    total_time = time.perf_counter() - start_time

    print(f'Thread {thread_id} calling wait on barrier\n', end="")
    barrier.wait()  # Wait for all threads to complete the task before printing
    print(
        f'Thread {thread_id}: time = {total_time:.5f}: primes found = {len(primes)}\n', end="")


def main():

    # 4 is the number of threads to wait for
    barrier = threading.Barrier(4)

    # Create 4 threads, pass a "thread_id" and a barrier to each thread
    threads = []
    threads.append(threading.Thread(target=thread_function,
                                    args=(1, barrier, 1, 1000)))
    threads.append(threading.Thread(target=thread_function,
                                    args=(2, barrier, 1000, 2000)))
    threads.append(threading.Thread(target=thread_function,
                                    args=(3, barrier, 2000, 3000)))
    threads.append(threading.Thread(target=thread_function,
                                    args=(4, barrier, 3000, 4000)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
```

Here is the output of the program.  Notice that without the barrier, each thread would have displayed its results too early. 

```
<long list of numbers>
Thread 3: time = 1.01124: primes found = 127
Thread 1: time = 0.99509: primes found = 120
Thread 2: time = 1.00182: primes found = 168
Thread 4: time = 1.00864: primes found = 135
```

### Example 2
When using a queue to synchronize data between 2 or more threads, a barrier can be used to ensure that a thread that ends does not prematurely put a sentinel on the queue while other threads are still adding items to the queue:

```python
import threading
import queue

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

def thread_function(thread_id, q: queue.Queue, barrier: threading.Barrier, start_value, end_value):
    for i in range(start_value, end_value):
        if is_prime(i):
            q.put(i)

    barrier.wait()  # Wait for all threads to complete the task before printing
    q.put(None) # signal to print function to end

def print_function(q: queue.Queue):
    count = 0
    while True:
        number = q.get()
        if number == None:
            break
        print(f'{number} is prime')
        count += 1
    print(
        f'Total primes found = {count}\n', end="")

def main():

    # 4 is the number of threads to wait
    barrier = threading.Barrier(4)

    q = queue.Queue()

    # Create 4 threads, pass a "thread_id" and a barrier to each thread
    threads = []
    threads.append(threading.Thread(target=thread_function,
                                    args=(1, q, barrier, 1, 3)))
    threads.append(threading.Thread(target=thread_function,
                                    args=(2, q, barrier, 3, 5)))
    threads.append(threading.Thread(target=thread_function,
                                    args=(3, q, barrier, 5, 7)))
    threads.append(threading.Thread(target=thread_function,
                                    args=(4, q, barrier, 7, 9)))
    threads.append(threading.Thread(target=print_function, args=(q,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
```

Output:
```
2 is prime
3 is prime
5 is prime
7 is prime
Total primes found = 4
```

Without the barrier, the following would be the output:
```
2 is prime
Total primes found = 1
```

The print thread would have ended too early.
![](../../banner.png)


# 08 Prepare: Process Communication and Barriers

**Things you should know or know how to do that you learned from last week**
(if not, then please ask---see [Matthew 7:7-8](https://www.churchofjesuschrist.org/study/scriptures/nt/matt/7?lang=eng))
1. Explain the difference between a process and a thread.
2. Explain the relationship between a GIL and a process (in Python). 
3. Know when to use a thread versus a process.
4. Know how to create a new process using the multiprocessing module.
5. Know how to create a pool of processes.
6. Understand what the map function is.

<ins>Key Concepts in this week's reading:</ins>
1. Why data cannot be easily shared between processes.
2. How use a multiprocessing queue to share data between processes.
3. How use a multiprocessing pipe to share data between processes.

## Overview

When sharing information between processes in Python, there are limits on what we can do.  We will cover those issues here as well as understanding barriers.

## Preparation Material

Please read the following information found in the links below.

### Links to Articles

- [Python Documentation](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues)
- [StackOverFlow: Pipe vs Queue](https://stackoverflow.com/questions/8463008/multiprocessing-pipe-vs-queue)
- [Python Shared Memory Between Processes](https://www.geeksforgeeks.org/multiprocessing-python-set-2/)
- [Pool, Process, Queue, and Pipe code examples](http://www.kasimte.com/multiprocessing-in-python-pool-process-queue-and-pipe)

## Issues with sharing data between processes

It was easy to create shared data structures that work between threads.  This is because there is only one GIL running and all threads can share the program's memory.

Processes in Python are different since when you create a process, you create a new GIL.  Each process/GIL has its own memory, stack, and registers.  The `multiprocessing` module supplies us with a few options for sharing data between processes.

First, lets review the problem in a few examples. In the following example from last lesson, we have three threads all sharing the same list.  This list contains three values `[0, 0, 0]` before the threads are started and it is passed to each thread.

```python
import threading

def thread_function(thread_id, lock, data):
    # Only change the value in the list based on thread_id
    for i in range(10):
        data[thread_id] += 1
    print(f'Process {thread_id}: {data}')

def main():    
    lock = threading.Lock()

    # Create a value with each thread
    data = [0] * 3

    # Create 3 threads, pass a "thread_id" for each thread
    threads = [threading.Thread(target=thread_function, args=(i, lock, data)) for i in range(3)]

    for i in range(3):
        threads[i].start()

    for i in range(3):
        threads[i].join()

    print(f'All work completed: {sum(data)}')

if __name__ == '__main__':
    main()
```
The program generates the following output.  The thread order might be different if you run this program on your computer, but the results are the same.  Each thread only changes the value in the list based on thread_id.

```
Process 0: [10, 0, 0]
Process 1: [10, 10, 0]
Process 2: [10, 10, 10]
All work completed: 30
```

Here is the same program using processes from the `multiprocessing` module.

```python
import multiprocessing as mp 

def process_function(process_id, data):
    # only change the value based on process_id
    for i in range(10):
        data[process_id] += 1
    print(f'Process {process_id}: {data}')

def main():    
    # Create a value with each thread
    data = [0] * 3

    # Create 3 processes, pass a "process_id" for each thread
    processes = [mp.Process(target=process_function, args=(i, data)) for i in range(3)]

    for i in range(3):
        processes[i].start()

    for i in range(3):
        processes[i].join()

    print(f'All work completed: {sum(data)}')

if __name__ == '__main__':
    main()
```
The results of this program are very different from the thread version.  When each process was created, a new GIL was created for each.  In this case, each process has their own version of the list `data`.  After each process changes their version of the data list, the main code calls `join()` to wait until they are finished.  Then, main's version of the list `data` is used in the finial print() statement.  It's empty, because the processes changed a different `data` list.

In should be clear that global variables would be handled in the same method using processes, where each process has a copy of the global variables.

```
Process 0: [10, 0, 0]
Process 1: [0, 10, 0]
Process 2: [0, 0, 10]
All work completed: 0
```

### Solution to the processes sharing

The `multiprocessing` module provides a few mechanisms to help with sharing data between processes.

**mp.Queue**

A Queue from the `multiprocessing` module allows you to share a queue between processes.  Here is the code example from last lesson using processes and `mp.Queue`

```python
import multiprocessing as mp 

MAX_COUNT = 10

def read_thread(shared_q):
    for i in range(MAX_COUNT):
        # read from queue
        print(shared_q.get())

def write_thread(shared_q):
    for i in range(MAX_COUNT):
        # place value onto queue
        shared_q.put(i)

def main():
    """ Main function """

    # This queue will be shared between the processes
    shared_q = mp.Queue()

    write = mp.Process(target=write_thread, args=(shared_q,))
    read = mp.Process(target=read_thread, args=(shared_q,))

    read.start()        # doesn't matter which starts first
    write.start()

    write.join()
    read.join()

if __name__ == '__main__':
    main()
```

**mp.Pipe**

Pipes are used to send messages (ie., data) between processes.  The following is from the Python documentation on pipes.  Note, that a pipe removes the need for a lock.  The more locks in a program, the potential of it slowing down.

> When using multiple processes, one generally uses message passing for communication between processes and avoids having to use any synchronization primitives like locks.

### Creating a pipe

When you create a pipe from the multiprocessing module, you receive both ends of the pipe.  They are called the parent and child connections in most programming languages.  (ie., the parent will send information using their connection and the child will receive information using their connection).  You can send information in both directions.  Just be careful that you don't have both processes waiting for information at the same time (ie., deadlock)

```python
import multiprocessing 

parent_connection, child_connection = multiprocessing.Pipe()
```

Here is an example of creating a pipe and passing the parent connection to the `sender` process and the child connection to the `receiver` process.  Note that if a process tries to read from a pipe using `recv()` and there is nothing to read, then the process will wait.  If nothing ever is send on that pipe, you have a deadlock situation.

```python
import multiprocessing 

def sender(conn): 
    """ function to send messages to other end of pipe """
    conn.send('Hello')
    conn.send('World')
    conn.close() 			# Close this connection when done

def receiver(conn): 
    """ function to print the messages received from other end of pipe  """
    print(f'Received: {conn.recv()}')
    print(f'Received: {conn.recv()}')

if __name__ == "__main__": 

    # creating a pipe 
    parent_conn, child_conn = multiprocessing.Pipe() 

    # creating new processes 
    p1 = multiprocessing.Process(target=sender, args=(parent_conn,)) 
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,)) 

    # running processes 
    p1.start() 
    p2.start() 

    # wait until processes finish 
    p1.join() 
    p2.join() 

```

Output:

```
Received: Hello
Received: World
```


**mp.Value and mp.Array**

Normally variables can't be shared between processes because each process has a complete copy of the program.  However, there is a method for sharing data. We will need to use the `multiprocessing` module for this.

Here is an example from [the Python documentation website](https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes)

[Data types for Value() function](https://docs.python.org/3/library/array.html#module-array)

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

Output:

```
3.1415927
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

Break down of the above example:

We need to import **Value** and/or **Array**. (There are other methods of sharing data, but will wait later in the course to talk about them.)

```python
from multiprocessing import Process, Value, Array
```

Next, we can use **Value** and/or **Array** to create the shared variables that will be used between processes.

For both Value and Array, they take two arguments. 

- The first one is the data type. `d` indicates a double precision float and `i` indicates a signed integer.

- The second is the initial value for Value() and for Array, it is the list of values.


```python
num = Value('d', 0.0)
arr = Array('i', range(10))
```

For other examples:

```python
count = Value('i', 0)   			   # create a shared integer count
counts = Array('i', [0, 0, 0, 0, 0])   # Create shared array of 5 values
```


Here we just pass them to the process using the `args` argument.

```python
p = Process(target=f, args=(num, arr))
```

Using these shared variables is a little different.  For shared Value() variables, you need to use `.value` to use them.  For the shared Array() variable, you use them normally using `[]`.

```python
def f(n, a):
	n.value = 3.1415927
	for i in range(len(a)):
	    a[i] = -a[i]
```

When using shared variables, remember that if there are processes writing and reading them, when you need to stop a race condition by using a shared lock.

## Managers

We have `Queue` and `Pipe` for sharing data between processes.  For all other data the `multiprocessing` module has a managers.  Managers are used for sharing between processes.  Lets go back to the process example with the shared list that didn't work.  Here is a version that does. `data = mp.Manager().list([0] * 3)` solves the data sharing issue.

```python
import multiprocessing as mp 

def process_function(process_id, data):
    for i in range(10):
        data[process_id] += 1
    print(f'Process {process_id}: {data}')

def main():    
    # Create a value with each thread
    data = mp.Manager().list([0] * 3)

    # Create 3 processes, pass a "process_id" for each thread
    processes = [mp.Process(target=process_function, args=(i, data)) for i in range(3)]

    for i in range(3):
        processes[i].start()

    for i in range(3):
        processes[i].join()

    print(f'All work completed: {sum(data)}')

if __name__ == '__main__':
    main()
```

Output from the above program.  Why was the results of the list after process 0 was finished `[10, 9, 0]` and not `[10, 10, 0]`?

```
Process 0: [10, 9, 0]
Process 1: [10, 10, 0]
Process 2: [10, 10, 10]
All work completed: 30
```

More document on managers can be [found here](https://docs.python.org/3/library/multiprocessing.html#managers).
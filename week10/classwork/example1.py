import multiprocessing as mp
import threading
import time

SUMS = []

def sum_all_values(x):
    sum = 0
    for i in range(x):
        sum += i
    time.sleep(0.25)
    return sum

def sum_all_values_cb(result):
    global SUMS
    SUMS.append(result)
def prime_number_cb(result):
    global PRIMES
    PRIMES.append(result)

def main():
    pool = mp.Pool(mp.cpu_count())
    
    for x in range(1, 100):
        pool.apply_async(sum_all_values, args=(x,), callback=sum_all_values_cb)
    
    # I want to do something
    print('this will run and not wait for the previous line')
    
    #output = [p.get() for p in results]
    pool.close()
    pool.join()
    print(f'{SUMS=}')
    
if __name__ == "__main__":
    main()
import multiprocessing as mp
import time

RESULTS_1 = []
RESULTS_2 = []
RESULTS_3 = []

def sum_all_values(n: int):
    s = 0
    for i in range(n):
        s += i
        print(f'{i=}, {s=}')
        time.sleep(0.1)
    return s

def cb_1(result):
    RESULTS_1.append(result)

def cb_2(result):
    RESULTS_2.append(result)

def cb_3(result):
    RESULTS_3.append(result)

def main():

    pool_1 = mp.Pool(2)
    pool_2 = mp.Pool(2)
    pool_3 = mp.Pool(2)
    
    pool_1.apply_async(func=sum_all_values, args=(5, ), callback=cb_1)
    pool_2.apply_async(func=sum_all_values, args=(6, ), callback=cb_2)
    pool_3.apply_async(func=sum_all_values, args=(7, ), callback=cb_3)

    #print(result.get())
    
    pool_1.close()
    pool_1.join()
    pool_2.close()
    pool_2.join()
    pool_3.close()
    pool_3.join()
    
    print(f'{RESULTS_1=}')
    print(f'{RESULTS_2=}')
    print(f'{RESULTS_3=}')
    print("DONE")


if __name__ == '__main__':
    main()

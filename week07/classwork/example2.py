import multiprocessing
import time

def square(n: int):
    n **= 2
    print(f'{multiprocessing.current_process().name}: {n=}')
    time.sleep(0.1)
    #results.append(n)
    return n
    
def main():
    
    inputs = list(range(1, 101))
    results = []
    
    # processes = []
    # for i in inputs:
    #     p = multiprocessing.Process(target=square, args=(i, results))
    #     p.start()
    #     processes.append(p)
        
    # for p in processes:
    #     p.join()
    
    # print(f'{results=}')
    
    cores = multiprocessing.cpu_count()
    print(f'{cores=}')
    
    pool = multiprocessing.Pool(cores)
    result = pool.map(func=square, iterable=inputs)
    
    print(f'{result=}\n', end="")


if __name__ == '__main__':
    main()
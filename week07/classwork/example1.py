import multiprocessing

SUM = 0

def count(loopCount):
    sum = 0
    for i in range(loopCount):
        sum += i
        
    global SUM
    SUM = sum
    print(f'\n{multiprocessing.current_process().name}: memory address={id(SUM)}, {SUM=}')

def main():
    
    p1 = multiprocessing.Process(target=count, args=(10,))
    p1.start()
    p1.join()
    
    print(f'{multiprocessing.current_process().name}: memory address={id(SUM)}, {SUM=}')

print(f'\n{__name__=}')

if __name__ == '__main__':
    main()
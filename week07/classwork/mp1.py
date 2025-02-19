import multiprocessing as mp
import time

MY_SUM = 0


def sum(x: int):
    #global MY_SUM
    #MY_SUM = x + x
    #print(f'inside of sum, MY_SUM={MY_SUM}')
    return x + x 

class MyProcess(mp.Process):
    def __init__(self, x: int):
        mp.Process.__init__(self)
        self.x = x
        
    def run(self):
        print(f'{self.x + self.x}')

def square(n :int):
    n **= 2
    #print(f'{mp.current_process().name}: {n=}')
    #time.sleep(1)
    return n

def main():
    # p1 = mp.Process(target=sum, args=(10, ))
    # p1.start()
    # p1.join()
    
    s = square(10)
    #print(f'{s=}')
    
    #p2 = MyProcess(3)
    #p2.start()
    #p2.join()
    
    inputs = list(range(100))
    outputs = []
    
    # with mp.Pool(mp.cpu_count()) as p:
    #     outputs = p.map(square, inputs)
    p = mp.Pool(4)
    
    #outputs = p.map(square, inputs)
    #print(f'1: {outputs=}')
    
    outputs = p.map_async(sum, inputs)
    print(f'{outputs.get()}')
    p.close()
    p.join()

    #print(f'{outputs=}')
    #print(f'in main, MY_SUM={MY_SUM}')
    print("Done")


#print("__name__=", __name__)
if __name__ == '__main__':
    main()

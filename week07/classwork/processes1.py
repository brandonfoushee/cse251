import multiprocessing as mp
import time
import asyncio

VALUE = 10
SUM = 0


def square(n: int):
    n **= 2
    time.sleep(0.1)
    global VALUE
    VALUE = n
    print(f'{id(VALUE)=}')
    print(f'{mp.current_process().name}: {n}')
    return n


class MyProcess(mp.Process):
    def __init__(self, loopCount):
        mp.Process.__init__(self)
        self.loopCount = loopCount

    def run(self):
        sum = 0
        for i in range(self.loopCount):
            sum += i
        print(f'{sum=}')
        global SUM
        SUM = sum


def main():
    # p = mp.Process(target=square, args=(6,))
    # p.start()
    # p.join()
    # square(3)
    # print(f'{VALUE=}')

    # p1 = MyProcess(9)
    # p2 = MyProcess(10)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    inputs = list(range(101))
    outputs = []

    with mp.Pool(mp.cpu_count()) as p:
        outputs = p.map(square, inputs)
        
    print(f'{outputs=}')


if __name__ == '__main__':
    main()

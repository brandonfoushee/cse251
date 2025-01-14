import threading
import time
import random

SUM = 0


def add_two_numbers(n1, n2, results: list):
    #global SUM
    sum = n1 + n2
    #print(f'{sum=}\n', end="")
    #time.sleep(3)
    #print('all done\n', end="")
    #SUM = sum
    time.sleep(random.uniform(0.1, 0.2))
    results.append(sum)


class Sum_Thread(threading.Thread):
    def __init__(self, n1: int, n2: int):
        threading.Thread.__init__(self)
        self.n1 = n1
        self.n2 = n2
        self.sum = 0

    def run(self):
        time.sleep(3)
        self.sum = self.n1 + self.n2


# t1 = threading.Thread(target=add_two_numbers, args=(1, 2))
# t1.start()
# print(f'I have started my thread')
# print(f'{SUM=}')

# t1.join()
# print(f'{SUM=}')

# t2 = Sum_Thread(5, 6)
# t2.start()
# print(f'{t2.sum=}')
# t2.join()
# print(f'{t2.sum=}')

#results = [0] * 100
results = []

threads = []
# for i in range(100):
#     t = threading.Thread(target=add_two_numbers, args=(i, i + 1, i, results))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print(f'{results=}')

threads = []
for i in range(100):
    t = threading.Thread(target=add_two_numbers, args=(i, i + 1, results))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f'{results=}')
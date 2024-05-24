'''
Requirements
1. Using two threads, put space ships onto a shared queue, with one thread consuming
   the items from the queue and the other producing the items.
2. The size of queue should never exceed 10.
3. Do not call queue size to determine if maximum size has been reached. This means
   that you should not do something like this: 
        if q.size() < 10:
   Use the blocking semaphore function 'acquire'.
4. Produce a Plot of count vs queue size (okay to use q.size since this is not a
   condition statement).
5. COMMENT every line that you write yourself.
   
Questions:
1. Do you need to use locks around accessing the queue object when using multiple threads? 
   Why or why not?
   >
   >
2. How would you define a semaphore in your own words?
   >
   >
3. Read https://stackoverflow.com/questions/2407589/what-does-the-term-blocking-mean-in-programming.
   What does it mean that the "join" function is a blocking function? Why do we want to block?
   >
   >
   >
'''

from datetime import datetime
import time
import threading
import random
import string
# DO NOT import queue

from plots import Plots
from cse251functions import *

# Global Constants
MAX_QUEUE_SIZE = 10
SLEEP_REDUCE_FACTOR = 50

#########################
# NO GLOBAL VARIABLES!
#########################


class SpaceShip():
    """ This is the SpaceShips class that will be created by the starports """

    # Class Variables
    spaceship_makes = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune',
                 'Pluto')

    spaceship_models = [f'{random.choice(string.ascii_uppercase)}{n}' for n in range(20)]

    spaceship_years = [i for i in range(2100, 2150)]

    def __init__(self):
        # Make a random spaceship
        self.model = random.choice(SpaceShip.spaceship_makes)
        self.make = random.choice(SpaceShip.spaceship_models)
        self.year = random.choice(SpaceShip.spaceship_years)

        # Sleep a little
        time.sleep(random.random() / (SLEEP_REDUCE_FACTOR))

        # Display the spaceship that has just be created in the terminal
        self.display()

    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class NonBlockingQueue():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        self.items.append(item)
        if(len(self.items) > MAX_QUEUE_SIZE):
            raise Exception("You have exceeded the size of your space queue!!!\nYou have broken the law and the Solar System Space Force are coming for you...!!!\nYou need to use semaphore.acquire to block when the queue is full, and call semaphore.release after removing a spaceship from the queue.")

    """Will throw an error if called when there are no items (list is empty)"""
    def get(self):
        if(len(self.items) == 0):
            raise Exception("You are trying to pop an item from your queue, but your queue is empty!\nYou must use a semaphore.acquire to block to prevent this from happening. Call semaphore.release after you put a spaceship on the queue, this will unblock the semaphore.acquire.")
        return self.items.pop(0)


class SpaceShipFactory(threading.Thread):
    """ This is a factory.  It will create spaceships and place them on the queue """

    def __init__(self):
        # TODO - add attributes to self based on the parameters you pass in when instantiating
        #        your thread object (like count, semaphore, queue, etc)
        # Note: don't forget to call the super class's constructor
        pass  # delete this and the comment above!!!

    def run(self):
        for i in range(self.count):
            # TODO Add your code here (delete this line)
            pass # delete this line
        # signal the buyer that there there are no more spaceships coming


class SpaceShipBuyer(threading.Thread):
    """ This is a buyer that receives spaceships from the queue """

    def __init__(self):
        # TODO - add attributes to self based on the parameters you pass in when instantiating
        #        your thread object (semaphore, queue, etc)
        # Note: don't forget to call the super class's constructor
        pass  # remove this and the comment above!!

    def run(self):
        while True:
            # TODO Add your code here (delete this)

            # Sleep a random amount after selling a space ship
            time.sleep(random.random() / (SLEEP_REDUCE_FACTOR))


def main():
    # Start a timer
    begin_time = time.perf_counter()

    # Number of spaceships the factory will send to the buyer
    spaceships_to_produce = 500

    # TODO Create semaphores
    # TODO Create queue (ONLY use class NonBlockingQueue)
    # TODO Create lock

    # This tracks the size of the queue at the time a spaceship
    # is removed from the queue by the buyer (do it after calling get()).
    # queue_stats[queue.size()] += 1
    buyer_stats = [0] * MAX_QUEUE_SIZE

    # TODO create your one spaceship factory

    # TODO create your one spaceship buyer

    # TODO Start factory and buyer

    # TODO Wait for factory and buyer to complete

    total_time = "{:.2f}".format(time.perf_counter() - begin_time)
    print(f'Total time = {total_time} sec')
    
    # The number of spaceships that the factory sends 
    # to the buyer should be exactly the same
    assert(sum(buyer_stats) == spaceships_to_produce)

    # Plot space ship count vs queue size
    xaxis = [i for i in range(1, MAX_QUEUE_SIZE + 1)]
    plot = Plots()
    plot.bar(xaxis, buyer_stats,
             title=f'{sum(buyer_stats)} Spaceships Produced by {STUDENT_NAME}: Count VS Queue Size', x_label='Queue Size', y_label='Count')


if __name__ == '__main__':
    main()
    create_signature_file()

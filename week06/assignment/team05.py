"""
Course: CSE 251
Lesson Week: 05
File: team05.py
Author: Brother Comeau (modified by Brother Foushee)

Purpose: Team Activity

Instructions:

- See in Canvas

"""

import threading
import queue
import time
import requests
import json

RETRIEVE_THREADS = 4        # Number of retrieve_threads
NO_MORE_VALUES = 'No more'  # Special value to indicate no more items in the queue


def retrieve_thread(q: queue.Queue, idx: int):  # TODO add arguments
    """ Process values from the data_queue """
    while True:
        
        url = q.get()
        
        if url == NO_MORE_VALUES:
            print("ALL DONE\n", end="")
            q.put(NO_MORE_VALUES)
            break

        http_response = requests.get(url)
        response = http_response.json()
        print(f'{response["name"]}\n', end="")


def file_reader(q: queue.Queue):  # TODO add arguments
    """ This thread reads the data file and places the values in the data_queue """
    
    with open("urls.txt") as f:
        for line in f:
            #print(f'{line=}')
            q.put(line.strip())
            
    #for _ in range(RETRIEVE_THREADS):
    q.put(NO_MORE_VALUES)

def main():
    """ Main function """

    # Start a timer
    begin_time = time.perf_counter()

    q = queue.Queue()

    threads = []

    # Pass any arguments to these thread needed to do their jobs
    filereader_t = threading.Thread(target=file_reader, args=(q,))
    filereader_t.start()
    threads.append(filereader_t)

    for i in range(RETRIEVE_THREADS):
        t = threading.Thread(target=retrieve_thread, args=(q, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    total_time = "{:.2f}".format(time.perf_counter() - begin_time)
    print(f'Total time to process all URLS = {total_time} sec')


if __name__ == '__main__':
    main()

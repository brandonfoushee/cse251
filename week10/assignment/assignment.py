'''
Requirements
1. Create a multiprocessing program that reads in files with defined tasks to perform.
2. The program should use a process pool per task type and use apply_async calls with callback functions.
3. The callback functions will store the results in global lists based on the task to perform.
4. Once all 4034 tasks are done, the code should print out each list and a breakdown of 
   the number of each task performed.
5. COMMENT every line that you write yourself.
   
Questions:
1. How many processes did you specify for each pool:
   >Finding primes:
   >Finding words in a file:
   >Changing text to uppercase:
   >Finding the sum of numbers:
   >Web request to get names of Star Wars people:
   
   >How do you determine these numbers:
   
2. Specify whether each of the tasks is IO Bound or CPU Bound?
   >Finding primes:
   >Finding words in a file:
   >Changing text to uppercase:
   >Finding the sum of numbers:
   >Web request to get names of Star Wars people:
   
3. What was your overall time, with:
   >one process in each of your five pools:  ___ seconds
   >with the number of processes you show in question one:  ___ seconds
'''

import glob
import json
import math
import multiprocessing as mp
import os
import time
from datetime import datetime, timedelta
from cse251functions import *

import numpy as np
import requests

TYPE_PRIME = 'prime'
TYPE_WORD = 'word'
TYPE_UPPER = 'upper'
TYPE_SUM = 'sum'
TYPE_NAME = 'name'

# Global lists to collect the task results
result_primes = []
result_words = []
result_upper = []
result_sums = []
result_names = []


def is_prime(n: int):
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def task_prime(value):
    """
    Use the is_prime() above
    Add the following to the global list:
        {value} is prime
            - or -
        {value} is not prime
    """
    pass


def task_word(word):
    """
    search in file 'words.txt'
    Add the following to the global list:
        {word} Found
            - or -
        {word} not found *****
    """
    pass


def task_upper(text):
    """
    Add the following to the global list:
        {text} ==>  uppercase version of {text}
    """
    pass


def task_sum(start_value, end_value):
    """
    Add the following to the global list:
        sum of {start_value:,} to {end_value:,} = {total:,}
    """
    pass


def task_name(url):
    """
    use requests module
    Add the following to the global list:
        {url} has name <name>
            - or -
        {url} had an error receiving the information
    """
    pass


def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename) as json_file:
            data = json.load(json_file)
        return data
    else:
        return {}


def main():
    begin_time = time.time()
    count = 0
    
    # TODO Create process pools

    # The below code is example code to show you the logic of what you are supposed to do.
    # Remove it and replace with using process pools with apply_async calls.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # task_files = glob.glob("tasks/*.task")
    # for filename in task_files:
    #     # print()
    #     # print(filename)
    #     task = load_json_file(filename)
    #     print(task)
    #     count += 1
    #     task_type = task['task']
    #     if task_type == TYPE_PRIME:
    #         task_prime(task['value'])
    #     elif task_type == TYPE_WORD:
    #         task_word(task['word'])
    #     elif task_type == TYPE_UPPER:
    #         task_upper(task['text'])
    #     elif task_type == TYPE_SUM:
    #         task_sum(task['start'], task['end'])
    #     elif task_type == TYPE_NAME:
    #         task_name(task['url'])
    #     else:
    #         print(f'Error: unknown task type {task_type}')
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # TODO start pools and block until they are done before trying to print

    def print_list(lst):
        for item in lst:
            print(item)
        print(' ')

    print('-' * 80)
    print(f'Primes: {len(result_primes)}')
    print_list(result_primes)

    print('-' * 80)
    print(f'Words: {len(result_words)}')
    print_list(result_words)

    print('-' * 80)
    print(f'Uppercase: {len(result_upper)}')
    print_list(result_upper)

    print('-' * 80)
    print(f'Sums: {len(result_sums)}')
    print_list(result_sums)

    print('-' * 80)
    print(f'Names: {len(result_names)}')
    print_list(result_names)

    print(f'Number of Primes tasks: {len(result_primes)}')
    print(f'Number of Words tasks: {len(result_words)}')
    print(f'Number of Uppercase tasks: {len(result_upper)}')
    print(f'Number of Sums tasks: {len(result_sums)}')
    print(f'Number of Names tasks: {len(result_names)}')
    print(f'Finished processes {count} tasks = {time.time() - begin_time}')


if __name__ == '__main__':
    main()
    create_signature_file()

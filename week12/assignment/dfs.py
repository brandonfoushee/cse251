"""
Course: CSE 251
Lesson Week: 12
File: assignment.py
Author: <your name>
Purpose: Assignment 12 - Family Search
"""
import json
import threading
import time

import requests
from virusApi import *
from cse251functions import *

TOP_API_URL = 'http://127.0.0.1:8129'
NUMBER_GENERATIONS = 2  # set this to 2 as you are testing your code
NUMBER_THREADS = 0  # TODO use this to keep track of the number of threads you create

#COMMENT every line that you write yourself.


def dfs_recursion(family_id, pandemic: Pandemic):

    # base case
    if family_id == None:
        return

   # print(f'{family_id=} Retrieving Family: {family_id}\n', end="")

    # add family to pandemic
    family_response = requests.get(f'{TOP_API_URL}/family/{family_id}')

    if ("id" not in family_response.json()):
        return

    family = Family.fromResponse(family_response.json())
    #print(f'{family_id=} family.response={family_t.response}\n', end="")
    pandemic.add_family(family)

    virus1 = None
    virus2 = None

    # Get VIRUS1
    if family.virus1 != None:
        response = requests.get(
            f'http://{hostName}:{serverPort}/virus/{family.virus1}')
        if response.ok:
            virus1 = response.json()

    # Get VIRUS2
    if family.virus2 != None:
        response = requests.get(
            f'http://{hostName}:{serverPort}/virus/{family.virus2}')
        if response.ok:
            virus2 = response.json()

    # Get OFFSPRING
    offspring = []
    for id in family.offspring:
        response = requests.get(f'http://{hostName}:{serverPort}/virus/{id}')
        if response.ok:
            offspring.append(response.json())

    # ADD VIRUS1 to Pandemic
    if virus1 != None:
        v = Virus.createVirus(virus1)
        pandemic.add_virus(v)
        if v.parents != None:
            dfs_recursion(v.parents, pandemic)

    # ADD VIRUS2 to Pandemic
    if virus2 != None:
        v = Virus.createVirus(virus2)
        pandemic.add_virus(v)
        if v.parents != None:
            dfs_recursion(v.parents, pandemic)

    # ADD offspring to Pandemic
    for o in offspring:
        v = Virus.createVirus(o)
        # don't try and add virus that we have already added
        # (happens when we add a virus and then loop over the
        # virus parent's offspring)
        if not pandemic.does_virus_exist(v.id):
            pandemic.add_virus(v)


def dfs(start_id, generations):
    pandemic = Pandemic(start_id)

    # tell server we are starting a new generation of viruses
    requests.get(f'{TOP_API_URL}/start/{generations}')

    # get all the viruses in the pandemic recursively
    dfs_recursion(start_id, pandemic)

    requests.get(f'{TOP_API_URL}/end')

    print('')
    print(f'Total Viruses  : {pandemic.get_virus_count()}')
    print(f'Total Families : {pandemic.get_family_count()}')
    print(f'Generations    : {generations}')
    
    return pandemic.get_virus_count()


def main():
    # Start a timer
    begin_time = time.perf_counter()

    print(f'Pandemic starting...')
    print('#' * 60)

    response = requests.get(f'{TOP_API_URL}')
    jsonResponse = response.json()

    print(f'First Virus Family id: {jsonResponse["start_family_id"]}')
    start_id = jsonResponse['start_family_id']

    virus_count = dfs(start_id, NUMBER_GENERATIONS)

    total_time = time.perf_counter() - begin_time
    total_time_str = "{:.2f}".format(total_time)

    print(f'\nTotal time = {total_time_str} sec')
    print(f'Number of threads: {NUMBER_THREADS}')
    print(f'Performance: {round(virus_count / total_time, 2)} viruses/sec')
    
if __name__ == '__main__':
    main()
    create_signature_file()
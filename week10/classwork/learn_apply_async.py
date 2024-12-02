import json
import threading
from datetime import datetime, timedelta
import time

import requests
import multiprocessing as mp

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
CALL_COUNT = 0

char_data = []

# -------------------------------------------------------------------------------


class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        global CALL_COUNT
        http_response = requests.get(self.url)
        CALL_COUNT += 1
        # Check the status code to see if the request succeeded.
        if http_response.status_code == 200:
            self.response = http_response.json()

def display_names(title, name_list):
    print('')
    print(f'{title}: {len(name_list)}')
    names = sorted([item["name"] for item in name_list])
    print(str(names)[1:-1].replace("'", ""))

def print_film_details(film, chars, planets, starships, vehicles, species):

    print('-' * 40)
    print(f'Title   : {film["title"]}')
    print(f'Director: {film["director"]}')
    print(f'Producer: {film["producer"]}')
    print(f'Released: {film["release_date"]}')

    display_names('Characters', chars)
    display_names('Planets', planets)
    display_names('Starships', starships)
    display_names('Vehicles', vehicles)
    display_names('Species', species)

def get_responses_from_urls(urls):
    results = []
    threads = []

    for url in urls:
        t = Request_thread(url)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        results.append(t.response)

    return results

def get_response_from_url(url):
    http_response = requests.get(url)
    json = http_response.json()
    #print(f'{json=}')
    return json

def get_char_cb(result):
    global character_responses
    #print(f'{result=}')
    char_data.append(result)

def main():

    # Start a timer
    begin_time = time.perf_counter()

    # Retrieve Top API urls
    # urls = []
    t = Request_thread(TOP_API_URL)
    t.start()
    t.join()

    top_urls = t.response

    # Retrieve film 6 details
    #print(f'INDEX ZERO: {top_urls}')
    film_url = top_urls['films']
    #print(f'FILM URL: {film_url}')

    t = Request_thread(f'{film_url}6')
    t.start()
    t.join()
    film_data = t.response
    # print(film6)
    #print(f'FILM_DATA: {film_data}')
    
    pool = mp.Pool(mp.cpu_count())

    # TODO change from using threads to using a pool of processes. Use 
    # apply_async with a callback function.
    # pool_1.apply_async(func=sum_all_values, args=(x,), callback=get_sum_cb)
    for url in film_data['characters']:
        pool.apply_async(func=get_response_from_url, args=(url,), callback=get_char_cb)
        
    for url in film_data['planets']:
        pool.apply_async(func=get_response_from_url, args=(url,), callback=get_planet_cb)
    # planet_data = get_responses_from_urls(film_data['planets'])
    # starship_data = get_responses_from_urls(film_data['starships'])
    # vehicles_data = get_responses_from_urls(film_data['vehicles'])
    # species_data = get_responses_from_urls(film_data['species'])

    # Display results
    print_film_details(film_data, char_data, planet_data,
                        starship_data, vehicles_data, species_data)

    pool.close()
    pool.join()
    
    print(f'{len(char_data)}')
    print(f'There were {CALL_COUNT} calls to the server')
    total_time = "{:.2f}".format(time.perf_counter() - begin_time)
    print(f'Total time = {total_time} sec')


if __name__ == "__main__":
    main()

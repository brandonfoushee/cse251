'''
Requirements
1. Write a multithreaded program that calls a local web server. The web server is 
   provided to you. It will return data about the Star Wars movies.
2. You will make 94 calls to the web server, using 94 threads to get the data.
3. Using a new thread each time, obtain a list of the characters, planets, 
   starships, vehicles, and species of the sixth Star Wars movie.
3. Use the provided print_film_details function to print out the data 
   (you can modify it if you need).
   
Questions:
1. Is this assignment an IO Bound or CPU Bound problem (see https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)?
    >
2. Review dictionaries (see https://isaaccomputerscience.org/concepts/dsa_datastruct_dictionary). How could a dictionary be used on this assignment to improve performance?
    >
'''


from datetime import datetime, timedelta
import time
import requests
import json
import threading
from cse251functions import *


# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
CALL_COUNT = 0

#TODO create a thread class that uses the 'requests' module
#     to call the server using an URL.


def print_film_details(film, chars, planets, starships, vehicles, species):
    '''
    Print out the film details in a formatted way
    '''
    
    def display_names(title, name_list):
        print('')
        print(f'{title}: {len(name_list)}')
        names = sorted([item["name"] for item in name_list])
        print(str(names)[1:-1].replace("'", ""))

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


def main():
    #Start a timer
    begin_time = time.perf_counter()
    
    print('Starting to retrieve data from the server')

    # TODO Using your thread class, retrieve TOP_API_URL to get
    # the list of the urls for each of the categories in the form
    # of a dictionary (open your browser and go to http://127.0.0.1:8790
    # to see the json/dictionary). Note that these categories are for
    # all the Star Wars movies.

    # TODO Retrieve details on film 6 by putting a '6' at the end of the films URL.
    # For example, http://127.0.0.1:8790/films/6 gives you all the details of 
    # the sixth movie.
    
    # Iterate over each of the keys in the sixth film details and get the data
    # for each of the categories (might want to create function to do this)

    # TODO Call the display function

    print(f'There were {CALL_COUNT} calls to the server')
    total_time = time.perf_counter() - begin_time
    total_time_str = "{:.2f}".format(total_time)
    print(f'Total time = {total_time_str} sec')
    
    # If you do have a slow computer, then put a comment in your code about why you are changing
    # the total_time limit. Note: 90+ seconds means that you are not doing multithreading
    assert total_time < 15, "Unless you have a super slow computer, it should not take more than 15 seconds to get all the data."
    
    assert CALL_COUNT == 94, "It should take exactly 94 threads to get all the data"
    

if __name__ == "__main__":
    main()
    create_signature_file()

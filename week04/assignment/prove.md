![](../../banner.png)

# 04 Prove: Star Wars

## Overview

The python server in this assignment contains details of all of the Star Wars films.  You can access this information by making GET requests.  You will be retrieving the details of the 6th Star Wars film.

## Instructions

1. If you have cloned the class repo, then open the [assignment.py](assignment.py) file.
2. Your goal is to retrieve the information from the website as fast as you can.

**Coding Instructions**

- Each API call must only retrieve one piece of information
- Run the server.py program from a terminal/console program.  Simply type `python server.py`.  Note that you need the `data.txt` in the same folder as `server.py` in order for the server to work. 
- The only **fixed** or hard coded URL that you can use is TOP_API_URL.  Use this URL to retrieve other URLs that you can use to retrieve information from the server.
- You need to match the output outlined in the description of the assignment.
- You are required to use a threaded class (inherited from threading.Thread) for this assignment.  This object will make the API calls to the server. You can define your class within this Python file (ie., no need to have a separate file for the class).
- Do not add any global variables except for the ones included in this program.
- The main goal of the program is to create as many threads objects (in different parts of your program) as you can, then start them all, then wait for all of them to finish.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have this dictionary hard coded - use the API call to get this.  Then you can use this dictionary to make other API calls for data.


## Required Output

The following is the **required** output of your assignment. Only the time should be different.

```text
Starting to retrieve data from the server
-----------------------------------------
Title   : Revenge of the Sith
Director: George Lucas
Producer: Rick McCallum
Released: 2005-05-19

Characters: 34
Adi Gallia, Anakin Skywalker, Ayla Secura, Bail Prestor Organa, Beru Whitesun lars, C-3PO, Chewbacca, Darth Vader, Dooku, Eeth Koth, Grievous, Ki-Adi-Mundi, Kit Fisto, Leia Organa, Luke Skywalker, Luminara Unduli, Mace Windu, Nute Gunray, Obi-Wan Kenobi, Owen Lars, Padmé Amidala, Palpatine, Plo Koon, Poggle the Lesser, R2-D2, R4-P17, Raymus Antilles, Saesee Tiin, Shaak Ti, Sly Moore, Tarfful, Tion Medon, Wilhuff Tarkin, Yoda,

Planets: 13
Alderaan, Cato Neimoidia, Coruscant, Dagobah, Felucia, Kashyyyk, Mustafar, Mygeeto, Naboo, Polis Massa, Saleucami, Tatooine, Utapau,

Starships: 12
Banking clan frigte, Belbullab-22 starfighter, CR90 corvette, Droid control ship, Jedi Interceptor, Jedi starfighter, Naboo star skiff, Republic attack cruiser, Theta-class T-2c shuttle, Trade Federation cruiser, V-wing, arc-170,
 
Vehicles: 13
AT-RT, AT-TE, Clone turbo tank, Corporate Alliance tank droid, Droid gunship, Droid tri-fighter, Emergency Firespeeder, LAAT/i, Neimoidian shuttle, Oevvaor jet catamaran, Raddaugh Gnasp fluttercraft, Tsmeu-6 personal wheel bike, Vulture Droid,

Species: 20
Cerean, Chagrian, Clawdite, Droid, Geonosian, Human, Iktotchi, Kaleesh, Kel Dor, Mirialan, Muun, Pau'an, Quermian, Skakoan, Tholothian, Togruta, Toong, Twi'lek, Wookie, Yoda's species,

Total Time To complete = 7.32 sec
There were 94 calls to the server
```

## How to use the requests package

There are a number of Python packages that can help you make URL calls.  We will be using the package `requests`.

### Install Package

This package needs to be installed.  Read the details on how to install packages in the `resources/software` section of the course.  Using pip, the command is `pip install requests`.  Using Python, it's `python -m pip install requests`.  (Mac users might need to use pip3)

### How to make an URL call to the server

```python
import requests
import json

# Const Values
TOP_API_URL = r'http://127.0.0.1:8790'

if __name__ == '__main__':

    response = requests.get(TOP_API_URL)
    
    # Check the status code to see if the request succeeded.
    if response.status_code == 200:
        data = response.json()
        print(data)

		# Example to get person 1 url
        print('\nHere is the URL for person id = 1:', f'{data["people"]}1')
    else:
        print('Error in requesting ID')
```

Output:

```
{
    'people': 'http://127.0.0.1:8790/people/', 
    'planets': 'http://127.0.0.1:8790/planets/', 
    'films': 'http://127.0.0.1:8790/films/', 
    'species': 'http://127.0.0.1:8790/species/', 
    'vehicles': 'http://127.0.0.1:8790/vehicles/', 
    'starships': 'http://127.0.0.1:8790/starships/'
}

Here is the URL for person id = 1: http://127.0.0.1:8790/people/1
```

## Rubric

Item | Point Value
--- | ---
Runs without errors | 30
Loops over returned URLs returned to make new threads/calls | 20
Makes correct number of calls to server (passes Assert) | 20
Finishes under required time limit (or justification provided) | 20
Questions answered | 10

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be plagiarized will be graded according to the `ACADEMIC HONESTY` section in the syllabus. Personalize your code by adding comments explaining how your code works. This provides evidence that you wrote it yourself. You are allowed to work with other students, but your comments need to be in your own words.

## Submission

When finished, upload your assignment.py and signature files to Canvas (no zip files).

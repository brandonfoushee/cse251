import inspect
import json
import os
import platform
import uuid
import hashlib
from datetime import date, datetime
from student_info import *
import pathlib

from PIL import Image, ImageDraw, ImageFont
from termcolor import colored

# ===============================================================================================


def print_dict(dict, title=''):
    """ Display a dictionary in a structured format """
    if title != '':
        print(f'Dictionary: {title}')
    print(json.dumps(dict, indent=3))


# ===============================================================================================
def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename) as json_file:
            data = json.load(json_file)
        return data
    else:
        return {}


def printError(errStr):
    print(colored("#" * len(errStr) +
          f"\n{errStr}\n" + "#" * len(errStr), "red"))
    exit()


def create_signature_file():
    if SIS_ID == None or SIS_ID == '012345678':
        printError("Enter your SIS_ID in the resources/student_info.py file")

    if STUDENT_NAME == None or STUDENT_NAME == 'firstname.lastname':
        printError("Enter your first and last name in the resources/student_info.py file")

    width = 725
    height = 400

    char_count = 0
    word_count = 0
    line_count = 0
    frame = inspect.stack()[1]
    assignment_full_path = frame[0].f_code.co_filename
    if "prove" in assignment_full_path:
        print("grading...")
        return
    
    assignment_name = os.path.basename(assignment_full_path)
    
    with open(assignment_full_path, 'r') as f:
        for line in f:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += sum(len(word) for word in words)

    divide_index = 70
    if len(assignment_full_path) > divide_index:
        # find the nearest directory divider before the div_index characters
        for c in range(51, 0, -1):
            if assignment_full_path[c] == os.sep:
                divide_index = c
                break
        assignment_full_path = assignment_full_path[:divide_index] + '\n' + ' ' * 9 + assignment_full_path[divide_index:]
        
    text = f"Filename={assignment_full_path} \
            \nDATEIME={datetime.now()} \
            \nUUID={uuid.uuid4()} \
            \nNODE={uuid.getnode()} \
            \nLOGIN={os.getlogin()} \
            \nHOST={platform.node()} \
            \nARCH={platform.architecture()} \
            \nVERSION={platform.version()} \
            \nCORES={platform.processor()} \
            \nPROC={platform.machine()} \
            \n\nCharacters in {assignment_name[:-3]}={char_count} \
            \nWords in {assignment_name[:-3]}={word_count} \
            \nLines in {assignment_name[:-3]}={line_count} \
            \n\nSIS_ID={SIS_ID} \
            \nName={STUDENT_NAME} \
            \n\nOn my honor: \
            \n1. I wrote this myself\
            \n2. I have not copied any code from a current or previous student of CSE251 \
            \n3. I have added a comment to every line of code that I added to this assignment"
    filename = f'{SIS_ID}_{assignment_name[:-3]}_signature.jpeg'
    # get the absolute path to the directory this file exists in
    resource_path = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    # append the font name
    font_path =  os.path.join(resource_path, "COURBD.TTF")

    img = Image.new('CMYK', (width, height))
    draw1 = ImageDraw.Draw(img)
    font1 = ImageFont.truetype(font_path, 14)
    draw1.text((10, 15), text, (255, 255, 255), font=font1)
    img.save(filename)


def is_prime(n: int):
    """
    Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test

    Parameters
    ----------
    ``n`` : int
        Number to determine if prime

    Returns
    -------
    bool
        True if ``n`` is prime.
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

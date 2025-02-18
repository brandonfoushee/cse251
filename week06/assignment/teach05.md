![](../../banner.png)

# 05 Teach: Using Queues

## Overview

Today's team activity will be using a queue. 

## Assignment

The file `urls.txt` contains a list of URLs for the program `server.py`.  You will need to run the server.py program for this team activity.  This is the same server used in the Star Wars assignment.  You will be creating a thread that will read this data file line by line and placing the URLs into a queue.  The other thread(s) will take URLs from the queue and request information using that URL.  Use the `requests` module for Internet requests.

[](team_graph.png)

## Instructions

- NO global variables!!!
- Review all of the given code so you understand it before adding your code.
- Recommended that you set the RETRIEVE_THREADS to 1, get that to work, and then increase it to 4.

## Requirements

1. In a terminal (mac) or command window (windows), run the server with the command `py server.py` for Windows, `python3 server.py` for Mac.  You can check the documentation on the Star Wars assignment on how to run the server.

2. Start with `RETRIEVE_THREADS = 1` while implementing the threads.  Implement your program in steps - building on code that works.

3. You final goal is to set `RETRIEVE_THREADS = 4` where you will create 4 `retrieve_thread()` threads.

4. Once you have the program working with multiple threads, run the program using different `RETRIEVE_THREADS` values.  Does your program complete faster with more threads?  Is there a point where adding more threads to this program doesn't improve completion time?

## Sample Solution

No solution provided.


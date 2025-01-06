![](../../banner.png)

# 13 Prove: Family Search

## Overview

You will be implementing both a [depth-first algorithm](https://www.youtube.com/watch?v=9RHO6jU--GU) (aka. DFS) and [breadth-first algorithm](https://www.youtube.com/watch?v=86g8jAQug04) (aka. BFS).  Please refer to those two video links for more information on these algorithms.  You will be retrieving family tree information from a server.  This server can handle multiple concurrent requests.  Each request takes the server 0.25 seconds to reply.

The assignment is divided into two parts.  The first part will retrieve the family tree information using DFS.  The second part will use BFS.

There are a number of classes in `common.py` that you can use:

**Person**

This class will decode and hold person details sent from the server.

**Family**

This class holds the family information from the server.

**Tree**

The tree class allows you to build a family tree from the families and individuals that you retrieve from the server.

**Request_thread**

The only method of requesting information from the server.

## Assignment

### Assignment files

- `functions.py` - This is the Python file that you will be changing and submitting for the assignment. This is the file you will be writing your code in.
- `assignment.py` - This file contains main() and will call your functions in the `functions.py` Python file.
- `common.py` - Contains common classes and functions for the assignment.
- `runs.txt` - Contains which search algorithms will be run and how many generations will be retrieved from the server.  You can modify this file while you are testing your program.

### FS Server

There is a server program that you will need to run in its own terminal window on your computer.  The program is `server.py`.  

1. Open a command or terminal window on your computer.
1. Go to the directory of the assignment.
1. Type `python server.py` to start the server.
1. Note if the server is very busy it might not reply with a 200 reply code or might return an empty JSON.  You should handle these issues in your program.

While running, the server will display requests and replies from your assignment.  It also displays the current number of active threads making requests and the maximum number of threads.

### Part 1

- The function `depth_fs_pedigree()` will retrieve the family tree using a recursive algorithm.
- Your task is to use threads to make this function faster.  There is no limit on the number of threads you can use.
- You must build the pedigree tree starting with the starting family id.  You must write your program to handle different family information from the server (ie., number of families, number of children, etc.).  A family might be missing a parent and the number of children is random.
- You must retrieve all individuals in a family and add them to the tree object. (ie., husband, wife and children)
- Suggestion: get the function to work without using threads first.
- **Your goal is to execute part 1 in under 10 seconds for 6 generations**

### Part 2

- In this part, you will be retrieving the family information using a breadth-first algorithm in the function `breadth_fs_pedigree()`.
- Your goal is to make this function as fast as possible by using threads.
- You must retrieve all individuals in a family (ie., husband, wife and children)
- Do not use recursion for this algorithm.
- **Your goal is to execute part 2 in under 10 seconds for 6 generations**

### 10% Bonus

- A 10% bonus if you can limit the number of threads to 5 while retrieving the family information in part 2 using function `breadth_fs_pedigree_limit5()`.  
- The server must not have more than 5 active threads at a time. (watch the output from the server to see number of activity threads)
- Needs to run faster than if you only used one thread.


## Rubric

**breadth-first search**
Item | Point Value
--- | ---
Runs without errors (including deadlocks) | 20
All calls to server are in a new thread | 10
Number of people and families matches the server | 10
Runs in under 10 seconds | 10

**depth-first search**
Item | Point Value
--- | ---
Runs without errors (including deadlocks) | 20
All calls to server are in a new thread | 10
Number of people and families matches the server | 10
Runs in under 10 seconds | 10

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be plagiarized will be graded according to the `ACADEMIC HONESTY` section in the syllabus. Personalize your code by adding comments explaining how your code works. This provides evidence that you wrote it yourself. You are allowed to work with other students, but your comments need to be in your own words.

## Submission

When finished, upload your functions.py Python, and assignment.log, and signature files to Canvas (no zip files).


![](../../banner.png)

# 12 Prove: Pandemic

## Overview

Now that you are a multithreading expert, you are being hired by a medical research company to convert their virus tracking program from single threaded to multithreaded. Their program has to interface with a viral online database to figure out how viruses are mutating. However, they don't control the database and it takes one second to make a query to obtain the necessary data. They need you to make their working program multithreaded to speed up the time it takes to track the virus mutations. 

## Assignment

The company wrote two recursive programs: `bfs.py` (breadth-first search) and `dfs.py` (depth-first search). Your job is to modify these files to run using threads. 

### Description of the problem

1. The company wrote a simulator program `virusServerSimulator.py` that simulates the online database. Run this file in a command line or terminal.
2. The server contains a SLEEP global that you can decrease while you are testing your modifications. Once you have your threading changes working, change it back to one second.
3. The company also wrote a file called `virusApi.py` that contains common classes that are used both by the server and in their programs. Careful making changes to this file since the "real" online virus database API can't be changed by you. Adding print statements to help you debug is acceptable.
4. You should create your own thread class, similar to Request_Thread class used on other assignments.
5. The company has requested that you obtain a minimum performance of 5 viruses/sec (this will print out at the end of a program run). With no threads, the existing performance is 0.49 viruses/sec (this is what the company gets on their computer, so may be different on your computer):

```text
Pandemic starting...
First Virus Family id: 1000
############################################################

Total Viruses  : 189
Total Families : 63
Generations    : 6

Total time = 384.93 sec
Number of threads: 0
Performance: 0.49 viruses/sec
```

6. The `virusServerSimulator.py` will always generate 189 viruses, 63 families for 6 generations of viruses.
7. You can change the number of generations to run at the top of the `bfs.py` and `dfs.py` files. Start with 2 while you are getting your threading to work.

### Sample output of the assignment

**bfs.py**
```text
Pandemic starting...
############################################################
First Virus Family id: 1000

Total Viruses     : 189
Total Families    : 63
Generations       : 6

Total time = 16.44 sec
Number of threads: 380
Performance: 11.5 viruses/sec
```
**dfs.py**
```text
############################################################
First Virus Family id: 1000

Total Viruses  : 189
Total Families : 63
Generations    : 6

Total time = 16.51 sec
Number of threads: 380
Performance: 11.44 viruses/sec
```

## Rubric

**bfs.py**
Item | Point Value
--- | ---
Runs without errors (including deadlocks) | 20
All calls to server are in a new thread | 20
Correct number of viruses and families found for 6 generations | 10

**dfs.py**
Item | Point Value
--- | ---
Runs without errors (including deadlocks) | 20
All calls to server are in a new thread | 20
Correct number of viruses and families found for 6 generations | 10

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be plagiarized will be graded according to the `ACADEMIC HONESTY` section in the syllabus. Personalize your code by adding comments explaining how your code works. This provides evidence that you wrote it yourself. You are allowed to work with other students, but your comments need to be in your own words.

## Submission

When finished

- Upload your bfs.py and signature files to Canvas (no zip files)
- Upload your dfs.py and signature files to Canvas (no zip files)


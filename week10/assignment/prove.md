![](../../banner.png)

# 10 Prove: Processing Task Files

## Overview

Your assignment will process a directory full of task files.  Each file will contain details on the task to be preformed.

## Assignment

1. Download the [assignment.py](assignment.py), [create_tasks.py file](create_tasks.py) [server.py file](server.py), [words.txt](words.txt) and [data.txt](data.txt) files.
2. Follow the instructions found in the `assignment.py`
3. Run the Python program **create_tasks.py** to create the task files.
4. There are 5 different tasks that need to be processed.  Each task needs to  have it's own process pool.  The number of processes in each pool is up to you.  However, your goal is to process all of the tasks as quicky as possible using these pools.  You will need to try out different pool sizes.
5. The program will load a task one at a time and add it to the pool that is used to process that task type.  You can't load all of the tasks into memory/list and then pass them to a pool.
6. You are required to use the function apply_async() for these 5 pools. You can't use map(), or any other pool function.  Use callback functions or get() to optain the necessary return values from the processes.
7. Each pool will collect that results of their tasks into a global list. (ie. result_primes, result_words, result_upper, result_sums, result_names) --> remember that global variables are not shared across processes.
8. The task_* functions contain general logic of what needs to happen.
9. Run the server.py program from a terminal/console program.  Simply type `py server.py` (or `python3 server` if on a Mac).  This server is the same one used for the Star Wars assignment.

### create_tasks.py program

This program will create the task files that your assignment will process.  There are two features for creating the task files.  When you run to the program, you get this prompt:

```
Do you want all task files (y), or just a few for testing (n): 
```

If you select 'y' to create all of the task files (4034 of them).  You are required to process of these files for your assignment.  However, while you are developing your program, you can select the 'n' option to only create 5 task files.  Each of these task files represents one of the 5 different tasks your assignment must handle.

Truncated output:

```
...

http://127.0.0.1:8790/people/52/ has name Ki-Adi-Mundi

http://127.0.0.1:8790/people/4/ has name Darth Vader

http://127.0.0.1:8790/people/21/ has name Palpatine

http://127.0.0.1:8790/people/6/ has name Owen Lars

Primes (3): 1000
Words (3): 1000
Uppercase (1): 1000
Sums (2): 1000
Names (4): 34
Finished processes 4034 tasks = 20.497827291488647
```

## Rubric

Item | Point Value
--- | --- |
Runs without errors | 30
One pool per task category used | 20
Selection of pool size demonstrates understanding of IO Bound vs CPU Bound tasks | 20
Callback lists contain correct number of items | 20
Questions answered | 10

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be plagiarized will be graded according to the `ACADEMIC HONESTY` section in the syllabus. Personalize your code by adding comments explaining how your code works. This provides evidence that you wrote it yourself. You are allowed to work with other students, but your comments need to be in your own words.

## Submission

When finished, upload your assignment.py and signature files to Canvas (no zip files).
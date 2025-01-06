![](../../banner.png)

# 06 Prove: Space Factory and Space Buyers - Part 2

## Overview

You will be using queue(s) and thread semaphore(s) to synchronize many threads in the production and selling of spaceships.

## Project Description

This is a continuation of the previous assignment.  Instead of one factory and one buyer, you will have multiple of each.  The restriction of only producing `MAX_QUEUE_SIZE` is still in place.

## Assignment

1. Download the [assignment.py](assignment.py) file.
2. Review the instructions found in the Python file as well as the global constants.
4. The function `run_production()` will be passed different number of factories and buyers that are to be created for a production run.
5. You must not use the Python queue object for this assignment.  Use the provided queue class.

Here is a sample run of the completed assignment.  The number of spaceships each manufacturer produces is random:

```
Begin production run with factory_count=1 and buyer_count=1
Spaceship Factories : 1
Spaceship Buyers    : 1
Run Time            : 0.72 sec
Factory Stats       : [289]=289
Buyer Stats         : [289]=289

Begin production run with factory_count=1 and buyer_count=2
Spaceship Factories : 1
Spaceship Buyers    : 2
Run Time            : 0.73 sec
Factory Stats       : [286]=286
Buyer Stats         : [141, 145]=286

Begin production run with factory_count=2 and buyer_count=1
Spaceship Factories : 2
Spaceship Buyers    : 1
Run Time            : 0.67 sec
Factory Stats       : [252, 234]=486
Buyer Stats         : [486]=486

Begin production run with factory_count=2 and buyer_count=2
Spaceship Factories : 2
Spaceship Buyers    : 2
Run Time            : 0.78 sec
Factory Stats       : [298, 278]=576
Buyer Stats         : [287, 289]=576

Begin production run with factory_count=2 and buyer_count=5
Spaceship Factories : 2
Spaceship Buyers    : 5
Run Time            : 0.66 sec
Factory Stats       : [259, 211]=470
Buyer Stats         : [92, 99, 95, 95, 89]=470

Begin production run with factory_count=5 and buyer_count=2
Spaceship Factories : 5
Spaceship Buyers    : 2
Run Time            : 0.89 sec
Factory Stats       : [247, 240, 284, 208, 258]=1237
Buyer Stats         : [613, 624]=1237

Begin production run with factory_count=10 and buyer_count=10
Spaceship Factories : 10
Spaceship Buyers    : 10
Run Time            : 0.74 sec
Factory Stats       : [209, 200, 252, 231, 281, 201, 270, 222, 245, 225]=2336
Buyer Stats         : [228, 228, 233, 237, 222, 235, 235, 243, 250, 225]=2336
```


## Rubric

Item | Point Value
--- | ---
Runs without errors | 30
Semaphore used to control queue size | 15
Semaphore used to control reading empty queue | 15
Queue size not used in IF statement | 5
Spaceships produced equals spaceships bought (assert passes) | 20
Barrier correctly used to ensure sentinel not placed prematurely on queue | 10

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be plagiarized will be graded according to the `ACADEMIC HONESTY` section in the syllabus. Personalize your code by adding comments explaining how your code works. This provides evidence that you wrote it yourself. You are allowed to work with other students, but your comments need to be in your own words.

## Submission

When finished, upload your assignment.py and signature files to Canvas (no zip files).
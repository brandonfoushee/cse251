![](../../banner.png)

# 03 Prove: Finding Prime Numbers

## Overview

Programs can run with and without threads.  In this assignment you will be taking a program that counts the number of prime numbers in a range and converting it to use threads to find these prime numbers.

## Instructions

See the list of requirements and psuedocode in [assignment](assignment.py).

Psuedocode: 
1. Create variable for the start number (100_000_000)
2. Create variable for range of numbers to examine (370_803)
3. Create variable for number of threads (start with 1 to get your program running,
   then increase to 5, then 10).
4. Determine an algorithm to partition the 110,003 numbers based on 
    the number of threads. Each thread should have approx. the same amount
    of numbers to examine. For example, if the number of threads is
    5, then the first 4 threads will examine 74,160 numbers, and the
    last thread will examine 74,163 numbers. Determine the start and
    end values of each partition.
5. Use these start and end values as arguments to a function.
6. Use a thread to call this function.
7. Create a function that loops from a start and end value, and checks
   if the value is prime using the isPrime function. Use the globals
   to keep track of the total numbers examined and the number of primes
   found. 

## Rubric

Item | Point Value
--- | ---
Runs without errors | 20
Uses a variable amount of threads | 25
Fairly divides up the numbers among the threads | 25
Asserts pass | 20
Questions answered | 10

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be plagiarized will be graded according to the `ACADEMIC HONESTY` section in the syllabus. Personalize your code by adding comments explaining how your code works. This provides evidence that you wrote it yourself. You are allowed to work with other students, but your comments need to be in your own words.

## Submission

When finished, upload your assignment.py and signature files to Canvas (no zip files).


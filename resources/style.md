# Style

## "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." – Martin Fowler


Style is subjective and is more art than science. The goal of my style rules is to make your code look more professional.

Looking "professional", of course, may be different from company to company. In an academic setting, style also provides
a way for you as a student to make the code "your own". This helps in two ways:

1. Provides uniqueness to your code: providing evidence that your wrote it.
2. Makes it easier for a reviewer (including yourself) to understand your thinking.

So, here are some ideas about how make your code professional looking:

1. Remove/Revise all TODO comments (these are just there to help you know what to write, but once you write it, 
   the comment should be either removed or revised with an explanation). Also, remove the keyword 'pass'. This is used for "stub functions", meaning for a function that is not fully implemented yet. The pass keyword prevents the 
   compiler from throwing an error if the function has no defined body.

2. Use predefined formatting: turn on formatting and you can click a hot-key and autoformat your code
   (see https://code.visualstudio.com/docs/python/editing).

3. Provide comments for algorithms. A block of code that works to produce a result is an algorithm. 
   Provide an explanation for how the algorithm works. If you can't explain it, then chances are the someone else won't be 
   able to understand it either (i.e., won't want to take the time to understand it).
      
5. Use meaningful names for your variables. Better to give your variables a name to conveys its purpose. The exception
   to this is using 'i' for an index. But avoid naming variables things like 'x' or 'my_variable'.

6. Use whitespace to help split code into "paragraphs". If a few lines of code all work together to do something (like
   a FOR loop), then put whitespace between the top and bottom of it to help separate it. This makes reading
   your code much easier (happy grader = more points).
   
If you feel you've received unfair deductions for style, please email/speak with me. 

I strongly believe that using good style helps focus your mind on your solution, aids in debugging, better pattern
recognition, and help other people understand your code.

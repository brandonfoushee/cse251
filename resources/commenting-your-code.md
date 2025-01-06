# Commenting Your Code

Unfortunately, plagiarism is common in computer science education. Possible reasons include the easiness of copying and pasting code or students not fully understanding that copying code found online is considered plagiarism. 

To prevent students from submitting plagiarized code, students will be required to comment every line of code that they write. These comments will not fully prevent a student from copying code, but the comments act as a barrier to make plagiarism harder.

Rule for comments in CSE251:
1. Place a comment above every line of code that you write
```
# Creating a thread to compute the product of a range of numbers
t = threading.Thread(target=computerProduct, args=(number,))
```
2. Place a space after the comment character # and use a capital letter in the first word.

3. Place a blank line before a comment
```
# Creating a thread to compute the product of a range of numbers
t = threading.Thread(target=computerProduct, args=(number,))

# Start the computeProduct thread
t.start()

# Wait for the computerProduct thread to finish
t.join()
```
4. Place a comment on any functions you write
```
# Accepts an integer 'n' then sets a global variable equal to 
# the product of all numbers from 1 to (n - 1)
def computeProduct(n: int):
```
5. A comment should demonstrate an understanding of the line it comments:

Bad example:
```
# Start of a loop
for i in range(n):
```
Better example:
```
# Factorial of 'n'
for i in range(n):
```
Even better example:
```
# Loop from 1 to (n - 1) to compute the factorial of 'n'
for i in range(n):
```

For purposes of this class, the student should convey not only WHAT the line of code is doing, but WHY it is doing it. Notice that in the 'bad example' only the WHAT is stated. In the 'better example' the WHY is provided, but not the WHAT. In the 'even better example' both the WHAT and WHY are stated.

More examples:

## Parrot comments
Bad | Good
--- | ---
```# Initialize integer and set it to 1```<br>```i = i``` | ```# Counter to keep track of the number of spaceships, setting initial```<br>```# value to one since we already have one spaceship```<br>```number_spaceships = 1```
```# Loop forever```<br>```while True:``` | ```# Keep looping to pull a spaceship from the queue, ```<br>```# loop will break when None gets popped from queue```<br>```while True:```

## Meaningless comments
Bad | Good
--- | ---
```# Required print statement```<br>```print(f'Time to complete = {total_time} sec')``` | ```# This program should complete in less than 10 seconds```<br>```print(f'Time to complete = {total_time} sec')```

![](../../banner.png)

# 01 Prepare: Python Overview

There are certain Python knowledge that you should have to be successful in this class. The information in this section is to help you review this knowledge. Sometimes students are knowledgeable in some computer science areas but lack the experience for how to "do it" in Python. Also, some students might just not have a lot of experience in coding and need more useful examples.

This overview is broken into the following areas:
1. Object-Oriented Programming
2. Working with object types
3. The "Python" way of doing things
4. Advanced techniques 

## Object-Oriented Programming

I will not cover in-depth all that could be said about OOP. Instead, I will focus on what you should know to be successful in this class. If you need more explanation or examples see https://realpython.com/python3-object-oriented-programming/

### Creating classes

To create a class you put the word 'class' at the beginning of the line, followed by the name of your class.

```
class MyClass:
```

If you need to pass a parameter when you create an object of you class, then define a constructor. In Python, a constructor is a function with the name of '__init__'

```
class MyClass:
    def __init__(self, myParameter):
        self.myParameter = myParameter
```

The 'self' parameter is a way to reference the object that is being instantiated. So, if I instantiate an object of this class doing this:

```
myClass = MyClass(10)
```

An object is created in memory with a reference name of 'myClass'. The constructor is automatically called upon instantiation. I passed in the value '10' as a parameter. The self.myParameter creates a new attribute on this object and sets the value of this attribute to '10'. 

Now I can reference the attribute by using the dot operator:

```
print (f'{myClass.myParameter})
```

VS Code knows that the object class type is MyClass. It uses Intellisense to give you a list of attributes and functions available to you when you enter the period (dot) after the object name. This is super important to help you know what functions or attributes you can call. 

This only works if VS Code knows the object type.

### Working with object types

Python is a dynamically typed language [statically vs dynamically typed languages](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages). While this can make the syntax easier when writing your code, there is a trade-off since you don't always know what functions or attributes you have available to you. Also, trivial compile errors are not always caught when writing your code and you need to run your code to discover these errors.

While you don't need to specify the type of an object, knowing the type is essential when writing your code. One very useful thing you can use in Python is called [type hinting](https://realpython.com/lessons/type-hinting/).

```
class MyClass:
    def __init__(self, myParameter: int):
        self.myParameter = myParameter
```

The type of the parameter can be set by placing a colon after the parameter name, space, then the type.

This can be useful if the object being passed in is a class with functions:

```
class MyOtherClass:
    def __init__(self, myclass: MyClass):
        self.myclass = myclass
    def run(self):
        print(f'{self.myclass.myParameter}')
```

Now when you are writing your code, you can type `self.myclass.` and VS Code will produce a drop down list of functions and attributes that this object has. Because you put the type hint of `MyClass` on the parameter `myclass`, it knows that the attribute `myParameter` is availabe for me to select. 

In this class, you are going to be using many classes that have already been written for you. Most of these classes have functions that you will need to use. Being able to quickly see all the functions that you can use (with a DocuString available for most), will help you know what to do. Also, if the function that you are calling uses type hinting, then if you pass in an object of the incorrect type, you will see this error in VS Code. Knowing about errors before running your code can be very useful as you write your code.

### The "Python" way of doing things
There are some ways of doing things in Python that is different than other languages.

One useful statement is `with` (see https://realpython.com/python-with-statement). This allows us to take advantage of built-in context managers to handle setting up and tearing down objects or other resources. The `with` keyword will ensure that if an object or resource has a defined context manager, that the context manager is used. The context manager works similarly to a try/finally block.

Using with ensures that locks and files get released or closed after use:

```python
with lock:
    # The lock is acquired automatically 
    # Do critical section of code
# The lock is automatically released after the with block exits
```
Using `with` to open a file is covered further below under Advanced Techniques.

### Advanced Techniques

**Opening A File**
To open a file you want to create a file object with the [open](https://www.w3schools.com/python/ref_func_open.asp) function:
```f = open(filename, "r")```

You can specify "r" to mean that you are only opening the file to read. And "w" means write (which allows read and write).

The 'f' object is of type TextIOWrapper which has many read and write functions. One useful way to read a line from a file is to loop over the file object. This will automatically use the readline function:
```python
for line in f:
    print(line)
```

Another useful approach is to use the defined context manager of the open function to ensure that the file object gets closed after it is opened:
```python
with open(filename) as f:
    for line in f:
        data_queue.put(line.strip())
```

This will open the file and create an object named 'f' as the file object. Then, each line in the file is read and stored in the line string object. Finally, the string is stored in a queue.

Notice that the 'strip()' function is called on the line string object (see https://www.w3schools.com/python/ref_string_strip.asp). This removes any spaces at the beginning or end of the string as well as if there is a Carriage Return and Line Feed (CR/LF) ascii characters at the end.

If you need to write a line to a file over and over, then use the 'a' (append) mode with the writeline function:
```python
with open(filename, "a") as f:
    f.writelines("writing a line of text to the file")
```

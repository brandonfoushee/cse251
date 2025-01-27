"""
Purpose: Drawing with Python Turtle

The follow program will draw a series of shapes - squares, circles, triangles
and rectangles.  

There is a Python class called SlowTurtle that is used to hold the drawing
commands that are created by the program.  This is required because threads can
not draw to the screen - only the main thread can do this.

Instructions:

- Find the "TODO" comment below and add your code that will use threads.
- No global variables necessary.
- Run the program before doing anything and watch it draw the turtle shapes in order.
- Your goal is to modify the code to get the shapes to draw in concurrently. This 
  does not mean that they will draw in parallel. Why can't they draw in parallel?
  Walk through the slow_turtles file and notice what the code is doing and not
  doing. It is not actually drawing to the screen. Instead, it is make a list of 
  drawing commands. Your goal is to make threads that all put their drawing commands
  into the list. Then, after the list is complete, the commands are given to the
  build-in Turtle class and drawn to the screen. 

- You will need to use Locks to get this to work. Why? Where should the locks go? Discuss with your team.
"""


import math
import threading
from turtle import RawTurtle
from slow_turtles import *


def draw_square(tur: SlowTurtle, x: int, y: int, side, color='black'):
    """Draw Square"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    for _ in range(4):
        tur.forward(side)
        tur.right(90)


def draw_circle(tur: SlowTurtle, x: int, y: int, radius, color='red'):
    """Draw Circle"""
    steps = 8
    circumference = 2 * math.pi * radius

    # Need to adjust starting position so that (x, y) is the center
    x1 = x - (circumference // steps) // 2
    y1 = y
    tur.move(x1, y1 + radius)

    tur.setheading(0)
    tur.color(color)
    for _ in range(steps):
        tur.forward(circumference / steps)
        tur.right(360 / steps)


def draw_rectangle(tur: SlowTurtle, x: int, y: int, width, height, color='blue'):
    """Draw a rectangle"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    tur.forward(width)
    tur.right(90)
    tur.forward(height)
    tur.right(90)
    tur.forward(width)
    tur.right(90)
    tur.forward(height)
    tur.right(90)


def draw_triangle(tur: SlowTurtle, x: int, y: int, side, color='green'):
    """Draw a triangle"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    for _ in range(4):
        tur.forward(side)
        tur.left(120)


def draw_coord_system(tur: SlowTurtle, x: int, y: int, size=300, color='black'):
    """Draw coordinate lines"""
    tur.move(x, y)
    for i in range(4):
        tur.forward(size)
        tur.backward(size)
        tur.left(90)


def draw_squares(tur: SlowTurtle, lock: threading.Lock):
    """Draw a group of squares"""
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            with lock:
                draw_square(tur, x - 50, y + 50, 100)


def draw_circles(tur: SlowTurtle, lock: threading.Lock):
    """Draw a group of circles"""
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            with lock:
                draw_circle(tur, x, y-2, 50)


def draw_triangles(tur: SlowTurtle, lock: threading.Lock):
    """Draw a group of triangles"""
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            with lock:
                draw_triangle(tur, x-30, y-30+10, 60)


def draw_rectangles(tur: SlowTurtle, lock: threading.Lock):
    """Draw a group of Rectangles"""
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            with lock:
                draw_rectangle(tur, x-10, y+5, 20, 15)

def draw(tur: SlowTurtle, main_turtle: RawTurtle):
    """Draw different"""
    
    start_time = time.perf_counter()
    
    # Draw Coords system
    tur.pensize(0.5)
    draw_coord_system(tur, 0, 0, size=375)
    tur.pensize(4)

    print('-' * 50)
    print('Start Drawing')
    tur.move(0, 0)

    # TODO - use threads to draw shapes
    lock = threading.Lock()
    threads = []
    threads.append(threading.Thread(target=draw_squares, args=(tur, lock)))
    threads.append(threading.Thread(target=draw_circles, args=(tur, lock)))
    threads.append(threading.Thread(target=draw_triangles, args=(tur, lock)))
    threads.append(threading.Thread(target=draw_rectangles, args=(tur, lock)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print('All drawing commands have been created')

    tur.move(0, 0)
    print(f'Number of Drawing Commands: {tur.get_command_count()}')

    # Play the drawing commands that were created
    tur.play_commands(main_turtle)
    "Total drawing time: {:.2f}".format(time.perf_counter() - start_time)
    tur.clear()


def main():
    # Shouldn't need to modify any code in main
    
    # create a Screen Object
    screen = turtle.Screen()

    # Screen configuration
    screen.setup(800, 800)

    # Make RawTurtle Object (built in Python class)
    main_turtle = turtle.Turtle()
    main_turtle.speed(0)
    main_turtle.shape('turtle')

    # Customized CSE251 Turtle object
    turtle251 = SlowTurtle()

    # Draw the turtles
    draw(turtle251, main_turtle)

    # Waiting for user to close window
    turtle.done()

if __name__ == "__main__":
    main()

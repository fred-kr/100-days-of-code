# TODO: Create steerable turtle. W is forwards, S is backwards, A is counter-clockwise rotation, D
# is clockwise rotation. Basically an Etch-A-Sketch.

from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    tt.forward(10)

def move_backwards():
    tt.back(10)
    
def rotate_counter_clockwise():
    new_heading = tt.heading() + 10
    tt.setheading(new_heading)

def rotate_clockwise():
    new_heading = tt.heading() - 10
    tt.setheading(new_heading)

def clear():
    tt.clear()
    tt.penup()
    tt.home()
    tt.pendown()
    
def reset():
    tt.reset()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)
screen.onkey(key="r", fun=reset)






screen.exitonclick()
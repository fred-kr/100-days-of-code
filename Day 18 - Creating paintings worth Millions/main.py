from turtle import Turtle, Screen
from random import randint

ttt = Turtle()

# Draw a square
# for i in range(4):
#     ttt.forward(100)
#     ttt.right(90)

# Draw a dashed line
# for i in range(15):
#     ttt.forward(10)
#     ttt.penup()
#     ttt.forward(10)
#     ttt.pendown()

# Draw different shapes (triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon)
# Every shape has random color and a length of 100
# Angles of every shape are 360 / number of sides
screen = Screen()
screen.colormode(255)

def draw_spirograph(size_of_gap):
    ttt.speed("fastest")
    for i in range(int(360 / size_of_gap)):
        ttt.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        ttt.circle(100)
        ttt.setheading(ttt.heading() + size_of_gap)
        
draw_spirograph(5)

def random_walk():
    ttt.speed("fast")
    ttt.pensize(15)
    while True:
        ttt.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        ttt.forward(30)
        new_direction = randint(0, 3)
        if new_direction == 0:
            ttt.setheading(0)
        elif new_direction == 1:
            ttt.setheading(90)
        elif new_direction == 2:
            ttt.setheading(180)
        elif new_direction == 3:
            ttt.setheading(270)

# random_walk()

# for i in range(3, 11):
#     ttt.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     for j in range(i):
#         ttt.forward(100)
#         ttt.right(360 / i)

screen.exitonclick()

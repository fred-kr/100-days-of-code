# from colorgram import extract
import random as rd
from turtle import Turtle, Screen

color_list = [
    (197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205), (104, 129, 152), (67, 64, 59), (112, 135, 140), (175, 196, 206)
]

t = Turtle()

screen = Screen()
screen.colormode(255)

for row in range(10):
    for column in range(9):
        t.dot(20, color_list[rd.randint(0, len(color_list) - 1)])
        t.penup()
        t.forward(50)
        t.dot(20, color_list[rd.randint(0, len(color_list) - 1)])
        t.penup()
    if row % 2 != 0:
        t.left(90)
        t.forward(50)
        t.left(90)
    else:
        t.right(90)
        t.forward(50)
        t.right(90)
        
screen.exitonclick()
# Task: find all the colors in the image and create a list of tuples with RGB values

# def get_rgb_values():
#     rgb_values = []
#     colors = extract("Day 18 - Intro to Graphics with Turtle\hirst-painting\money_laundering.jpg", 34)
#     for color in colors:
#         rgb_values.append((color.rgb.r, color.rgb.g, color.rgb.b))
#     return rgb_values[4:]
# Reqs for Hirst painting:
    # 10 x 10 grid
    # dot size 20
    # spacing between dots 50
import random
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -280:
            self.goto(self.xcor(), new_y)


# REVIEW: Maybe look at ways to make CPU paddle more intelligent
class Computer(Paddle):
    def __init__(self, position):
        super().__init__(position)
        self.direction = random.choice([1, -1])
        if self.direction == 1:
            self.seth(0)
        else:
            self.seth(180)

    def move(self):
        if self.ycor() > 250:
            self.seth(180)
        elif self.ycor() < -250:
            self.seth(0)
        self.forward(20)

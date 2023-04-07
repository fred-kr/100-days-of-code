from turtle import Screen, Turtle
import random


class Scene:
    def __init__(self):
        self.screen = Screen()
        self.food = Turtle(shape="circle")
        self.score = 0

    def screen_setup(self):
        """Set up the screen for the game."""
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Eater")
        self.screen.exitonclick()
        return self.screen

    def spawn_food(self, snake_pos):
        self.food.color("red")
        self.food.penup()

        while True:
            x = random.choice(range(-280, 280, 20))
            y = random.choice(range(-280, 280, 20))
            if (x, y) not in snake_pos:
                break

        self.food.goto(x, y)

    def remove_food(self):
        self.food.hideturtle()

    def update_score(self):
        self.score += 1
        self.screen.title(f"Snake Eater - Score: {self.score}")

    def game_over(self):
        self.screen.title(f"Snake Eater - Game Over {self.score}")
        self.screen.exitonclick()

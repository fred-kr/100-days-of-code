import random
from turtle import Turtle, _Screen


class Scene:
    def __init__(self):
        self.score = 0

    def screen_setup(self, screen, title):
        """Set up the screen for the game."""
        if isinstance(screen, _Screen):
            screen.setup(width=600, height=600)
            screen.bgcolor("black")
            screen.title(title)
            screen.listen()
            new_screen = screen
            return new_screen

        else:
            raise TypeError("screen must be a Screen object")

    def spawn_food(self, snake_pos):
        food = Turtle(shape="circle", visible=False)
        food.speed("fastest")
        food.color("red")
        food.penup()

        while True:
            x = random.choice(range(-280, 280, 20))
            y = random.choice(range(-280, 280, 20))
            if (x, y) not in snake_pos:
                break

        food.goto(x, y)
        food.showturtle()
        return food

    def remove_food(self, food):
        food.hideturtle()

    def update_score(self, screen):
        self.score += 1
        screen.title(f"Snake Eater - Score: {self.score}")

    def game_over(self, screen):
        screen.title(f"Snake Eater - Game Over {self.score}")

        screen.ontimer(screen.bye, 2000)

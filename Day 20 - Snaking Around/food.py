import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, snake_pos: list) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh(snake_pos)

    def refresh(self, snake_pos: list) -> None:
        """
        Move food to a random location on the screen that is not occupied by the snake.

        Args:
            snake_pos (list): List of tuples containing the positions of the snake segments.
        """
        while True:
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            if (random_x, random_y) not in snake_pos:
                break

        self.goto(random_x, random_y)

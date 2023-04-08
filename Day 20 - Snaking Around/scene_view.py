# from turtle import Screen, Turtle, _Screen


# class Scene(_Screen):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.delay = 0.1
#         self.screen = Screen()
#         self.screen_setup()

#     def screen_setup(self):
#         self.screen.setup(width=600, height=600)
#         self.screen.bgcolor("black")
#         self.screen.title("Snake Game")
#         self.screen.listen()
#         self.screen.tracer(0)

#     # def move_food(self, food, snake_pos):
#     #     while True:
#     #         x = random.choice(range(-280, 280, 20))
#     #         y = random.choice(range(-280, 280, 20))
#     #         if (x, y) not in snake_pos:
#     #             break

#     #     food.goto(x, y)

#     def update_score(self):
#         self.score += 1
#         self.screen.title(f"Snake Eater - Score: {self.score}")

#     def game_over(self):
#         self.screen.resetscreen()
#         self.screen.title("Snake Eater - Game Over")
#         self.screen.bgcolor("black")
#         scoreboard = Turtle(visible=False)
#         scoreboard.color("white")
#         scoreboard.penup()
#         scoreboard.write(
#             f"Game Over! Your score was {self.score}.",
#             align="center",
#             font=("Courier", 24, "normal"),
#         )

import time
from turtle import Screen, Turtle, _Screen

from food import Food
from scoreboard import Scoreboard
from snake_body import Snake

DELAY = 0.1
STARTER_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()
border = Turtle(visible=False)
border.penup()
border.goto(-300, 275)
border.pencolor("white")
border.pendown()
border.goto(300, 275)

snake_player: Snake = Snake(STARTER_POSITIONS)
food = Food(STARTER_POSITIONS)

screen.onkey(snake_player.up, "w")
screen.onkey(snake_player.down, "s")
screen.onkey(snake_player.left, "a")
screen.onkey(snake_player.right, "d")


def game_over(screen: _Screen, snake_player: Snake) -> None:
    snake_player.is_alive = False
    for turtle in screen.turtles():
        turtle.hideturtle()


# Main game loop
while snake_player.is_alive:
    screen.update()
    # Exit loop if snake hits wall
    if not (-290 < snake_player.head.xcor() < 290) or not (-305 < snake_player.head.ycor() < 255):
        scoreboard.game_over()
        game_over(screen, snake_player)
        break
    else:
        snake_player.move()

    # Exit loop if snake hits tail
    if any(
        snake_player.head.distance(segment) < 10
        for segment in snake_player.get_segment_positions()[1:]
    ):
        scoreboard.game_over()
        game_over(screen, snake_player)
        break
    else:
        # Handle collision with food
        if snake_player.head.distance(food) < 15:
            food.refresh(snake_player.get_segment_positions())
            snake_player.add_segment()
            scoreboard.increase_score()

    time.sleep(DELAY)

screen.exitonclick()

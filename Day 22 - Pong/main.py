import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player = Paddle((-480, 0))
computer = Paddle((480, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(computer.move_up, "Up")
screen.onkey(computer.move_down, "Down")

active = True

screen.listen()

while active:
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(player) < 50 or ball.distance(computer) < 50) and not ball.colliding:
        ball.bounce_x()
        ball.colliding = True
    elif ball.distance(player) >= 50 and ball.distance(computer) >= 50:
        ball.colliding = False

    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        active = False
        scoreboard.game_over()

    ball.move()
    ball.get_speed()

    time.sleep(ball.move_speed)

screen.exitonclick()

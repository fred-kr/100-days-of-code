# Day 20
# [x] 1. Create a snake body that is 3 squares long.
# [x] 2. Move the snake.
# [x] 3. Control the snake.

# Day 21
# [x] 4. Detect collision with food.
# [ ] 5. Create a scoreboard.
# [ ] 6. Detect collision with wall.
# [ ] 7. Detect collision with tail.
from turtle import Turtle, Screen
from snake_body import Snake
from scene_view import Scene
import random

play_area = Scene().screen_setup()
# play_area.screen_setup()

snake_player = Snake([(0, 0), (-20, 0), (-40, 0)])

play_area.spawn_food(snake_player.get_segment_positions()) # type: ignore

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake Eater")

# snek = Snake([(0, 0), (-20, 0), (-40, 0)])

# # 30x30 grid of 20x20 squares
# all_spawn_positions = []
# for x in range(-280, 280, 20):
#     for y in range(-280, 280, 20):
#         all_spawn_positions.append((x, y))
# # set to allow for easy removal of occupied positions
# all_spawns = set(all_spawn_positions)

# # Get all squares that are occupied by the snake
# def get_current_snake_positions():
#     snake_positions = []
#     for segment in snek.segments:
#         snake_positions.append((segment.xcor(), segment.ycor()))
#     snake_set = set(snake_positions)
#     return snake_set

# # Get all squares that are not occupied by the snake
# def get_current_viable_spawns():
#     return all_spawns - get_current_snake_positions()

# # Create new apple object
# def new_apple():
#     apple = Turtle(shape="circle")
#     apple.color("red")
#     apple.penup()
#     return apple

# # Place apple in random available spawn
# def set_apple_position(available_spawns):
#     apple.goto(random.choice(list(available_spawns)))

# Remove apple from screen and add new segment to snake
# def eat_apple():
#     apple.hideturtle()
#     snek.add_segment()

# play_area.onkey(snake_player.up, "w")
# play_area.onkey(snake_player.down, "s")
# play_area.onkey(snake_player.left, "a")
# play_area.onkey(snake_player.right, "d")

# while snek.is_alive:
#     screen.listen()

#     # Exit loop if snake hits wall
#     if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
#         snek.is_alive = False
#         # snek.hide()
#         break
#     else:
#         snek.move()
        
#     # On collision with apple, call eat_apple()
#     if snek.head.distance(apple) < 10:
#         eat_apple()
        
        
# play_area.exitonclick()

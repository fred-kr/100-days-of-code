# Day 20
# [x] 1. Create a snake body that is 3 squares long.
# [x] 2. Move the snake.
# [x] 3. Control the snake.

# Day 21
# [x] 4. Detect collision with food.
# [ ] 5. Create a scoreboard.
# [x] 6. Detect collision with wall.
# [x] 7. Detect collision with tail.

from turtle import Screen, Turtle  # noqa: F401

from scene_view import Scene
from snake_body import Snake  # noqa: F401

game = Scene()
screen = Screen()

snake_player = Snake([(0, 0), (-20, 0), (-40, 0)])

game_view = game.screen_setup(screen, "Snake Eater")
food = game.spawn_food(snake_player.get_segment_positions())

game_view.onkey(snake_player.up, "w")
game_view.onkey(snake_player.down, "s")
game_view.onkey(snake_player.left, "a")
game_view.onkey(snake_player.right, "d")

while snake_player.is_alive:
    # Exit loop if snake hits wall
    if snake_player.head.xcor() in (-300, 300) or snake_player.head.ycor() in (-300, 300):
        snake_player.is_alive = False
        game.game_over(game_view)
        break
    else:
        snake_player.move()

    # Exit loop if snake hits tail
    for segment in snake_player.get_segment_positions()[1:]:
        if snake_player.head.distance(segment) < 10:
            snake_player.is_alive = False
            game.game_over(game_view)
            break
    else:
        # Handle collision with food
        if snake_player.head.distance(food) < 10:
            game.remove_food(food)
            snake_player.add_segment()
            game.update_score(game_view)
            food = game.spawn_food(snake_player.get_segment_positions())

game_view.exitonclick()

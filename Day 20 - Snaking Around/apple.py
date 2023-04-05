from turtle import Turtle
import random

class Apple:
    def __init__(self):
        pass
        
    def get_viable_spawn_locations(self, occupied_locations):
        viable_spawns = []
        for x in range(-280, 280, 20):
            for y in range(-280, 280, 20):
                viable_spawns.append((x, y))
        for segment in occupied_locations:
            if (segment.xcor(), segment.ycor()) in viable_spawns:
                viable_spawns.remove((segment.xcor(), segment.ycor()))
        return viable_spawns
    
    def spawn(self, occupied_locations):
        self.apple = Turtle(shape="circle")
        self.apple.color("red")
        self.apple.penup()
        self.apple.goto(random.choice(self.get_viable_spawn_locations(occupied_locations)))
        return self.apple
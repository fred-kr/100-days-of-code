# from turtle import Turtle, Screen
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("HP", [100, 100, 100])
table.align = "l"


print(table)

# turner = Turtle()
# my_screen = Screen()

# turner.shape("turtle")
# turner.color("red")
# turner.forward(100)

# my_screen.exitonclick()

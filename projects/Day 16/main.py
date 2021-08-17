# from another_module import another_variable
# print(another_variable)

# from turtle import Turtle, Screen
# buddy = Turtle() # creating class object
# print(buddy)
# buddy.shape("turtle") # calling class methods
# buddy.color("blue")
# buddy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight) # getting class attribute
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

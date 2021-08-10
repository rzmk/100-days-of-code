from turtle import Turtle, Screen
import random

# Game settings
is_race_on = False
screen = Screen()
screen.title("The Great Turtle Race!")
screen.setup(width=500, height=400)

# Get user guess
user_selection = ""
while not user_selection:
    user_selection = screen.textinput(title="Who will win?", prompt="Which turtle will win the race?\nType blue, green, red, orange, turquoise, or purple.\nEnter a color: ")

# Setup turtle objects after input
colors = ["blue", "green", "turquoise", "orange", "red", "purple"]
turtles = [Turtle(shape="turtle") for turtle in range(6)]
for i in range(6):
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=-100+(i*40))

# Start race!
result = Turtle()
result.penup()
result.hideturtle()
result.goto(x=0, y=100)
is_race_on = True
while is_race_on:
    for turtle in turtles:
        # Move turtle forward a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        # Check if a turtle won the race
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_selection:
                result.write(f"You've won! The {winning_color} turtle is the winner!", align="center", font=("Open Sans", 16, "normal"))
            else:
                result.write(f"You've lost! The {winning_color} turtle is the winner!", align="center", font=("Open Sans", 16, "normal"))

screen.exitonclick()
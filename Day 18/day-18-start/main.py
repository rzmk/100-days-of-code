from turtle import Turtle, Screen, colormode
from random import randint, choice

arrow = Turtle()

# Draw a square
def square():
    for i in range(4):
        arrow.forward(100)
        arrow.right(90)

# square()

# Draw a dashed line
def dashed_line():
    for i in range(20):
        arrow.forward(10)
        arrow.penup()
        arrow.forward(10)
        arrow.pendown()

# dashed_line()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
def polygons():
    colormode(255)
    for i in range(3, 11):
        angle = 360 / i
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        arrow.color(color)
        for j in range(1, i + 1):
            arrow.right(angle)
            arrow.forward(100)

# polygons()

# Random Walk (thickness, speed up turtle)
def random_walk(steps):
    colormode(255)
    arrow.pensize(15)
    arrow.speed(0)
    for i in range(steps):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        arrow.color(color)
        step_size = randint(0, 50)
        arrow.setheading(choice([0, 90, 180, 270]))
        arrow.forward(step_size)

# random_walk(1000)

# Spirograph
def spirograph():
    colormode(255)
    arrow.speed(0)
    heading = 0
    for i in range(72):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        arrow.color(color)
        arrow.circle(200)
        arrow.setheading(heading)
        heading += 5

# spirograph()

screen = Screen()
screen.exitonclick()

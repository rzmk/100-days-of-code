# # Get color palette from an image
# import colorgram

# color_list = []
# colors = colorgram.extract('colors_source.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)

from turtle import Turtle, Screen, colormode
import random

arrow = Turtle()

color_list = [
    (221, 144, 96),
    (165, 57, 88),
    (68, 84, 153),
    (100, 167, 208),
    (154, 66, 54),
    (109, 176, 128),
    (195, 76, 113),
    (209, 123, 155),
    (222, 90, 66),
    (233, 163, 188),
    (238, 223, 97),
    (107, 117, 187),
    (176, 184, 224),
    (141, 210, 221),
    (84, 95, 88),
    (163, 139, 49),
    (58, 173, 186),
    (67, 54, 96),
    (234, 171, 155),
    (166, 206, 188),
    (154, 35, 49),
    (91, 159, 124),
    (189, 27, 24),
    (65, 55, 64),
    (56, 49, 71),
    (71, 56, 49),
]

# Set arrow starting position
arrow.hideturtle()
arrow.speed(0)
arrow.penup()
arrow.sety(-250)
arrow.setx(-250)
arrow.width(20)

# Create dots
colormode(255)
number_of_dots = 100
for i in range(1, number_of_dots + 1):
    arrow.pendown()
    arrow.dot(20, random.choice(color_list))
    arrow.penup()
    arrow.forward(50)
    if i % 10 == 0:
        arrow.penup()
        arrow.backward(500)
        arrow.left(90)
        arrow.forward(50)
        arrow.right(90)

screen = Screen()
screen.exitonclick()

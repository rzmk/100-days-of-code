from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()

def move_forwards():
    arrow.forward(10)

def move_backwards():
    arrow.backward(10)

def clockwise():
    arrow.right(10)

def counter_clockwise():
    arrow.left(10)

def clear_drawing():
    arrow.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards) # higher order function
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
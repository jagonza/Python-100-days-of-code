import colorgram
from turtle import Turtle, Screen
import random

# Extract 6 colors from an image.
image_colors = colorgram.extract('image.jpg', 20)

colors = []
for image_color in image_colors:
    color = (image_color.rgb.r, image_color.rgb.g, image_color.rgb.b)
    colors.append(color)

screen = Screen()
screen.setup(650, 650)
screen.colormode(255)
screen.bgcolor((56, 40, 40))

painter = Turtle()
painter.hideturtle()
painter.speed("fastest")
painter.penup()
painter.goto(-225, -225)


def paint_row():
    for _ in range(10):
        # painter.pendown()
        painter.dot(20, random.choice(colors))
        # painter.penup()
        painter.forward(50)


def move_to_next_line():
    painter.backward(500)
    painter.left(90)
    painter.forward(50)
    painter.right(90)


def paint():
    for _ in range(10):
        paint_row()
        move_to_next_line()


paint()

screen.exitonclick()

import random
from turtle import Turtle, Screen

my_turtle = Turtle()

## SQUARE ##
# my_turtle.begin_fill()
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)

## DASHED LINE ##
# for _ in range(15):
#     my_turtle.pendown()
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)

## PLIGONS ##
# COLORS = ["red", "pink", "blue", "yellow", "orange", "purple"]
# TOTAL_ANGLE = 360

# my_turtle.width(2)

# def draw_poligon(sides):
#     for _ in range(sides):
#         my_turtle.forward(100)
#         my_turtle.right(TOTAL_ANGLE / sides)


# for idx, sides in enumerate([3, 4, 5, 6, 8, 10]):
#     my_turtle.color(COLORS[idx])
#     draw_poligon(sides)


## RANDOM WALK ##
my_screen = Screen()
my_screen.colormode(255)

ANGLES = [-270, -180, -90, 0, 90, 180, 270]
DIRECTION = [0, 1]

my_turtle.speed(10)
my_turtle.width(10)

while True:
    my_turtle.forward(25)
    my_turtle.pencolor(random.choice(range(256)),
                       random.choice(range(256)),
                       random.choice(range(256)))
    direction = random.choice(DIRECTION)
    if direction == 0:
        my_turtle.left(random.choice(ANGLES))
    else:
        my_turtle.right(random.choice(ANGLES))


my_screen.exitonclick()

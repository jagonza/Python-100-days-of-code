import random
from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.setheading(180)
        self.shapesize(1, random.uniform(0.5, 4.0))
        self.setposition(random.uniform(420, 450), random.uniform(-250, 200))
        self.color(self.get_random_color())

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def move(self):
        self.forward(10)

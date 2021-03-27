import random
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self, dir):
        if dir == "up":
            self.forward(10)
        elif dir == "down":
            self.forward(-10)

    def is_at_finish_line(self):
        return self.ycor() == 250

    def reset_position(self):
        self.setposition(0, -280)

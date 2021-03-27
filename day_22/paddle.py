from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.setposition(position)

    def move(self, direction):
        if direction == "up":
            new_y = self.ycor() + 20 if self.ycor() + 20 < 250 else 250
            self.goto(self.xcor(), new_y)
        elif direction == "down":
            new_y = self.ycor() - 20 if self.ycor() - 20 > -250 else -250
            self.goto(self.xcor(), new_y)

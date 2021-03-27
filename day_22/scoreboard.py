from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position=(0, 0)):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(position)
        self.write(f'{self.points}', font=(
            'Courier New', 80, 'bold'), align='center')

    def add_point(self):
        self.clear()
        self.points += 1
        self.write(f'{self.points}', font=(
            'Courier New', 80, 'bold'), align='center')

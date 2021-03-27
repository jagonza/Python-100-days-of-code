from turtle import Turtle

FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-330, 260)
        self.write(f"LEVEL {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("G A M E  O V E R", align="center", font=FONT)

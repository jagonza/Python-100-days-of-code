from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.score = 0
        self.goto(0, 280)
        self.hideturtle()
        self.color('white')
        self.write(f'Score: {self.score}', font=(
            'Courier', 20), align='center')

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', font=(
            'Courier', 20), align='center')

    def game_over(self):
        self.goto(0, 0)
        self.write('GAMAME OVER', font=(
            'Courier', 40), align='center')

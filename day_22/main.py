from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_score = Scoreboard((50, 200))
left_score = Scoreboard((-50, 200))

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
middle_line = Turtle()
middle_line.penup()
middle_line.hideturtle()
middle_line.setheading(270)
middle_line.color("white")
middle_line.pensize(5)
middle_line.goto(0, 300)
for _ in range(50):
    middle_line.pendown()
    middle_line.forward(20)
    middle_line.penup()
    middle_line.forward(20)

ball = Ball()

screen.onkey(lambda: right_paddle.move("up"), "Up")
screen.onkey(lambda: right_paddle.move("down"), "Down")
screen.onkey(lambda: left_paddle.move("up"), "w")
screen.onkey(lambda: left_paddle.move("down"), "s")
screen.listen()


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 325)
            or (ball.distance(left_paddle) < 50 and ball.xcor() > -329)):
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        left_score.add_point()
    elif ball.xcor() < -400:
        ball.reset_position()
        right_score.add_point()

    screen.update()


screen.exitonclick()

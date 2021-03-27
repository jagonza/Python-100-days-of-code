import time
import random
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def config_screen():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("snake game")
    screen.tracer(0)
    screen.update()

    set_listeners()


def set_listeners():
    screen.onkey(lambda: snake.change_direction("up"), "Up")
    screen.onkey(lambda: snake.change_direction("down"), "Down")
    screen.onkey(lambda: snake.change_direction("left"), "Left")
    screen.onkey(lambda: snake.change_direction("right"), "Right")
    screen.listen()


screen = Screen()
config_screen()

scoreboard = Scoreboard()
snake = Snake()
food = Food()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    snake.move()

    distance = snake.head.distance(food)
    if distance < 15:
        scoreboard.add_point()
        snake.extend()
        food.refresh()

    if (snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if segment and snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

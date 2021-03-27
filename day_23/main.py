import time
from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title = "The Turtle Crossing Capstone"
screen.colormode(255)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.onkey(lambda: player.move("up"), "Up")
screen.onkey(lambda: player.move("down"), "Down")
screen.listen()

is_game_on = True


def move_cars():
    for car in cars:
        car.move()


def check_for_collision():
    global is_game_on
    for car in cars:
        if (is_game_on and (player.distance(car) < 20)):
            is_game_on = False
            scoreboard.game_over()


cars = []
iteration = 0
while is_game_on:
    FACTOR = 1 / scoreboard.level

    time.sleep(0.1 * FACTOR)

    if iteration % int(10 * FACTOR) == 0:
        cars.append(Car())

    move_cars()
    check_for_collision()
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.level_up()

    screen.update()

    iteration += 1


screen.exitonclick()

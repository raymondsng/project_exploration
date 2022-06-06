import time
from turtle import Screen, Turtle
import random

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FONT = ("Courier", 18, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

character = Player()
level = Scoreboard()
cars = []
loop = 0

game_is_on = True
while game_is_on:
    loop += 1
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:
        cars.append(CarManager())
    for _ in cars:
        _.scroll()
        if _.distance(character) < 20:
            message = Turtle()
            message.penup()
            message.write("Game Over!", align="center", font=FONT)
            game_is_on = False

    screen.listen()
    screen.onkeypress(fun=character.movement_up, key="w")
    screen.onkeypress(fun=character.movement_down, key="s")
    screen.onkeypress(fun=character.reset_position, key="r")

    # Turtle has reached top of screen
    if character.ycor() >= player.FINISH_LINE_Y:
        level.level_advancement()
        character.reset_position()
        for _ in cars:
            _.hideturtle()
        cars = []
        CarManager.increment()


Screen().exitonclick()


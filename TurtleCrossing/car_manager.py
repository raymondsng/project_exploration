from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.movement = STARTING_MOVE_DISTANCE
        super().__init__()
        self.penup()
        # Randomly spawn
        self.goto(300, randint(-250, 250))
        self.shape("square")
        # Randomly generate color
        self.color(COLORS[randint(0, len(COLORS) - 1)])
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.scroll()

    def scroll(self):
        self.forward(self.movement)

    @staticmethod
    def increment():
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

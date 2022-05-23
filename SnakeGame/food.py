import turtle
import random

SCREEN_DIMENSION = (560, 560)


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.location = (random.randint(int(-SCREEN_DIMENSION[0]/2), int(SCREEN_DIMENSION[0]/2)),
                         random.randint(int(-SCREEN_DIMENSION[1]/2), int(SCREEN_DIMENSION[1]/2)))
        self.speed(0)
        self.penup()
        self.goto(self.location)
        self.color("blue")
        self.shapesize(0.5, 0.5, 1)

    def spawn(self):
        self.location = (random.randint(int(-SCREEN_DIMENSION[0] / 2), int(SCREEN_DIMENSION[0] / 2)),
                         random.randint(int(-SCREEN_DIMENSION[1] / 2), int(SCREEN_DIMENSION[1] / 2)))
        self.goto(self.location)

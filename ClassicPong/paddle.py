import turtle
from turtle import Turtle

UP, DOWN, MOVEMENT_DISTANCE = 90, 270, 20
SCREEN_BORDER = 300

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1, 1)
        self.spawn_loc(position)

    def spawn_loc(self, position):
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() <= SCREEN_BORDER - 55:
            y_pos = self.ycor() + 20
            self.goto(self.xcor(), y_pos)

    def down(self):
        if self.ycor() >= -SCREEN_BORDER + 70:
            y_pos = self.ycor() - 20
            self.goto(self.xcor(), y_pos)
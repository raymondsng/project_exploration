from turtle import Turtle

class Ball(Turtle):

    def __init__(self, angle):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.setheading(angle)

    def go_forward(self):
        self.forward(5)

    def deflect(self):
        self.setheading(self.heading() + 90)
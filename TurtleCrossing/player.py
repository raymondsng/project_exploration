from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        # Faces up
        self.setheading(90)

    def movement_up(self):
        self.forward(MOVE_DISTANCE)

    def movement_down(self):
        self.backward(MOVE_DISTANCE)

    def reset_position(self):
        # For resetting after level clearance
        self.goto(STARTING_POSITION)

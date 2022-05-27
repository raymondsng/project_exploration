from turtle import Turtle

ALIGNMENT, FONT = "center", ("Courier", 20, "normal")

class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"{self.left_score} <- Score -> {self.right_score}", align=ALIGNMENT, font=FONT)

    def left_increment(self):
        self.left_score += 1
        self.clear()
        self.write(f"{self.left_score} <- Score -> {self.right_score}", align=ALIGNMENT, font=FONT)

    def right_increment(self):
        self.right_score += 1
        self.clear()
        self.write(f"{self.left_score} <- Score -> {self.right_score}", align=ALIGNMENT, font=FONT)

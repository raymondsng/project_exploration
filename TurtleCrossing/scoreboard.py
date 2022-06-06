from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230, 270)
        self.level = 1
        self.hideturtle()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_advancement(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_loop(self):
        return self.level




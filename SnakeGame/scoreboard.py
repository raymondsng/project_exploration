import turtle

ALIGNMENT, FONT = "center", ("Courier", 20, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        # Default move value is False which prevents the text from moving
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def end_game(self):
        message = turtle.Turtle()
        message.hideturtle()
        message.penup()
        message.goto(0, 0)
        message.color("blue")
        message.write("GAME OVER", align=ALIGNMENT, font=FONT)

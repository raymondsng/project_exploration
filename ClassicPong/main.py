import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from field import Field
from ball import Ball
import time

DRAW_DIST, SCREEN_HEIGHT = 20, 600
ALIGNMENT, FONT = "center", ("Courier", 14, "normal")
RIGHT_TILT, LEFT_TILT = 45, 225
# Screen creation
screen = Screen()
screen.title("Pong Program")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)
paddle1 = Paddle((-380, -100))
paddle2 = Paddle((370, 100))
ball = Ball(RIGHT_TILT)
scoreboard = Field()
operation = True

# Middle border creation
drawer = Turtle(shape="square")
drawer.hideturtle()
drawer.pencolor("white")
drawer.pensize(5)
drawer.penup()
drawer.goto(0, 280)
drawer.setheading(270)
for _ in range(SCREEN_HEIGHT//DRAW_DIST * 2):
    drawer.pendown()
    drawer.forward(DRAW_DIST)
    drawer.penup()
    drawer.forward(DRAW_DIST)

# Game logic
while operation:
    screen.update()
    ball.go_forward()

    # Paddle movement
    screen.listen()
    screen.onkeypress(fun=paddle1.up, key="w")
    screen.onkeypress(fun=paddle1.down, key="s")
    screen.onkeypress(fun=paddle2.up, key="Up")
    screen.onkeypress(fun=paddle2.down, key="Down")

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280 or ball.distance(paddle1) < 20 or ball.distance(paddle2) < 5:
        ball.deflect()

    # Paddle collision
    if (ball.xcor() > 360 and ball.distance(paddle2) < 50) or (ball.xcor() < -360 and ball.distance(paddle1) < 50):
        ball.deflect()

    # Update scoreboard
    if ball.xcor() < -400:
        scoreboard.right_increment()
        ball.reset()
        paddle1.reset()
        paddle2.reset()
        paddle1 = Paddle((-380, -100))
        paddle2 = Paddle((370, 100))
        ball = Ball(LEFT_TILT)
        continue
    elif ball.xcor() > 400:
        scoreboard.left_increment()
        ball.reset()
        paddle1.reset()
        paddle2.reset()
        paddle1 = Paddle((-380, -100))
        paddle2 = Paddle((370, 100))
        ball = Ball(RIGHT_TILT)

        continue

    # End of game logic
    if scoreboard.left_score == 3:
        drawer.penup()
        drawer.goto(-200, 0)
        drawer.write("YOU WIN", align=ALIGNMENT, font=FONT)
        drawer.goto(200, 0)
        drawer.write("YOU LOSE", align=ALIGNMENT, font=FONT)
        operation = False
    elif scoreboard.right_score == 3:
        drawer.penup()
        drawer.goto(-200, 0)
        drawer.write("YOU LOSE", align=ALIGNMENT, font=FONT)
        drawer.goto(200, 0)
        drawer.write("YOU WIN", align=ALIGNMENT, font=FONT)
        operation = False

screen.exitonclick()
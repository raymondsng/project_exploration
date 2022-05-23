import turtle
from turtle import Turtle


default_pos = [(0, 0), (-20, 0), (-40, 0)]
red = True
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:

    def __init__(self):
        self.snake_bits = []
        self.create_snake()
        self.head = self.snake_bits[0]

    def create_snake(self):
        global red
        for position in default_pos:
            snake = Turtle(shape="square")
            if red:
                snake.color("red")
                red = False
            else:
                snake.color("green")
                red = True
            snake.penup()
            snake.goto(position)
            self.snake_bits.append(snake)

    def turn_right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def turn_up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def increment(self):
        global red
        snake = Turtle(shape="square")
        if red:
            snake.color("red")
            red = False
        else:
            snake.color("green")
            red = True
        snake.penup()
        snake.goto(self.snake_bits[-1].pos())
        self.snake_bits.append(snake)

    def move(self):
        for num in range(len(self.snake_bits) - 1, 0, -1):
            position = self.snake_bits[num - 1].pos()
            self.snake_bits[num].goto(position)
        self.snake_bits[0].forward(20)
        turtle.listen()
        turtle.onkeypress(fun=self.turn_left, key="Left")
        turtle.onkeypress(fun=self.turn_right, key="Right")
        turtle.onkeypress(fun=self.turn_up, key="Up")
        turtle.onkeypress(fun=self.turn_down, key="Down")
        turtle.onkeypress(fun=self.increment, key="s")

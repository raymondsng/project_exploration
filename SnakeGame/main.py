from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


s = Screen()
s.tracer(0)
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Program")
snake = Snake()
food = Food()
scoreboard = Scoreboard()

operation = True
LOWER_BORDER_LIMIT, UPPER_BORDER_LIMIT = -290, 290

while operation:
    s.update()
    time.sleep(0.07)
    snake.move()

    # Food logic
    if snake.head.distance(food.location) < 15:
        food.spawn()
        snake.increment()
        scoreboard.increment()

    # Wall logic
    if (snake.head.xcor() > UPPER_BORDER_LIMIT) or (snake.head.xcor() < LOWER_BORDER_LIMIT) \
            or (snake.head.ycor() > UPPER_BORDER_LIMIT) or (snake.head.ycor() < LOWER_BORDER_LIMIT):
        operation = False
        scoreboard.end_game()
        operation = "c" if s.textinput(title="Retry?", prompt="Press c to continue: ") == "c" else False
        s.clear()
        snake = Snake()
        food = Food()
        scoreboard = Scoreboard()
        scoreboard.color("black")

    # Tail collision logic
    for bit in snake.snake_bits[1:]:
        if snake.head.distance(bit) < 5:
            operation = False
            scoreboard.end_game()
            operation = "c" if s.textinput(title="Retry?", prompt="Press c to continue: ") == "c" else False
            s.clear()
            snake = Snake()
            food = Food()
            scoreboard = Scoreboard()
            scoreboard.color("black")


s.exitonclick()

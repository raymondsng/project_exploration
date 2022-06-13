import turtle
import pandas

# Data processing and game creation
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
# Adding shape to available shape inputs for turtle object
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
answer_gate = screen.textinput(title="Guess the State", prompt="Type a State!").title()
countries = data["state"].to_list()
guessed_countries = set()


# def pointer(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(pointer)

# Game logic, AND used instead of OR because we want 'Quit' to exit the program even without 50 states guessed.
while answer_gate != "Quit" and len(guessed_countries) != 50:
    if answer_gate in countries:
        guessed_countries.add(answer_gate)
        writer = turtle.Turtle()
        writer.speed(0)
        writer.hideturtle()
        writer.penup()
        writer.goto(int(data[data.state == answer_gate].x), int(data[data.state == answer_gate].y))
        writer.write(answer_gate)
    answer_gate = screen.textinput(title=f"{len(guessed_countries)}/50 - Guess the State", prompt="Type a State!").title()

screen.exitonclick()

# End of game logic - Generate a file with names of states that were not successfully guessed
entry = {"Countries not guessed": []}
for i in countries:
    if i in guessed_countries:
        countries.remove(i)
    else:
        entry["Countries not guessed"].append(i)
info = pandas.DataFrame(entry)
info.to_csv("States to learn.csv")



#Number Guessing Game Objectives:

# Include an ASCII art logo.

from art import logo
import random
print(logo)

answer = random.randint(1, 100)
lives = 0
print("Welcome to the Soju cap number simulator! Range of available values: 1 - 100 ")
difficulty = input("What difficulty do you want? Hard = 5 Tries, Normal = 10 Tries, Easy = No limit\nYour Choice (h/n/e): ")
if difficulty == "h":
    lives = 5
elif difficulty == "n":
    lives = 10
else:
    #Essentially unlimited in this context due to greater value than available guesses
    lives = 200

def gauge(guess, answer):
    global lives
    if guess > answer:
        lives -= 1
        print ("Too high")
    elif guess < answer:
        lives -= 1
        print("Too low")
    else:
        print("That is the right answer!")
    

guess = 0
while guess != answer:
    if lives > 100:
        print("You have unlimited attempt(s) to guess the correct number")
        guess = int(input("Pick a number: "))
        gauge(guess, answer)
    elif 0 < lives < 100:
        print(f"You have {lives} attempt(s) to guess the correct number")
        guess = int(input("Pick a number: "))
        gauge(guess, answer)
    else:
        print("Nobody guessed the right number in time! Everyone drinks!")
        break


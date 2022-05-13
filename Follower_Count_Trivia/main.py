from art import logo, vs
from game_data import data
import os
import random
print(logo)

right = True
score = 0
first = random.choice(data)
second = random.choice(data)

def choice(str):
    if str == "b":
        return second['follower_count'] > first['follower_count']
    else:
        return second['follower_count'] < first['follower_count']

while right:
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
    print(vs)
    print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}")
    decision = input("Select your option (a/b): ")
    os.system('clear')
    print(logo)
    if choice(decision):
        score += 1
        print(f"You are correct! Score: {score}")
        first = second
        second = random.choice(data)
    else:
        print(f"That was the wrong answer. Final Score: {score}")
        right = False
        

from art import logo
import random

player_score, computer_score = 0, 0
str1, str2 = "Player" , "Computer"

def replace(lst):
    result = lst.copy()
    result.remove(11)
    result.append(1)
    return result
            

def draw_card():
    global str1, str2
    while (len(your_hand["Player"]) < 5 and sum(your_hand["Player"]) < 21):
        draw = input("Will you draw a card? (y/n)\n")
        if draw == "y":
            first = cards[random.randint(0, len(cards) - 1)]
            your_hand["Player"].append(first)
            if (sum(your_hand["Player"]) > 21 and 11 in your_hand["Player"]):
                your_hand["Player"] = replace(your_hand["Player"])
                print("Aces in hand were converted to 1.")
            print(f"{first} was added to Player's hand. Current hand: {your_hand[str1]} Value: {sum(your_hand[str1])}\n")
        else:
            break

def winner_message(code):
    if code == 0:
        global player_score 
        player_score += 1
        print("You have won!")
    else:
        global computer_score
        computer_score += 1
        print("You lost!")
        

while True:
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_hand = {"Player" : []}
    com_hand = {"Computer" : []}
    for i in range(2):
        first = cards[random.randint(0, len(cards) - 1)]
        second = cards[random.randint(0, len(cards) - 1)]
        your_hand["Player"].append(first)
        print(f"{first} was added to Player's hand. Current hand: {your_hand[str1]} Value: {sum(your_hand[str1])}\n")
        com_hand["Computer"].append(second)
        print(f"{com_hand[str2][0]} is the only card you can see from the Opponent. Shown Value:{com_hand[str2][0]}\n")

    if sum(your_hand["Player"]) == 21:
        player_score += 2
        print("Congratulations, you got a BlackJack! Double Score!")
        print(f"Your score: {player_score}\nComputer score: {computer_score}\n------------------------------------------------------------------")
        continue
    elif sum(your_hand["Player"]) == 22:
        player_score += 3
        print("Congratulations, you got Pocket Rockets! Triple Score!")
        print(f"Your score: {player_score}\nComputer score: {computer_score}\n------------------------------------------------------------------")
        continue
    
    draw_card()

    #AI logic for computer competency in game
    if sum(com_hand["Computer"]) < 14:
        com_draw = cards[random.randint(0, len(cards) - 1)]
        com_hand["Computer"].append(com_draw)
    print(f"Computer's final hand: {com_hand[str2]} Final Value: {sum(com_hand[str2])}\n")

    if (sum(your_hand["Player"]) > 21 and sum(com_hand["Computer"]) > 21):
        print("Both of you busted! It's a draw!")
    elif sum(your_hand["Player"]) > 21:
        computer_score += 1
        print("You busted! It's your loss!")
    elif len(your_hand["Player"]) == 5:
        player_score += 2
        print("五龙, Double Score!")
    elif sum(com_hand["Computer"]) > 21:
        player_score += 1
        print("The dealer busted! It's your win!")
    elif sum(your_hand["Player"]) == sum(com_hand["Computer"]):
        print("It's a draw!")
    else:
        print(winner_message(0) if sum(your_hand["Player"]) > sum(com_hand["Computer"]) else winner_message(1))

    print(f"Your score: {player_score}\nComputer score: {computer_score}\n------------------------------------------------------------------")



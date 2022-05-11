from replit import clear
from art import logo
import random
#HINT: You can call clear() to clear the output in the console.
artifact = ["Jewel of Marzepan", "Eye of Horus", "General Kozai's Breastplate", "Yian Garuga's Carapace", "Meteor Sword"]

rarity = {"Jewel of Marzepan" : "Extremely rare", "Eye of Horus" : "One-of-a-kind", "General Kozai's Breastplate" : "One-of-a-kind", "Yian Garuga's Carapace": "Relatively common", "Meteor Sword" : "rare"}

field_day = True

all_bidders = {}

print(logo)
print("Welcome to the underground bidding system.")
for key in rarity:
    if "common" in rarity[key]:
        field_day = False

if field_day:
    print("It is your lucky day! Every item for auction is exquisitely rare today!")

alternative_bids = "yes"
item = random.choice(artifact)

while alternative_bids == "yes":
    
    name_entry = input("What is your name?: ")
    bid_amount = int(input(f"Welcome {name_entry}. How much are you willing to bid for the {item}?\n$ "))
    all_bidders[name_entry] = bid_amount
    alternative_bids = input(f"Are there any other contenders for this {rarity[item]} artifact? yes/no : ")
    if alternative_bids == "yes":
        clear()
#below max function iterates through all_bidders dictionary and applies function key to each iterated element which is the key of the entries. Hence it resolves to all_bidders.get(x) for x in all_bidders essentially
result_name = max(all_bidders, key = all_bidders.get) 
result_amt = max(all_bidders.values())
print(f"The winner of this round is {result_name} and the winning bid amount is ${result_amt}! Congratulations to the winner for obtaining the {item} once again :D")
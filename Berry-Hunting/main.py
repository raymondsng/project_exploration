print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Mirage Island.")
print("Your mission is to find a Leichi Berry.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
import random
import sys
water = ["Magikarp", "Goldeen", "Crawdaunt", "Dunsparce", "Mudkip", "Psyduck"]
party = ["Squirtle", "Charmander"]
fainted = []
caught, steps = 0 , 0

def battle():
  if len(party) == 0:
    return "No pokemon available... Game over!"
    sys.exit("Game over, try again")
  ally = party.pop()
  print(f"Ally {ally} has fainted")
  fainted.append(ally)

def completion():
  return f"You have found the coveted Leichi Berry! {len(fainted)} of your pokemon fainted on this journey. While on this journey, you caught a total of {caught} new pokemon and took a total of {steps} actions. . Good Job :)"

print(''' *    .  *       .             *
                         *
 *   .        *       .       .       *
   .     *
           .     .  *        *
       .                .        .
.  *           *                     *
                             .
         *          .   *''')
grass = input("You spot some rustling in the nearby bushes, will you investigate? Y/N\n").upper()
steps += 1
if grass == "Y":
  battle()
  print(f"You have won the battle, {len(party)} pokemon left\n" if len(party) > 0 else "You are ambused by a Houndour, Game over!")
else:
  print("You veered away from the source of the rustling.")

print('''
             .'`'.'`'.
         .''.`.  :  .`.''.
         '.    '. .'    .'
         .```  .' '.  ```.
         '..',`  :  `,'..'
              `-'`'-`''')

lake = input("You encountered a sparkling lake with a deep aquamarine hue, will you use your Fishing Rod? Y/N\n").upper()
steps += 1
if lake == "Y":
  pokemon = water[random.randint(0,len(water))]
  party.append(pokemon)
  caught += 1
  print (f"Congratulations! You just caught a {pokemon}! It joined the party. You went along the bank of the lake.")
else:
  print("You went along the bank of the lake.")

print('''_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|''')

crossroads = input("You arrived at a winding path that diverges into two, which path would you take? Left/Right\n").lower()
steps += 1
if crossroads == 'left':
  print(f"You advanced on the {crossroads} path, and discovered two exotic plants. Will you take from the yellow or the turquoise plant? Y/T\n")
  steps += 1
  decision = input().lower()
  if decision == "y":
    print(completion())
    sys.exit("Game completed!:D")
  else:
    print("The berry you took was actually a pineco in disguise! Upon touching it, it denoted itself via selfdestruct. You and your party suffered heavy injuries. Game over!")
    sys.exit("Game over, try again")
else:
  print(f"You advanced on the {crossroads} path, and came face to face with a angry Ursaring. You proceed to battle.")
  battle()

print('''  *    .  *       .             *
                         *
 *   .        *       .       .       *
   .     *
           .     .  *        *
       .                .        .
.  *           *                     *
                             .
         *          .   *

''')

final = input("Upon defeating the Ursaring, you noticed a tunnel that it was previously blocking. Will you enter the tunnel? Y/N\n").lower()
steps += 1

if final == 'y':
  print('''
            _/-\_
         .-`-:-:-`-.
        /-:-:-:-:-:-\\
        \:-:-:-:-:-:/
         |`       `|
         |         |
         `\       /'
           `-._.-' ''')
  print("You found a hidden stash of berries and walked closer to have a better look at them")
  print(completion())
else:
  print("You wandered on for days but failed to find your way out of the Mysterious Island, you eventually succumb to fatigue. Game over!")
  sys.exit("Game over, try again")






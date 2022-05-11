import os
import sys
from importlib import reload
import importlib
import random

POKEMON_LIST = {0:('Blaziken',32,35,27),1:('Weedle',12,10,7),2:('Treecko',23,17,12),3:('Nidoking',34,30,28)}

class Pokemon(object):
    def __init__(self,details):
        self.name = details[0]
        self.exp = 0
        self.required_exp = 64
        self.experience = details[1]
        self.level = 1
        self.hp = details[2]
        self.atk = details[3]
        
    def attack(self,enemy):
        print(f'{self.name} attacked {enemy.name}!')
        enemy.hp -= self.atk
        if enemy.hp<=0:
            print(f'Foe {enemy.name} has fainted!')
            self.get_exp(enemy.experience)

        
      
    def get_exp(self,exp):
        self.exp += exp
        if self.exp > self.required_exp:
            self.level += 1
            print(f'{self.name} levelled up to level {self.level}')
            self.required_exp *= 1.5
        else:
            return f'{self.name} does not have enough experience to level up!'

class Trainer():
    def __init__(self,name):
        self.pokemon = []
        self.name = name
    def get_pokemon_names(self):
        return list(map(lambda x:x.name, self.pokemon))
    def get_name(self):
        return self.name

    
    

print('1 - New Game\n2 - Continue')
game_choice = input('What will you do? : ')
while game_choice != '1':
    if game_choice == '2':
        print('No save file available, please start a New Game')
        game_choice = input('What will you do? : ')
    else:
        print('Error! Choose a valid game choice!')
        game_choice = input('What will you do? : ')
    
print('Hello there! Welcome to the world of Pokemon! My name is Oak!\n'
      'People refer affectionately to me as Professor Oak.\n'
      'This world is inhabited by creatures called Pokemon!\n'
      'For some people, Pokemon are pets. Others use them for fights.\n'
      'Myself... I study Pokemon as a profession.')
name = input('First, what is your name? : ')
you = Trainer(name)
print(f'Right! So your name is {name},This is my grandson.\nHe\'s been your rival since you were a baby.')
rival = input('... Erm, what was his name again?: ')
print(f'That\'s right! I remember now! His name is {rival}!\n{name}! Your very own Pokemon legend is about to unfold!\nA world of dreams and adventures with MISSINGNO awaits!\nLet\'s go!')
print('1-Bulbasaur,2-Squirtle,3-Charmander')
starter = input('Which Pokemon would you like?: ')
if starter == '1':
    print('You got a Bulbasaur!')
    Bulbasaur = Pokemon(('Bulbasaur',30,28,9))
    you.pokemon.append(Bulbasaur)
elif starter == '2':
    print('You got a Squirtle!')
    Squirtle = Pokemon(('Squirtle',30,25,13))
    you.pokemon.append(Squirtle)
elif starter == '3':
    print('You got a Charmander!')
    Charmander = Pokemon(('Charmander',30,23,14))
    you.pokemon.append(Charmander)
else:
    print('You have your own Pokemon? That\'s fine by me!')
correct_answer = ['johndoesmurph!','nicwentwcpytd!','nadbakemuffin!']
HM = input('Hidden Message: ')
while HM:
    try:
        a = list(map(lambda x:x[0:2][::-1] + x[4:6] + x[18:20] + x[16] + x[11:14] + x[6:9][::-1] + '!',HM.split()))
        break
    except IndexError:
        print('Not enough characters, password is at least 20 characters long')
        HM = input('Hidden Message: ')
        continue
    
#ojbghnhprfrsmuhdeodo inufcwdtyfhwcpdwtuen andhdbnifdgmufhdekak

if a == correct_answer:
    for i in a:
        print(i)
    print('Congratulations! You have unlocked a 5000-Year-Old Dungeon!\n'
          f'Team {name} can now access it')
        
while a != correct_answer:
    map(lambda x:print(x),a)
    print('Wrong password, please try again')
    HM = input('Hidden Message: ')
    a.clear()
    try:
        a = list(map(lambda x:x[0:2][::-1] + x[4:6] + x[18:20] + x[16] + x[11:14] + x[6:9][::-1] + '!',HM.split()))
    except IndexError:
        print('Not enough characters, password is at least 20 characters long')
        HM = input('Hidden Message: ')
        continue
    if a == correct_answer:
        for i in a:
            print(i)
        print('Congratulations! You have unlocked a 5000-Year-Old Dungeon!\n'
          f'Team {name} can now access it')
input('Press any key')
print('You have entered the dungeon, wild pokemon may now attack you. Stay safe Hero!')
print('up-North,down-South,left-West,right-East')
direction = input('Which direction will you move in? : ')
while direction == 'up':
    print('You moved North!')
    encounter = Pokemon(random.choice(POKEMON_LIST))
    print(f'A wild {encounter.name} appeared!')
    print('1 - Yes\n'
          '2 - No')
    fight = input('Will you fight? : ')
    while fight == '2':
        print('You ran away')
        fight = 0
        direction = 0
        direction = input('Which direction will you move in? : ')
    while fight == '1':
        you.pokemon[0].attack(encounter)
        if encounter.hp <=0:
            print(f'{you.pokemon[0].name} has defeated {encounter.name}!')
            fight = 0
            direction = 0
            direction = input('Which direction will you move in? : ')
        else:
            print('1 - Yes\n'
                  '2 - No')
            fight = input('Will you fight? : ')
while direction == 'right':
    print('You moved East!')
    encounter = Pokemon(random.choice(POKEMON_LIST))
    print(f'A wild {encounter.name} appeared!')
    print('1 - Yes\n'
          '2 - No')
    fight = input('Will you fight? : ')
    while fight == '2':
        print('You ran away')
        fight = 0
        direction = 0
        direction = input('Which direction will you move in? : ')
    while fight == '1':
        you.pokemon[0].attack(encounter)
        if encounter.hp <=0:
            print(f'{you.pokemon[0].name} has defeated {encounter.name}!')
            fight = 0
            direction = 0
            direction = input('Which direction will you move in? : ')
        else:
            print('1 - Yes\n'
                  '2 - No')
            fight = input('Will you fight? : ')
while direction == 'left':
    print('You moved West!')
    encounter = Pokemon(random.choice(POKEMON_LIST))
    print(f'A wild {encounter.name} appeared!')
    print('1 - Yes\n'
          '2 - No')
    fight = input('Will you fight? : ')
    while fight == '2':
        print('You ran away')
        fight = 0
        direction = 0
        direction = input('Which direction will you move in? : ')
    while fight == '1':
        you.pokemon[0].attack(encounter)
        if encounter.hp <=0:
            print(f'{you.pokemon[0].name} has defeated {encounter.name}!')
            fight = 0
            direction = 0
            direction = input('Which direction will you move in? : ')
        else:
            print('1 - Yes\n'
                  '2 - No')
            fight = input('Will you fight? : ')
while direction == 'down':
    print('You moved South!')
    encounter = Pokemon(random.choice(POKEMON_LIST))
    print(f'A wild {encounter.name} appeared!')
    print('1 - Yes\n'
          '2 - No')
    fight = input('Will you fight? : ')
    while fight == '2':
        print('You ran away')
        fight = 0
        direction = 0
        direction = input('Which direction will you move in? : ')
    while fight == '1':
        you.pokemon[0].attack(encounter)
        if encounter.hp <=0:
            print(f'{you.pokemon[0].name} has defeated {encounter.name}!')
            fight = 0
            direction = 0
            direction = input('Which direction will you move in? : ')
        else:
            print('1 - Yes\n'
                  '2 - No')
            fight = input('Will you fight? : ')
            

    


    

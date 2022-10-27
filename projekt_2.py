import random
from string import digits
from unicodedata import numeric

'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
''' 

# Program pozdraví uživatele a vypíše úvodní text

print("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")

# Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
number = random.sample(range(10), 4)
if number[0] != 0:
    random_number = str(number[0]) + str(number[1]) + str(number[2]) + str(number[3])

# Hráč hádá číslo. 
game = True

while game:
    player_number = input("Enter a number: ")
    print("------------------------------")
    
    # Program vyhodnotí tip uživatele.
    if player_number == random_number: 
        game = False
        print("Correct, you've guessed the right number.")

    # Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla. Pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
    elif len(player_number) != 4 or player_number.isdigit() == False:
        print("Your enter is not 4 digit number. Write only number. Enter again.")

    elif player_number[0] == "0":
        print("Your first number can't be 0.")

    elif len(player_number) != len(set(player_number)):
        print("You have to input 4 different digits.")    
    

    # Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows)
   


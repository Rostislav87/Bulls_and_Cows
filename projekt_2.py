'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
''' 
import random

random_number = "" 
number_of_attempts = 0

# Uvítání uživatele


def print_greetings():
    print("""
    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    -----------------------------------------------
    """)
  

# Počítačem náhodně vygenerovaná 4 unikátní čísla  


def generate_number():
    global random_number
    number = random.sample(range(10), 4)
    if number[0] != 0:
        for num in number:
            random_number += str(num)
    else:
        generate_number()    

# Uživatel hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla. Pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky


def play_game():
    global number_of_attempts, random_number
    print(random_number)  
    while True :
        player_number = input("Enter a number or 'q' for exit the game: ")
        print("-----------------------------------------------")
        if player_number == "q":
            break
        elif len(player_number) != 4 or not player_number.isdigit():
            print("Your input is not 4 digit number. Write only number. Enter again.")
            continue
        elif player_number[0] == "0":
            print("Your first number can't be 0.")
            continue
        elif len(player_number) != len(set(player_number)):
            print("You have to input 4 different digits.") 
            continue
        number_of_attempts += 1
        
        bull = 0
        cow = 0 
        for num, num2 in zip(random_number, player_number):
            if num2 in random_number:
                if num2 == num:
                    bull += 1
                else:
                    cow += 1
        if bull > 1:             
            print(f"Bulls: {bull}")
        else:
            print(f"Bull: {bull}")

        if cow > 1:             
            print(f"Cows: {cow}")
        else:
            print(f"Cow: {cow}")
            
        if bull == 4:
            print(f"Congratulations. That's a right number. You needed {number_of_attempts} attempts to win.")
            break

print_greetings()
generate_number()
play_game()
    
    


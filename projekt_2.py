'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
''' 
import random

# Uvítání uživatele


def uvitej_uzivatele():
    print("""
    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    -----------------------------------------------
    """)


def main():
    game = True
    hra(game)

# Počítačem náhodně vygenerovaná 4 unikátní čísla 


def hra(game):
    number = random.sample(range(10), 4)
    if number[0] != 0:
        random_number = str(number[0]) + str(number[1]) + str(number[2]) + str(number[3])
        print(random_number)


# Uživatel hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla. Pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky 
    while game:
        player_number = input("Enter a number: ")
        print("-----------------------------------------------")
        if len(player_number) != 4 or not player_number.isdigit():
            print("Your input is not 4 digit number. Write only number. Enter again.")
        elif player_number[0] == "0":
            print("Your first number can't be 0.")
        elif len(player_number) != len(set(player_number)):
            print("You have to input 4 different digits.") 
        
        # Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows)
        bull = 0
        cow = 0
        for num, num2 in zip(random_number, player_number):
            if num2 in random_number:
                if num2 == num:
                    bull += 1
                else:
                    cow += 1            
        print(f"Bulls: {bull} Cows: {cow}")   
        if bull == 4:
            game = False
            print("Congratulations. That's a right number. You won!")



uvitej_uzivatele()
main()


    


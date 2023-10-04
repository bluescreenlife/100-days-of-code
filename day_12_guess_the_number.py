'''A simple number-guessing game with easy and hard modes.'''
import random
from replit import clear

art = '''
   ______                        ________            _   __                __ 
  / ____/_  _____  __________   /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/    / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )    / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/    /_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      
'''

def guess_the_number():
    print(art)

    number = random.randint(1, 100)
    guesses_remaining = 10

    difficulty_level = input("Try to guess the number, between 1 and 100.\nEnter difficulty level, easy or hard: ").lower()

    if difficulty_level == "hard":
        guesses_remaining = 5

    while guesses_remaining > 0:
        user_guess = int(input(f"\nYou have {guesses_remaining} guesses.\nGuess the number: "))
        if user_guess == number:
            print(f"\nYou win! The number was indeed {number}.")
            break
        elif user_guess < number:
            print("\nToo low. Try again.")
            guesses_remaining -= 1
        elif user_guess > number:
            print("\nToo high. Try again.")
            guesses_remaining -= 1
        else:
            print("\nUnknown error. Please try again.")
    
    if guesses_remaining == 0:
        print(f"\nOut of guesses! You lose.\nThe number was {number}.")

    if input("\nPlay again (Y/N)? ").upper() == "Y":
        clear()
        guess_the_number()
    else:
        print("\nSee you next time!")

if __name__ == "__main__":
    guess_the_number()
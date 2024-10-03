"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# IMPORTS
import random
import statistics

# LISTS
guesses_list = [] # 4. To store a list guesses per game.

# FUNCTION
def start_game():
    # 1. Welcome message
    print("WELCOME! I hope you enjoy the game!")
    #2. Created a random number to guess using randrange(): https://docs.python.org/3/library/random.html#functions-for-integers
    #2. Defined the range from 1 to 10. Noted that this function produces and int.
    random_number = random.randrange(1,10) 
    print(random_number) #DELETE - for testing purposes
    
    # 3. Set guess = 0 for initialization of the variable. The variable will be used to store the player's guess.
    # 3. Used a while loop to continuously prompt the play for a guess until the guess equals the random_number
    # 4. Set number_of_guesses = 0 for initialization of the variable. The variable will be used to store number of guess attempts.
    # 4. number_of_guesses updates in the while-loop with each guess.
    guess = 0
    number_of_guesses = 0
    
    while guess != random_number: # 3. While-loop initialization
        guess = int(input("Pick a number between 1 & 10: ")) # 3. Player's guess
        number_of_guesses += 1 # 4. Tracking number of guesses
        
        if guess < random_number: # 3.a
            print("It's higher.")
        elif guess > random_number: # 3.b
            print("It's lower.")

    
    print("GOT IT!!!") # 4. Informs user they got it
    guesses_list.append(number_of_guesses) #4. Appends list with number of guesses per the game.
    
    print(f"Number of guesses: {number_of_guesses}")
    print(guesses_list)
             
start_game()

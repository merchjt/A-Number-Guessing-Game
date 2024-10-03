"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Imported random and statistics modules
import random
import statistics

# Defined a function and updating. This will be function that starts and runs the game.
def start_game():
    # 1. Welcome message
    print("WELCOME! I hope you enjoy the game!")
    #2. Created a random number to guess using randrange(): https://docs.python.org/3/library/random.html#functions-for-integers
    #2. Defined the range from 1 to 10. Noted that this function produces and int.
    random_number = random.randrange(1,10) 
    print(random_number) #DELETE - for testing purposes
    
start_game()

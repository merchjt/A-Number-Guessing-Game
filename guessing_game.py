"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# IMPORTS
import random # .randrange() - used to create a random number from 1 to 10 for the game.
import statistics # .mean(), .median() and .multimode() used to display guessing data

# LISTS
# 4. The follow list is created to store a list of guesses per game.
# 4. The list is defined as a global variable so it is not reset to an
# 4. empty list while the start_game function continues to loop. 
guesses_list = [] 

# FUNCTION
def start_game():
    # 1. Welcome message
    print("WELCOME! I hope you enjoy the game!\n")
    print("""Object of the game:
        1. The game will select a random integer from 1 to 10.
        2. You will try to guess the integer
        3. GOOD LUCK!\n""")
    
    # 6. The while loop will run as long as the user wants to keep playing.
    # 6. Near the end of the loop, the user will be prompted for YES/NO response to keep playing.
    while True:
        #2. Created a random number to guess using randrange(): https://docs.python.org/3/library/random.html#functions-for-integers
        #2. Defined the range from 1 to 10. Noted that this function produces an integer.
        random_number = random.randrange(1,10) 

        # 3. Set guess = 0 for initialization of the variable.
        guess = 0
        # 4. Set number_of_guesses = 0 for initialization of the variable. 
        number_of_guesses = 0
        
        #3. The while loop will continue to prompt a player for a guess as long as it does not equal the random_number.
        while guess != random_number:
            # 4. Tracking number of guesses
            number_of_guesses += 1 
            
            # 3. Prompting a guess
            guess = input("Pick a number from 1 & 10: ")
            
            # Added a try block to test for ValueErrors.
            # The random_number is an integer by default of the .randrange() function.
            # If the guess is not an integer, it will prompt an exception error.
            try:
                guess = int(guess)
                if guess < random_number: # 3.a
                    if guess < 1:
                        print("\nToo low and outside the range of possible numbers, try again!")
                    else:
                        print("\nIt's higher, try again.")
                elif guess > random_number: # 3.b
                    if guess > 10:
                        print("\nToo high and outside the range of possible numbers, try again!")
                    else:
                        print("\nIt's lower, try again.")
            except ValueError:
                print("\nPlease provide an integer guess, try again.")
                    
        print("\nGOT IT!!!") # 4. Informs user they got it
        guesses_list.append(number_of_guesses) #4. Appends list with number of guesses per the game.
        
        # 5. Compiling data (mean, median, mode(s)) for series stats
        guesses_list.sort() #5. Sorts the list before running mean, median and mode
        series_mean = round(statistics.mean(guesses_list),2) #5.b
        series_median = statistics.median(guesses_list) #5.c
        series_mode = statistics.multimode(guesses_list) #5.d
        #5.d Converts list to a list of strings for printability of the list.
        #5.d https://www.geeksforgeeks.org/python-program-to-convert-list-of-integer-to-list-of-string/
        series_mode_string = [str(x) for x in series_mode] 
        low_score = min(guesses_list) # To track the low score.
        
        # 5. Display data from the game(s). Including: mean, median and mode(s)
        # 5. https://docs.python.org/3/library/statistics.html#module-statistics
        print(f"Number of guesses this game: {number_of_guesses}") #5.a
        print("\nSERIES STATS:")
        print(f"Mean: {series_mean}") #5.b
        print(f"Median: {series_median}") #5.c
        print("Mode(s): " + ", ".join(series_mode_string) + "\n") #5.d
        
        # 6. Prompts the player if they would like to play again. 
        # 6. The loop will keep asking if a YES/NO response is not given.
        keep_playing = ""
        while True:
            keep_playing = input("Would you like to play again? (YES/NO): ")
            if keep_playing.lower() == "yes":
                break
            elif keep_playing.lower() == "no":
                break
            else:
                print("\nNot a valid response.")
                continue

        # 6. After a (YES/NO) response is given, either runs the game again at the beginning of thw while-loop.
        # 6. Or, will end the game. 
        if keep_playing.lower() == "yes": #6.a. Starts game over
            print(f"\nThe low score to beat is {low_score}")
            continue
        else: #6.b. Ends the game
            print(f"\nThe low score was {low_score}")
            print("Thanks for playing! Bye!\n")
            break

# CALL FUNCTION TO START THE GAME    
start_game()
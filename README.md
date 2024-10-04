# A Number Guessing Game

The game welcomes and prompts the user to guess an integer from 1 to 10. 
The game will select a random integer using the random.randrange() function.
The user will be allowed to make as many guesses as possible until the the correct integer is guessed.
The game will provide statistics for the game and ask if the user would like to continue.
The user can continue as many times as they would like.

Programming requirements are listed below.

NOTE: I would like my project to be rejected if it does not meet all Exceeds Expectations Requirements



===== PROGRAMMING REQUIREMENTS =====
Import the random and statistics modules.

Create the start_game function.
Write your code inside this function.

When the program starts, we want to:
------------------------------------
1. Display an intro/welcome message to the player.
2. Store a random number as the answer/solution.
3. Continuously prompt the player for a guess.
    a. If the guess is greater than the solution, display to the player "It's lower".
    b. If the guess is less than the solution, display to the player "It's higher".

4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
5. Display the following data to the player
    a. How many attempts it took them to get the correct number in this game
    b. The mean of the saved attempts list
    c. The median of the saved attempts list
    d. The mode of the saved attempts list
6. Prompt the player to play again
    a. If they decide to play again, start the game loop over.
    b. If they decide to quit, show them a goodbye message.

( You can add more features/enhancements if you'd like to. )


Kick off the program by calling the start_game function.
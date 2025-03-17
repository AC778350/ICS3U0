# Adena Chaudary
# 778350
# ICS3U0

# Variable Dictionary:
# num: the number the user is trying to guess
# correct: checks to see if the user's guess is the same as the number
# guessnumber: records the number of guesses the user has made
# guess: records the user's guess

import random 
# allows the code to generate random numbers

num = random.randrange(1,100,1)
# sets the variable "num" to a random number in the range 1 - 100

guess = -1
# sets the guess outside of the range

correct = False
# sets the variable "correct" to false 

guessnumber = 1
# sets the guess the user is on to 1

print ("Hello! Welcome to the number guessing game!")
# Introduces the user to the program

print ("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.")
# explains the rules of the game to the user

while not correct:
# runs the loop until correct = True
    
    print("Guess #", guessnumber)
    # lets the user know what guess they are on
    
    guess = int(input("Input Guess:"))
    # prompts the user to guess
    
    correct = (guess == num)
    # if the guess is equal to the random number then correct will be true
    
    if correct:
    # checks if the variable correct is True
        
        print("You guessed right! The number is:", num)
        # lets the user know they guessed correctly
        
        print("Thanks for playing!")
        # thanks the user for playing
    
    else:
    # an alternative if the user's guess in incorrect
        
        guessnumber += 1
        # adds one guess to the amount of guesses
    
        if num > guess:
        # checks if the number is higher than the guess
        
            print("Higher!")
            # if the user's guess is lower than the number
            # let the user know to guess higher
    
        if num < guess:
        # checks if the number is lower than the guess
        
            print("Lower!")
            # if the user's guess is higher than the number
            # let the user know to guess lower
    
        if guessnumber == 7:
        # the user can only have 6 guesses, so if the guess number
        # reaches 7 and the user did not guess correctly, the user has lost
        
            print("Sorry, you are out of guesses! The answer was:", num)
            # lets the user know they are out of guesses and displays
            # the correct number
        
            print("Better luck next time!")
            # prompts the player to try again
        
            correct = True
            # sets the variable correct to True to exit the code

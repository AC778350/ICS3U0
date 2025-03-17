# Adena Chaudary
# 778350
# ICS3U0

import random 
# imports 

num = random.randrange(1,100,1)
# sets the variable "num" to a random number in the range 1 - 100

guess = -1


correct = False
# sets the variable "correct" to false 

guessnumber = 1


print ("Hello! Welcome to the number guessing game!")
# Introduces the user to the program

print ("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.")
# explains the rules of the game to the user

while not correct:
# 
    
    print("Guess #", guessnumber)
    
    
    guess = int(input("Input Guess:"))
    
    
    correct = (guess == num)
    
    
    if correct:
    
        
        print("You guessed right! The number is:", num)
        
        
        print("Thanks for playing!")
    
    
    else:
    
        
        guessnumber = guessnumber + 1
      
    
        if num > guess:
    
        
            print("Higher!")
      
    
        if num < guess:
    
        
            print("Lower!")
      
    
        if guessnumber == 7:
    
        
            print("Sorry, you are out of guesses! The answer was:", num)
        
        
            print("Better luck next time!")
        
        
            correct = True

  # Variable Dictionary:
  # num: the number the user is trying to guess
  # correct: checks to see if the user's guess is the same as the number
  # guessnumber: records the number of guesses the user has made
  # guess: records the user's guess

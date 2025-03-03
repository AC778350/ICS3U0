# Adena Chaudary
# 778350
# ICS3U0

import random 
num = random.randrange(1,100,1)
guess = -1
correct = False
guessnumber = 1
count = 6
print ("Hello! Welcome to the number guessing game!")
print ("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.")
while not correct:
    print("Guess #", guessnumber)
    guess = int(input("Input Guess:"))
    correct = (guess == num)
    if correct:
        print("You guessed right! The number is:", num)
    else:
      guessnumber = guessnumber + 1
      count = count - 1
      if num > guess:
        print("Higher!")
      if num < guess:
        print("Lower!")
if count == 0:
  print("Sorry, you are out of guesses! The answer was,", num)
  print("Better luck next time!")

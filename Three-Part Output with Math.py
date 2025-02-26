import math # imports mathimatical functions into the program
print("Welcome to the even and odd detector!") # introduces the user to the program
print("This program determines if the product of two positive numbers will be even or odd!") # explains the purpose of the program to the user
a = input("Please enter your first number:") # has the user input their first number
a = float(a) # turns the input 'a' into a decimal number
b = input("Please enter your second number:") # has the user input their second number
b = float(b) # turns the input 'b' into a decimal number
if a >= 0 or b >= 0: # compares the inputted numbers to make sure they are not equal to zero
  if a % 2 == 0: # if the remainder of the modulus is equal to zero, the number must be even
    print("The product of", a, "x", b, "will be an even number of", a*b, ".") # lets the user know their product is even as well as provides the product
  elif b % 2 == 0: # if the remainder of the modulus is equal to zero, the number must be even
    print("The product of", a, "x", b, "will be an even number of", a*b, ".") # lets the user know their product is even as well as provides the product
  else: # if the remainder of the modulus is not equal to zero, the number must be odd
    print("The product of", a, "x", b, "will be an odd number of", a*b, ".") # lets the user know their product is odd as well as provides the product
else: # an error message for if the user inputs any numbers lower than zero
  print("Error, you can only use positive numbers.") # lets the user know that they can only input positive numbers
print(" ") # creates a space between the previous and next program
print("I will find the cube's inner diagonal for any side length!") # introduces and explains the purpose of the program to the user
m = input("Please enter the side length of your cube:") # has the user input the side length of the cube 
m = float(m) # turns the input 'm' into a decimal number
if m == 0: # compares the input to zero, as a side length cannot be zero or less
  print("Error, the side length must be greater than 0.") # lets the user know they have inputted an invalid number
else: # provides an error message if the input is <= 0
  print("The length of the inner diagonal of a cube with side length of", m, "is: %.2f" % (m*math.sqrt(3))) # solves the equation using the user's input and rounds to two decimal places
print(" ") # creates a space between the previous and next program
print("Welcome to the change calculator!") # introduces the user to the program
c = input("Please input your amount of change in cents:") # prompts the user to input their amount of change 
c = int(c) # turns the input 'c' into an integer
q = 0 # sets the variable to 0 in case no change is needed for this coin amount
d = 0 # sets the variable to 0 in case no change is needed for this coin amount
n = 0 # sets the variable to 0 in case no change is needed for this coin amount
p = 0 # sets the variable to 0 in case no change is needed for this coin amount
c = c % 100 # finds the remainder of the modulus in case the user inputted more than 99 cents
if c >= 25: # compares c to 25 to see if any quarters can be used
  q = c/25 # the number of quarters equals the number of cents divided by 25
  q = int(q) # turns q into an integer / whole number
  c = c % 25 # The remainder of 25 is the number of cents left after the quarters have been accounted for
  if c >= 10: # compares the cents to 10 to see if any dimes can be used
    d = c/10 # the number of dimes equals the number of cents divided by 10
    d = int(d) # turns d into an integer / whole number
    c = c % 10 # the remainder of 10 is the number of cents left after the dimes have been accounted for
    if c >= 5: # compares the number of cents to 5 to see if any nickels can be used
      n = c/5 # the number of nickels equals the number of cents divided by five
      n = int(n) # turns n into an integer / whole number
      c = c % 5 # the remainder of 5 is the number of cents left after the nickels have been accounted for
      if c >= 1: # compares the number of cents to 1 to see if any pennies can be used
        p = c/1 # the number of pennies equals the number of cents divided by one
        p = int(p) # turns p into an integer / whole number
    else: # if there are no nickels, the code will check if there are pennies.
      if c >= 1: # repeats the code for if there are pennies.
        p = c/1
        p = int(p) 
  else: # if there are no dimes, the code will check if there are nickels and/or pennies.
    if c >= 5: # repeats the code for if there are nickels.
      n = c/5
      n = int(n)
      c = c % 5
    else: # repeats the code for if there are pennies.
      if c >= 1: 
        p = c/1
        p = int(p)
else: # if there are no quarters, the code will check if there are dimes, nickels and/or pennies.
  if c >= 10: # repeats the code for if there are dimes.
    d = c/10
    d = int(d)
    c = c % 10
    if c>= 5: # repeats the code for if there are nickels.
      n = c/5
      n = int(n)
      c = c % 5
      if c >= 1: # repeats the code for if there are pennies.
        p = c/1
        p = int(p)
    else: # repeats the code for if there are no nickels.
      if c >= 1:
        p = c/1
        p = int(p)
  else: # repeats the code for if there are no dimes.
    if c>= 5:
      n = c/5
      n = int(n)
      c = c % 5
      if c >= 1:
        p = c/1
        p = int(p)
    else:
      if c >= 1:
        p = c/1
        p = int(p)
print("Your change under a dollar is", q, "quarters,", d, "dimes,", n, "nickels and", p, "pennies.") # lets the user know how many of each coin they have based on their change input

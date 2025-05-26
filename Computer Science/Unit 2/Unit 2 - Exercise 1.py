print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice:")

if (ch == "A"):
  print("I prefer apples.")
elif (ch == "B"):
  print("I prefer bananas.")
elif (ch == "C"):
  print("I prefer cherries.")
else:
  print ("Error, please choose from the options provided.")

print(" ")

print("I will check your test score to determine out the grade you will recieve.")
x = input("Please input your test score:")
x = int(x)
if (x >= 80) and (x <= 100):
  print("Your test score is an A!")
elif (x >= 70) and (x <= 79):
  print("Your test score is a B!")
elif (x >= 60) and (x <= 69):
  print("Your test score is a C!")
elif (x >= 50) and (x <= 59):
  print ("Your test score is a D!")
elif (x >= 0) and (x <= 49):
  print("Your test score is an F!")
else:
  print("Error, the inputted test score is invalid.")

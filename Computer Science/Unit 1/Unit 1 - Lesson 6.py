import math
age = input("Please enter your age")
age = float(age)
yob = input("Please enter your birth year")
yob = float(yob)
num1 = (yob*2) + 5
num1 = float(num1)
num2 = (num1*50) + age
num2 = float(num2)
ans = (num2-250) / 100
print("Your result is", ans, "which is your birth year and age represented as Year.Age")

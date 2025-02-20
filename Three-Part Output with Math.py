import math
print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")
a = input("Please enter your first number:")
a = float(a)
b = input("Please enter your second number:")
b = float(b)
if a >= 0:
  if b >= 0:
    if a % 2 == 0:
      print("The product of", a, "x", b, "will be an even number of", a*b, ".")
    else:
      if b % 2 == 0:
        print("The product of", a, "x", b, "will be an even number of", a*b, ".")
      else:
        print("The product of", a, "x", b, "will be an odd number of", a*b, ".")
  else:
    print("Error, you can only use positive numbers.")
else:
  print("Error, you can only use positive numbers.")
print(" ")
print("I will find the cube's inner diagonal for any edge length!")
m = input("Please enter the edge length of your cube:")
m = float(m)
if m >= 0:
  print("The length of the inner diagonal of a cube with side length of", m, "is: %.2f" % (m*math.sqrt(3)))
else:
  print("Error, the side length must be greater than 0.")
print(" ")
import math
print("Welcome to the change calculator!")
c = input("Please input your amount of change in cents:")
c = float(c)
q = 0
d = 0
n = 0
p = 0
c = c % 100
if c >= 25:
  q = c/25
  q = int(q)
  c = c % 25
  if c >= 10:
    d = c/10
    d = int(d)
    c = c % 10
    if c >= 5:
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
  else:
    if c >= 5:
      n = c/5
      n = int(n)
      c = c % 5
    else:
      if c >= 1:
        p = c/1
        p = int(p)
else:
  if c >= 10:
    d = c/10
    d = int(d)
    c = c % 10
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
  else:
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
print("Your change under a dollar is", q, "quarters,", d, "dimes,", n, "nickels and", p, "pennies.")

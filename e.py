x = input("Please input a whole number between 1 and 20:")
x = int(x)
if (0 < x) and (x <= 20):
  y = input("Please input another nonzero whole number between 1 and 20:")
  y = int(y)
  if (0 < y)and (y <= 20):
    if y == 0:
      print("Error, y cannot equal 0. A factor cannot be determined.")
    else:
      print("Now deciding if", y, "is a factor of", x, "...")
      rem = x % y
      if rem == 0:
        print("Yes!", y, "is a factor of", x)
      else:
        print("No,", y, "is not a factor of", x)
  else:
      print(y, "is outside of the range, cannot continue.")
else:
  print(x, "is outside of the range, cannot continue.")

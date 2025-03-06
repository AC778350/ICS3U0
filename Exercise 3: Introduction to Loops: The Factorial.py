print("Factorial Calculator:")
n = int(input("Enter a value for the upper limit, n:"))
f = 0
r = 1
while f <= n:
  print(f, end = "! ")
  print("=", r)
  f = f + 1
  r = r * f

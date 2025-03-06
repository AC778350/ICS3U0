n = int(input("Give me a value of n:"))
print("Counting from n = 1 to", n, "...")
print(" ")
f = 1
r = 1
triangle = 1
print("factorial")
while f <= n:
  print(f, end = "! ")
  print("=", r)
  f = f + 1
  r = r * f
print(" ")
print ("triangle")
while triangle <= n:
  triangle = n * (n + 1)
  triangle /= 2
  triangle = int(triangle)
  print(triangle)
  n = n + 1

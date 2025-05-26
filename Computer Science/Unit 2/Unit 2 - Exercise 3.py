n  = int(input("Give me a value of n:"))
print("counting from n = 1 to", n, "...")
print(" ")

print( "n     triangle      factorial")

x = 1
f = 1
r = 1
y = 1
triangle = 1
while x <= n and f <= n and y <= n:
  triangle = x * (x + 1)
  triangle /= 2
  triangle = int(triangle)
  print(y, end = "     ")
  print(triangle, end= "              ")
  print(r)
  y += 1
  x += 1
  f += 1
  r = r * f

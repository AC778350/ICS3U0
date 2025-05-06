import math

c = 5
while c > 0:
  n = int(input("Please input a number:"))
  f = 1
  factors = []
  if (n != 0 and n != 1):
    max0 = int(math.sqrt(n))
    for i in range(1, max0 + 1):
      if n % i == 0:
        if i == 1:
          factors.append(i)
        else:
          f = n // i
          factors.append(i)
          factors.append(f)
  s = 0
  for a in factors:
    s = s + a
  print("Factor sum:", s)
  if s == n:
    print(n, "is perfect.")
  elif s < n:
    print(n, "is deficient.")
  elif s > n:
    print (n, "is abundant.")
  c -= 1
print("Goodbye!")

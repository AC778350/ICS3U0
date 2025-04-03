num = int(input("How many items are you entering?:"))
items = num
print("Enter your items now:")
while items > 0:
  list = input("Item:")
  items -= 1

print("You have entered", num, "items.")

for c in range(len(list)):
  print(list[c])

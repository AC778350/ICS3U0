items = int(input("How many items are you entering?:"))
num = items
print("Enter your items now:")
while items > 0:
  list = input("Item:")
  items -= 1
print("You have entered", num, "items.")
for c in range(len(list)):
    print(c, list[c])

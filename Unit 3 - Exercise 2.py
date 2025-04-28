grocerylist = []
num = int(input("How many items are you entering?:"))
print("Enter items now:")
for i in range(num):
  item = input("item:")
  grocerylist.append(item)
print("You have entered %d items." % len(grocerylist))
for x in grocerylist:
    print(x)

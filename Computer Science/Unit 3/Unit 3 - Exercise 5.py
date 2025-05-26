myList = [22, 91, 59, 67, 55, 84, 7, 16, 89, 48, 69, 30, 98, 28, 31]
highest = myList[0]
lowest = myList[0]
for N in range(1, len(myList)-1):
  if highest < myList[N]:
    highest = myList[N]
for N in range(1, len(myList)-1):
  if lowest > myList[N]:
    lowest = myList[N]
s = 0
for a in myList:
  s = s + a

print("The largest number is:", highest)
print("The smallest number is:", lowest)
print("The sum is:", s)

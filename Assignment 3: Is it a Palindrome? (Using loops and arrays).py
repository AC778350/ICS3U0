print("Palindrome Program!")
print(" ")
wordlist = ["racecar", "school", "civic", "pencil", "radar", "eraser", "kayak", "refer", "chair", "level"]
for x in range(len(wordlist)):
  word = wordlist[x]
  for x in range(len(word) // 2):
    if word[x] != word[len(word) - 1 - x]:
      print(word, "is not a palindrome")
    else:
      print(word, "is a palindrome")

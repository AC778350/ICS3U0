# Adena Chaudary
# 778350
# ICS3U0

# VARIABLE DICTIONARY:
# 1: wordlist - the list of words the program will
# determine whether or not it is a palindrome
# 2: x -
# 3: word - 


print("Palindrome Program!")
# introduces the program to the user 

wordlist = ["racecar", "school", "civic", "pencil", "radar", "eraser", "kayak", "refer", "chair", "level"]
# puts the words that will be checked for being palindromes in a list

for x in range(len(wordlist)):
# "x" will cycle through the words in the list

  word = wordlist[x]
  #
  
  for x in range(len(word) // 2):
  # "x" will cycle through each word in the list.
  # uses integer division to get an even number of letters
  # in each word so the letters can be compared
  
    if word[x] == word[len(word) - 1 - x]:
    # 
    
      print(word, "is a palindrome")
      # lets the user know the word is a palindrom
      
    else:
    # 
      print(word, "is not a palindrome")
      # lets the user know the word is not a palindrome
      
print("Goodbye!")
# lets the user know the program is finished

'''
Adena Chaudary
778350
ICS3U0

--- VARIABLE DICTIONARY: ---
1: wordlist - the list of words used by the program
2: word - representative of each word in the list
3: palindrome - sets to True or False to determine if the word is a palindrome
4: x - counting variable
5: y - counting variable
'''


# introduces the program to the user
print("Palindrome Program!")

# the list of words that will be checked
wordlist = ["racecar", "school", "civic", "pencil", "radar", "eraser", "kayak", "refer", "chair", "level"]

#
for x in range(len(wordlist)):
  
  #
  word = wordlist[x]

  # sets the variable palindrome to True so it can be used
  palindrome = True

  #
  for y in range(len(word) // 2):

    #
    if word[y] != word[len(word) - 1 - y]:

      #
      palindrome = False

  #
  if palindrome:

    #
    print(word, "is a palindrome")

  #
  else:

    #
    print(word, "is not a palindrome")

#
print("Goodbye!")

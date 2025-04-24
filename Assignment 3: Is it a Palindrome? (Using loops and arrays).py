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

# x represents every word in the wordlist
for x in range(len(wordlist)):
  
  # the variable word checks the index of each word (aka, x)
  word = wordlist[x]

  # sets the variable palindrome to True so it can be used
  palindrome = True

  # for y in the range of the length of each word divided by 
  # two and rounded down, this number is used to compare the 
  # letters in the words
  for y in range(len(word) // 2):

    ''' using the word racecar as an example, the letter r is
    at index 0. By comparing it to the length of the word minus
    one minus the current index (represented by y), you can 
    compare the two letters. The reason for subtracting 1
    is due to the index starting at 0. Using the example,
    racecar has 7 letters, so we are comparing r at [0] to
    the last r at [6] (aka 7 - 1 - y. y = 0, therefore
    7 - 1 - 0 = 6)'''
    if word[y] != word[len(word) - 1 - y]:

      # The previous line of code checks for if 
      # the letters are not equal, therefore
      # setting the variable palindrome to false
      palindrome = False

  # checks if the variable palindrome is true,
  # based on the conditions of the for loop before
  if palindrome:

    # lets the user know the word is a palindrome 
    print(word, "is a palindrome")

  # if palindrome is false
  else:

    # lets the user know that the word is not a palindrome
    print(word, "is not a palindrome")

# lets the user know the program is finished
print("Goodbye!")

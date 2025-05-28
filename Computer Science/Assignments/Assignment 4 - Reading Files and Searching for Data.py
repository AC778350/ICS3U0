'''
Adena Chaudary
778350
ICS3U0

--- VARIABLE DICTIONARY: ---
1. database - contains the information from the file
2. datesDatabase - contains the dates from the file
3. wordsDatabase - contains the words from the file
4. parts - separates the months, days, years and words
5. months - the months from the file
6. days - the days from the file
7. years - the years from the file
8. words - the words from the file
9. dates - merges the years, months, days from the file
10. option - checks if the user is looking for a word or date
11. word - the word inputted by the user
12. year - the year inputtted by the user
13. month - the month inputted by the user
14. day - the day inputted by the user
15. d - if the user wants to find a word from a date
16. w - if the user wants to find a date from a word
17. wordDate - the merged date inputted by the user
'''

# sets the variables year, month an day to 0 in
# case the user is not looking for a word's date
year = 0
month = 0
day = 0

# defines the function merge to turn the
# year, month and day into an integer
def merge(y, m, d):
    
    ''' contains the months (as abbreviations) in an array,
    checks to see if the month (represented by m) is equal 
    to the one in the array. If it is equal, m is equal to
    the index number plus one. The one is added since the
    array index starts at 0.'''
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i in range(len(months)):
        if m == months[i]:
            m = i + 1

    # converts m, d and y into strings, so they
    # won't be added numerically when merged
    m = str(m)
    d = str(d)
    y = str(y)

    ''' if d or m is a single digit, adds 0 in front 
    to make it two digits. numbers with d or m with 
    two digits will have more digits when merged,
    which is why this step is necessary '''
    if len(d) == 1:
        d = "0" + d
    if len(m) == 1:
        m = "0" + m

    # adds the strings to make a 6 digit number
    date = (y+m+d)
    
    # returns an integer to be able to compare numbers later
    return int(date)

''' an empty array is created to contain the lines from the 
file. a variable set to false allows the file to be read until
there is nothing left to be read. While reading, each line is
added to the array. a try and except is used to catch any
potential errors with the file. When the file reaches the end,
the variable is set to true and the file is closed'''
database = []
endOfFile = False
try:
    file = open("wordle.dat", "r")
    while not endOfFile:
        line = file.readline().strip()
        endOfFile = (line == "")
        if not endOfFile:
            database.append(line)
    file.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)
    file.close()

# an empty array to hold only the dates from the file
datesDatabase = []

# an empty array to hold only the words from the file
wordsDatabase = []

''' this for loop cycles through the array database and separates the month,
day, year and word. The month, day and year are merged using the merge function.
the dates and words are then appended to the datesDatabase and wordsDatabase 
arrays until the database array is finished '''
for i in range(len(database)):
    parts = database[i].split(" ")
    months = parts[0]
    days = parts[1]
    years = parts[2]
    words = parts[3]
    dates = merge(years, months, days)
    datesDatabase.append(dates)
    wordsDatabase.append(words)

# introduces the user to the program
print("Welcome to the Wordle Database!")

# prompts the user to input w to find the date of a word
# or d to find the word for a date
option = input("Enter w if you are looking for a word, or d for a word on a certain date:")

# if the user entered d, the program will ask them to input
# the year, month and day they are looking for. It will then
# merge the three using the merge function
if option == "d":
    year = input("Enter the year: ")
    month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
    day = input("Enter the day: ")
    wordDate = merge(year, month, day)
    
    # if the merged number is less than 20210619 or larger
    # than 20240421, the program will let the user know
    # that the date they added is too early/far ahead
    if wordDate < 20210619:
        print("Too early! Pick a date after Jun 19 2021.")
    elif wordDate > 20240421:
        print("Too far! Pick a date before Apr 21 2024.")
    
    # cycles through the datesDatabase array to find the
    # matching date. Prints a statement to tell the user the
    # word from the wordsDatabase array at the same index
    for x in range(len(datesDatabase)):
        if wordDate == datesDatabase[x]:
           print("The word on", wordDate, "was", wordsDatabase[x])

# if the user entered w, prompts them to enter the word they are looking for
elif option == "w":
    word = input("What word are you looking for? (write in all CAPS): ")

    ''' sets the variable equal to false until the inputted word
    and a word in the database is the same. If equal is True,
    prints a statement letting the user know the date of the
    word from the datesDatabase array using the same index number'''
    equal = False
    for x in range(len(wordsDatabase)):
        if word == wordsDatabase[x]:
            equal = True
            print("The word", word, "was the answer on", datesDatabase[x])
    
    # if equal is never set to True, the word does not exist in the database
    if not equal:
        print("Error, word is not in the database.")

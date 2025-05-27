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

    m = str(m)
    d = str(d)
    y = str(y)

    if len(d) == 1:
        d = "0" + d
    if len(m) == 1:
        m = "0" + m

    date = (y+m+d)
    return int(date)

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

datesDatabase = []
wordsDatabase = []
for i in range(len(database)):
    parts = database[i].split(" ")
    months = parts[0]
    days = parts[1]
    years = parts[2]
    words = parts[3]
    dates = merge(years, months, days)
    datesDatabase.append(dates)
    wordsDatabase.append(words)

print("Welcome to the Wordle Database!")
option = input("Enter w if you are looking for a word, or d for a word on a certain date:")
if option == "d":
    year = input("Enter the year: ")
    month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
    day = input("Enter the day: ")
    wordDate = merge(year, month, day)
    if wordDate < 20210619:
        print("Too early! The earliest date is Jun 19 2021.")
    elif wordDate > 20240421:
        print("Too late! The latest date is Apr 21 2024")
    for x in range(len(datesDatabase)):
        if wordDate == datesDatabase[x]:
           print("The word on", wordDate, "was", wordsDatabase[x])
elif option == "w":
    word = input("What word are you looking for? (write in all CAPS): ")
    equal = False
    for x in range(len(wordsDatabase)):
        if word == wordsDatabase[x]:
            equal = True
            print("The word", word, "was the answer on", datesDatabase[x])
    if not equal:
        print("Error, word is not in the database.")

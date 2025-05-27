def merge(y, m, d):
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i in range(len(months)):
        if m == months[i]:
            m = i + 1

    m = str(m)
    d = str(d)
    y = str(y)

    if len(d) == 1:
        d = "0" + day
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
        endOfFile = (line == " ")
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
if option == "w":
    word = input("What word are you looking for?: ")
elif option == "d":
    year = str(input("Enter the year: "))
    month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
    day = str(input("Enter the day: "))

wordDate = merge(year, month, day)

if option == "d":
    for x in range(len(dates)):
        if wordDate == dates:
           print("The word on", wordDate, "was", wordsDatabase[x])
elif option == "w":
    for x in range(len(wordsDatabase)):
        if word == wordsDatabase[x]:
            print("The word", word, "was the answer on", dates[x])

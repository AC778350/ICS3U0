print("Welcome to the Wordle Database!")
option = input("Enter w if you are looking for a word, or d for a word on a certain date:")
if option == "w":
    myWord = input("What word are you looking for?:")
elif option == "d":
    year = str(input("Enter the year:"))
    month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'):")
    day = str(input("Enter the day:"))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for i in range(len(months)):
    if month == months[i]:
        month = i + 1
    else:
        i += 1

month = str(month)

if len(day) == 1:
    day = "0" + day
if len(month) == 1:
    month = "0" + month

def merge(y: str, m: str, d: str):
    date = (y+m+d)
    return int(date)

wordDate = merge(year, month, day)

word = []
try:
    wordle = open("wordle.dat", "r")
    line = wordle.readline().strip()
    if line == wordDate:
        word.append(line)
    wordle.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)
    wordle.close()

print("The word entered on", wordDate, "was", word[0])

year = 0
month = 0
day = 0

print("Welcome to the Wordle Database!")
option = input("Enter w if you are looking for a word, or d for a word on a certain date:")
if option == "w":
    word = input("What word are you looking for?:")
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

def date(year: str, month: str, day: str):
    date = year+month+day
    return int(date)

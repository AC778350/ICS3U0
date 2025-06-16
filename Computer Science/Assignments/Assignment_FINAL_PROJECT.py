'''
Adena Chaudary
778350
ICS3U0

*** VARIABLE DICTIONARY: ***

--- FUNCTION: EXPDATE---

y --> the year represented by the integer (YYYY)
m --> the month represented by the integer (M) or (MM)
date --> the final merged date 

--- FUNCTION: MERGESORT ---

arr --> the array (containing integers) to be sorted
arr2 --> the second array to be sorted
arr3 --> the third array to be sorted
arr4 --> the fourth array to be sorted
arr5 --> the fifth array to be sorted
arr6 --> the sixth array to be sorted
l --> the leftmost index of the array
r --> the rightmost index of the array
m --> the index in the middle of the array

--- FUNCTION: MERGE ---

*** ALL THE VARIABLES FROM THE
MERGESORT FUNCTION ALSO APPLY TO
THIS FUNCTION ***

left --> the number of elements on the left
side of the array

right --> the number of elements on the right
side of the array

leftSide --> array containing the data on the
left side of the array *** all variables
with the name leftSide represent this for
its respective array ***

rightSide --> array containing the data on the
right side of the array *** all variables
with the name rightSide represent this for its
respective array ***

li --> index number of the left array
ri --> index number of the right array
ai --> index number of the merged array

--- MAIN CODE ---

GivenName --> array containing the data GivenName from the file
Surname --> array containing the data Surname from the file
CCType --> array containing the data CCType from the file
CCNumber --> array containing the data CCNumber from the file
ExpMonth --> array containing the data ExpMonth from the file
ExpYear --> array containing the data ExpYear from the file
endOfFile --> a variable to tell when to stop reading the file
file --> a handle to open and close the file for reading
ExpiryDates --> an array to hold all the coverted expiry dates
Status --> an array to hold all the card statuses
exp --> a variable to convert the years and months to one number
and to check if a card is expired or not
file2 --> a handle to open and close the file for writing
'''

''' The purpose of this function is to take a
year (YYYY) and a month (M) or (MM) and convert
it to an inter written as (YYYYMM). It first
converts them to string so they are not added
together, and if m is only one digit, adds a 0
at the front. The last step is to add them together
and then return the date as an integer'''
def ExpDate(y, m):
    
    y = str(y)
    m = str(m)
    
    if len(m) == 1:
        m = "0" + m
    
    date = y + m
    return int(date)


''' In our data file, there are 6 columns of data, meaning
there are 6 different arrays to sort. l and r represent the
leftmost index of the array and r the righmost index. All
arrays must be the same length.'''
def mergeSort(arr, arr2, arr3, arr4, arr5, arr6, l, r):
    
    ''' if the length of the array is less than or equal to
    1, that means that the array is already sorted making
    that the base case. It is not neccessary to add this step
    as the array will be returned as is if this is the case'''
    
    # if the leftmost index is less than the rightmost index,
    # the data will begin to sort
    if l < r:

        # m becomes the index in the middle of the array
        m = (l + r) // 2
        
        # the mergeSort function is called recursively
        # taking half of the array each time until there
        # are sub arrays left with only one value in them
        mergeSort(arr, arr2, arr3, arr4, arr5, arr6, l, m)
        mergeSort(arr, arr2, arr3, arr4, arr5, arr6, m+1, r)
        
        # it then takes the data and sends it to a function
        # to be sorted
        merge(arr, arr2, arr3, arr4, arr5, arr6, l, m, r)

# this function will be used to sort the data
def merge(arr, arr2, arr3, arr4, arr5, arr6, l, m, r):
    
    # the variables left and right contain the 
    # number of data on each side of the array
    left = m - l + 1
    right = r - m

    # creates an array of zeroes for each side of each array
    # of the same size of each side
    leftSide = [0] * left
    rightSide = [0] * right

    leftSide2 = [0] * left
    rightSide2 = [0] * right

    leftSide3 = [0] * left
    rightSide3 = [0] * right

    leftSide4 = [0] * left
    rightSide4 = [0] * right
    
    leftSide5 = [0] * left
    rightSide5 = [0] * right

    leftSide6 = [0] * left
    rightSide6 = [0] * right

    li = 0 # the first index of the left subarray
    ri = 0 # the first index of the right subarray
    ai = l # the first index of the merged subarray

    # this step copies all the data from the left side
    # of the arrays into the temporary arrays for the
    # left side
    for x in range(0, left):
        leftSide[x] = arr[l + x]
        leftSide2[x] = arr2[l + x]
        leftSide3[x] = arr3[l + x]
        leftSide4[x] = arr4[l + x]
        leftSide5[x] = arr5[l + x]
        leftSide6[x] = arr6[l + x]

    # same thing as above but instead for the right side
    for y in range(0, right):
        rightSide[y] = arr[m + 1 + y]
        rightSide2[y] = arr2[m + 1 + y]
        rightSide3[y] = arr3[m + 1 + y]
        rightSide4[y] = arr4[m + 1 + y]
        rightSide5[y] = arr5[m + 1 + y]
        rightSide6[y] = arr6[m + 1 + y]

    # this loop will run while the left and
    # right index is less than the number of
    # elements in each side
    while li < left and ri < right:
        
        ''' if the number on the left side is
        smaller or equal to the right side,
        the number at that index in the original
        array becomes that number. ***It is only
        comparing the numbers from the parameter
        "arr" since it is the only array with integer
        data. The rest are swapped alongside it so
        the indices will match at the end. '''
        if leftSide[li] <= rightSide[ri]:
            arr[ai] = leftSide[li]
            arr2[ai] = leftSide2[li]
            arr3[ai] = leftSide3[li]
            arr4[ai] = leftSide4[li]
            arr5[ai] = leftSide5[li]
            arr6[ai] = leftSide6[li]
            
            # one is added to the left index so 
            # it can move on to the next number
            li += 1
        
        # same thing as above except if the right
        # number is smaller instead
        else:
            arr[ai] = rightSide[ri]
            arr2[ai] = rightSide2[ri]
            arr3[ai] = rightSide3[ri]
            arr4[ai] = rightSide4[ri]
            arr5[ai] = rightSide5[ri]
            arr6[ai] = rightSide6[ri]
            ri += 1
        
        ai += 1
    
    """if all the numbers have been compared and
    there are still numbers left that havent been
    added, adds those to the merged array until
    all numbers have been added (in which case the
    index becomes higher than the number of elements)"""
    
    # adding the remaining numbers for the left side:
    while li < left:
        arr[ai] = leftSide[li]
        arr2[ai] = leftSide2[li]
        arr3[ai] = leftSide3[li]
        arr4[ai] = leftSide4[li]
        arr5[ai] = leftSide5[li]
        arr6[ai] = leftSide6[li]
        li += 1
        ai += 1
    
    # adding the remaining numbers for the right side:
    while ri < right:
        arr[ai] = rightSide[ri]
        arr2[ai] = rightSide2[ri]
        arr3[ai] = rightSide3[ri]
        arr4[ai] = rightSide4[ri]
        arr5[ai] = rightSide5[ri]
        arr6[ai] = rightSide6[ri]
        ri += 1
        ai += 1

# ***MAIN CODE***

# empty arrays to hold the data from each column
GivenName = []
Surname = []
CCType = []
CCNumber = []
ExpMonth = []
ExpYear = []

# sets a variable to false until the file
# reaches the end
endOfFile = False

''' reads the file, adding each piece of data to
its respective array. In the file, the data is
organized using commas, so it splits the data
between each comma. '''
try:
    file = open("data.dat", "r")
    while not endOfFile:
        line = file.readline().strip()
        endOfFile = (line == "")
        if not endOfFile:
            (gn, sn, cct, ccn, expm, expy) = line.split(",")
            GivenName.append(str(gn))
            Surname.append(str(sn))
            CCType.append(str(cct))
            CCNumber.append(str(ccn))
            ExpMonth.append(expm)
            ExpYear.append(expy)
    file.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)
    file.close()

# removes the first index of each array
# as it is not needed (header information)
GivenName.remove(GivenName[0])
Surname.remove(Surname[0])
CCType.remove(CCType[0])
CCNumber.remove(CCNumber[0])
ExpMonth.remove(ExpMonth[0])
ExpYear.remove(ExpYear[0])

# empty arrays for the expiry dates and the
# expiry status of the cards
ExpiryDates = []
Status = []

# calls the function ExpDate to organize
# the dates from the file. The data is then
# added to the ExpiryDates array
for i in range(len(ExpYear)):
    exp = ExpDate(ExpYear[i], ExpMonth[i])
    ExpiryDates.append(exp)
    
    '''if the expiry date is before the cutoff,
    appends "EXPIRED" to the Status array. If it
    is equal to the cutoff, appends "RENEW IMMEDIATELY".
    if the card is not expired, then a space character
    is added to the array in its place (to make sure the
    arrays are all the same length)'''
    if exp < 202507:
        Status.append("EXPIRED")
    elif exp == 202507:
        Status.append("RENEW IMMEDIATELY")
    else:
        Status.append("")

'''calls the mergeSort function for each of the data types,
plus the leftmost index and the rightmost index. ExpiryDates
is first as it is what is being compared (integer data). The
order of the rest of the arrays is not relevant as it completes
the same task '''
mergeSort(ExpiryDates, GivenName, Surname, CCType, CCNumber, Status, 0, len(ExpiryDates)-1)

'''writes the formatted data into a new file (data.txt)
the information is aligned to the left and each element
is assigned the same amount of characters so that it will
be formatted nicely when it is outputted to the file'''
try:
    file2 = open("data.txt", "w")
    for i in range(len(GivenName)):
        file2.write(f"{GivenName[i] + ' ' + Surname[i]:<40} {CCType[i]:<15} #{CCNumber[i]:<18} {ExpiryDates[i]:<8} {Status[i]:<20}\n")
    file2.close()
except IOError as err:
    print("IOError: ", err)
except OSError as err2:
    print("OSError: ", err2)
except PermissionError as err3:
    print("PermissionError: ", err3)

# ListPython Practice (Python List) Date: (06-03-2026 Friday)
from os import remove

# Python List Created Ally Syntext
# List1 = ["Shanto","Soni",20,False,20.1,"Mahi"]
# Python List Length Checking Command : len(List1)
# Python List Updated Command Using for Index: List1[1] = "Mahi"
# Python List Type Checking Command : print(type(List1)
# Python List Single Value Showing Command for Using for Index : print(List[3])
# Python List Adding Command : append("Samiya") adding the list last positon
# Python List Adding Command : insert(1,"Munni") adding the follow in your index number
# Python List Remove Items Command : Remove("Munni") this list item and name munni
# Python List Pope Items Command : pop(1) this is items his Remove pop index
# Python List Del Items Command : del List1[2] this is index 2 Remove here

# Print gapping line
print("\n\n")
# Python List Created in Cricket Player
cricketPlayer = ["tamim", "sakib", "mahmud", 210, 501.20, False, "Ashraf", "Shanto"]

# Python List Showing
print(cricketPlayer)
print(len(cricketPlayer))
# Python List Type Showing
print(type(cricketPlayer))

# Python List Index usg and showing and Updated Data
cricketPlayer[1] = "Samiya Sultana"
cricketPlayer[2] = "Munni Aktar"
cricketPlayer[0] = "Shipa Aktar"
cricketPlayer[4] = 5000.50
# Showing Updated Data
print(cricketPlayer)

# Showing Single item Data Using  for Index Value for List
print(cricketPlayer[1])

print(cricketPlayer[2])
# Python List Updated and List
# Created and Single List Updated and Showing Done.


# Python Another list Created Fruits Item List in Python

# Python List Created
fruits = ["banana", "orange", "cherry", "apple", "apple"]
# List Showing
print(fruits)
# Python List Updated in Using fo Index
fruits[1] = "Mango"
# And Updated List Print
print(fruits)
# Single Value Showing Another Value
print(fruits[3])
# Python List Length Showing (len Command)
print(len(fruits))
# Python List Type Checking
print(type(fruits))
print(fruits)

# Python-এ slicing Rule First to End +1 (akhane ache 0-4)
newlist = ["apple", "banana", "cherry", "Shipa"]
newlist[1:4] = ["Munni Milk"]
print(newlist)

# Python - Add List Items Practice (Python List Item Add)
print("\n\n")

# Another List Created
man = ["Shanto", "Rahatul", "Hossen", "Munni"]
# Python List Adding Item append() Command
man.append("Sam Altman")
man.append(520)
man.append(250.1230)
man.append(False)
print(man)

# Python List Item Adding : Insert Items all Position
print("\n\n")

shanto = ["sakib", 100, 20.21, False, "Munni", "Samiya", "Sanjida"]
shanto.insert(2, "Borsha")
shanto.insert(5, "Israt")
print(shanto)

# Another Python List Created
company = ["Meta", "Google", "Vivo", "Tesla", "NVDI"]
company.insert(2, "Sumsung")
print(company)
print(type(company))

# Python List Remove Practice
print("\n\n")

# Python Another List Created
game = ["football", "cricket", "bolyball", "hocky"]
print(game)
# Python Remove Keyword Using
game.remove("bolyball")
print(game)
# Python Pop Keyword Using
game.pop(1)
print(game)

# Del Keyword Using for the Python
print("\n\n")
games = ["football", "cricket", "bolyball", "hocky"]
del games[1]
print(games)

# Python Total List Remove here Command
print("\n\n")

listOne = [10, 50.21, "Sadiya", "Shanto"]
print(listOne)
listOne.clear()
print(listOne)

# For Loop Practice:
# Practice Date: (07-03-2026 Saturday)
# Rahatul Hossen Shanto : (Native Android Developer)
# Python for loop Practice
# Python range & len method Practice
# Python Loop Practice implementing with Python List


# You can loop through the list items by using a for loop:
# Loop Through a List (Practice in Python) For Loop Practice in Python
print("\n\n")
# python another list created
loopList = ["Samiya", "Munni", "Shipa", "Fariya", "Borsha", "Mithila", "Tanha"]
# python for loop created
for x in loopList:
    print(x)

# Use the range() and len() functions to create a suitable iterable.
# Another Loop Practice Range & Len Python
# Using Python Range & Len Method Python
print("\n\n")
# python another list Created
girlsList = ["Rohima", "Adri", "Israt", "Rehana", "Jebin"]
for x in range(len(girlsList)):
    print(x)

# Practice Date: (07-03-2026 Saturday)
# While Loop Practice in Python
# Rahatul Hossen Shanto : (Native Android Developer)
# Practice Python While Loop
# Print all items, using a while loop to go through all the index numbers
print("\n\n")

# Another Python List Created
boyList = ["Shanto", "Rakib", "Mushfiq", "Rahim"]
# while loop created
y = 0
while y < len(boyList):
    print(boyList[y])
    y = y + 1

print("\n\n")
# Another While Loop Practice
# While Loop Practice in Python
# While Loop Using in Python Loop Listing
birdsList = ["doyeel", "Koyeel", "Shaleek", "Choroiee", "hati", "egale", "hailka"]
x = 0
while x < 7:
    print(birdsList[x])
    x = x + 1

# Python - List Comprehension Practice in Using Python Language
print("\n\n")
print("This is Python List Comprehension This Line Code: and The Double Value")
# new_list = [expression for item in iterable]

# Another list Crated
num = [1, 2, 3, 4, 5]
double = [i * 2 for i in num]
print(double)


# Python - Sort Lists Practice in Using Python Language
print("\n\n")

# another list created
listB = ["banana","orange","fish","mango","mahi"]
listB.sort() # Capital Latter based sorting in python sort list
print(listB)


# Python Sort List Another
thisList = [100, 50, 65, 82, 23]
thisList.sort() # This Number Type Sorting in Small to Big
print(thisList)

# Python Sort List Another Practice
shanto = [500,200,20,1000,800,2,200]
shanto.sort(reverse=True) # This Sorting in Python is Reverse Big number to Small
print(shanto)

# Phthon Sort List using in the String type
fruits = ["mango","banana","mahi","samiya"]
fruits.sort(reverse=True)
print(fruits)

# Python - Copy Lists Practice in Using Python Language
sam = ["ashik","ridoy","srabon","payel"]
newCopy = sam.copy()
print(f"This is Old List : {sam}")
print(f"This is New List : {newCopy}")

# Python - Join Lists in Practice Python Programming Language
print("\n\n")
# Join 2 Item List Here

mahi = ["fish","chicken","kabab","egg"]
shanto = ["salat","orange","lebu"]
joinList = mahi + shanto
print(joinList)

# Python Another Join List Method Practice Here
shova = ["farhana","samiya","adri","sbli"]
samiya = ["22",5000,"Israt"]
shova.extend(samiya)
print(shova)


# Python Count Method Using in Practice
print("\n\n")
print("This is Python Count Method Checking: Item koto bar ache Sheta? ")
fruits = ['apple', 'banana', 'cherry','orange','cherry','shanto','orange']
x = fruits.count("cherry")
print(x)


# Python List Exercises : Practice in Python Using Python
# W3 School Practice in Exercises
# OK Run.........
# Date : (10-03-2026 TuesDay) 20 Ramadan Today.........




# Excercises Question Bank Practice Here
"""
shanto = ['samiya','israt','mahi','dipa']
value = shanto[-1]
print(value)

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[3:6])

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])


fruits = ["apple", "banana", "cherry"]
fruits.insert(2,"lemon")
print(fruits)

[print(x) for x in ['apple', 'banana', 'cherry']]
"""
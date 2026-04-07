# Python Tuple Practice
# Date : 11-03-2026
# Coder : Shanto
# A tuple is a collection which is ordered and unchangeable.
from itertools import count

# Created a Python Tuple
thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(type(thisTuple))
print(thisTuple)

# Python - Access Tuple Items System Practice Here
# [-1] == Tuple  Last Item k Arrested kora.
# [0] == Tuple  First Item k Arrested kora. (Old Style)
# Access Tuple Items
print(thisTuple[1])
print(thisTuple[-5])

# Python Range of Indexes Access Practice Here.
# 0- theke Starting hove but end Index 1+ ditee Count Korar Jonno.
print("\n")
munniTuple = ("Samiya", "Shipa", "Rohima", 500, False, 50.12, "Shanto")
print(munniTuple)
print(munniTuple[2:6])  # proved

# Python - Update Tuples Practice Here
# Change Tuple Values
print("\n\n")
# First Step : Tuple List Created
# Second Step : Tuple to Convert List with Variable
# Third Step : List to Convert Tuple with First Tuple Variable Using
# Fourth Step : List type Variable Using to Sqare Bracket and Indexing Tuple Updated
# Five Step : Print tuple
# print Final Out Put

shantoTuple = ("Munni", "Shipa", "Tamu", "Jui")
x = list(shantoTuple)  # Tuple convert this ListType
x[3] = "Fariya"
print(type(x))
shantoTuple = tuple(x)  # List Convert this Tuple
print(type(shantoTuple))
print(shantoTuple)

# Python - Update Tuples
print("\n\n")

munni = ("Shipa", "Samiya", 500, False, "SajjadurRahaman", "Shanto")
s = list(munni)  # tuple convert to list
s[4] = "Rahatul"
munni = tuple(s)  # list convert to tuple
print(munni)

# Another Practice Python Tuple Updated
santo = ("Ashik", "Rahman", "Ashraf", 500, True)
v = list(santo)  # convert to list
v.insert(3, "Soniya")
# v.append("Samiya")
# v[2] = "Shanto"
santo = tuple(v)  # list convert to tuple main variable
print(santo)

# Python - Unpack Tuples :
# Practice in Python Programming Language
print("\n\n")

soniya = ("Borsha", "Munni", "Samiya", "Tinu")
(Smoth, Darkish, Pink, White) = soniya
print(Pink)
print(Darkish)
print(Smoth)
print(White)

# Python Tuple Unpack Practice
print("\n")
lima = ("Sadiya", "Samiya", "Jui")
(pink, dark, queen) = lima
print(pink)
print(dark)
print(queen)

# Python Unpack Tuple
print("\n")
santoTupleGirls = ("Samiya", "Shanto", "Rishana", "Borsha")
(a, *b, c) = santoTupleGirls
print(a)
print(b)
print(c)

# Using Asterisk* Python in Practice
print("\n\n")
Mithi = ("First Value", 200.142, "Muntaha", "Fahmida", "Samiya", "Munni", "Last Value")
(a, *b, c, d) = Mithi
print(a)
print(b)
print(c)
print(d)

# Python - Loop Tuples
# Python - Loop Tuples Practice in IDE
print("\n\n")

# this is normal Loop practice
Sadiya = ("Shanto", "Rakib", "Munni", "Arafat")
for x in Sadiya:
    print(x)

# Loop Through the Index Numbers Practice
# If Needed Index then Using Range and Len Loop
print("\n")

Lamiya = ("Tanha", "Mithi", "Rishana", "Shipa", "Esrat")
for x in range(len(Lamiya)):
    print(Lamiya[x])

# Noramlly Loop Using
# If Needed Only Value then Using the Normally Loop
print("\n\n")
for i in Lamiya:
    print(i)

# Python Best Practice and Best Way Loop in Python
print("\n\n")
# If You Needed Index + Value then Using the Enumearate Loop
for index, val in enumerate(Lamiya):
    print(index, val)

print("\n\n")
# Python Loop Testing Practice
# Python Loop Only Tuple Value
Samiya = ("Shanto", "Fariya", "Munni", "Shipa", "Orpa", "Samiya")
for x in Samiya:
    print(x)

print("\n\n")
# Python Loop Testing Practice
# Python Loop Range + Value
Sadiya = ("Tarek", "Rahi", "Abir", "Mahi", "Jihad", "Niloy", "Payel")
for i in range(len(Sadiya)):
    print(Sadiya[i])

print("\n\n")
# Python Loop Testing Practice
# Python Loop Index + Value Getting and Proffesonal System Loop
Fariha = ("Ashik", "Rehana", "Borsha", "Ratul", "Shipa")
for index, name in enumerate(Fariha):
    print(index, name)

# Python Tuples Using a While Loop
# Practice
print("\n\n")

myGirls = ("Munni", "Fariha", "Shipa", "Tamu", "Rohima", "Dipa", "Tanha")
i = 0
while i < len(myGirls):
    print(myGirls[i])
    i = i + 1

print("\n\n")
# Another Practice in Python While Loop Usg in Tuple
myGfList = ("Farhana", "Orpa", "Mithi", "Jui", "Samiya", "Mahi", "Tamima", "Ripa", "Sumaiya", "Munni")
x = 0
while x < len(myGfList):
    print(myGfList[x])
    x = x + 1

# Python Joining Tuples Two Tuples Join
print("\n\n")
# Python - Join Tuples
# Python - Join Tuples Practice in IDE

fndListOne = ("Jihad", "Ashik", "Naim")
fndListTwo = ("Rahim", "Maruf", "Asif")
# Join Two Tuples
joinTuple = fndListOne + fndListTwo
print(joinTuple)

print("\n")
# Multiply Tuples
GirlsName = ("Sanjida", "Dipa", "Tanha", "Rishana")
toupleMulti = GirlsName * 2
print(toupleMulti)

# Python Tuples Method
print("\n\n")
# Python Tuples Count Method ar Kaj holo dhoren
# Count(5) dila Tuple er bitore 5 koyta ache seta khuje divee.
# Python Tuple Methods Practice in IDE
# Tuples Count() Method Practice
shantoTouples = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = shantoTouples.count(5)
print(x)

# Python Tuples Index Method Practice Here
# Python index Method usg  kora hoy tuples ar
# position koto number A Ache Seta dekhar jonno.

print("\n\n")
jui = ("Shanto", "Samiya", "Fariha", "Shipa", "Tinu")
x = jui.index("Shipa")
print(x)

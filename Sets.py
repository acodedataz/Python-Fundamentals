# Python Sets Practice

# Python Sets
shanto = {50, "Shanto", 50.21, False}
print(shanto)
# Sets index Number Showing Command len()
print(len(shanto))
# Show type
print(type(shanto))

# Duplicate Not Allowed
munni = {20, "Samiya", 20, "Samiya"}
print(munni)

# True and 1 Same Value, and This is Duplicate Value
samiya = {"apple", "banana", "cherry", True, 3, 2, 1}
print(samiya)

# False and 0, Same Value this is Duplicate Value
shipa = {20, "Shanto", False, 0, 500}
print(shipa)

print("\n\n")
# Python - Access Set Items Practice
Rahul = {"Sadiya", "Israt", "Romana", "Payel"}
for x in Rahul:
    print(x)

# Check if "Romana" is present in the set:
print("Romana" in Rahul)

# Check if "Romana" is NOT present in the set:
print("Romana" not in Rahul)

# Python - Add Set Items Practice
lipa = {"Sanjida", "Sneha", "Rifa", "Mahi"}
lipa.add("Samiya")
print(lipa)

print("\n\n")
# Add Sets in Python
# And Mixching this Value
priya = {"Mriya", "Jebin", "Ishika"}
jui = {"Snigdha", "Nishi", "Hridika"}
priya.update(jui)
print(priya)

# Add Any Iterable in Python Sets
# List and Sets Mixching Behavior this time
print("\n")
mySets = {"Shanto", "Rakib", "Mobarak", "Jubayer"}
myLists = ["Jebin", "Shova", "Munni", "Samiya"]
mySets.update(myLists)
print(mySets)

# Python - Remove Set Items Practice
print("\n\n")
# Set Remove Items using the command : remove()
sathi = {"Shanto", 520, "Munni", "Shipa", 520.21}
sathi.remove("Shanto")
print(sathi)

# Another Practice Remove in the Sets Items
# Using the Command : discard()
print("\n\n")
mahi = {"Payel", "Munni", "Fariha", "Jui"}
mahi.discard("Jui")
print(mahi)

# Another Practice Sets Removing
# Pop Method usg and any item Remove here.
print("\n")
orpa = {"Hakima", "Nahima", "Putul", "Rashed"}
x = orpa.pop()
print(x)

# Another Practice Sets Remove
# Akdom all Sets Remove here : clear()
print("\n")
halima = {"Tanha", "Lamiya", "Mithi", "Arpa", "Priya"}
halima.clear()
print(halima)

# Another Practice sets Removing

# print("\n")
# tanha = {"Habiba","Nusrat","Tisha","Akhi","Eti Aktar"}
# del  tanha
# print(tanha)

# Python - Loop Sets Practice in IDE
# Using the For Loop in Sets with Python
print("\n\n")
rishana = {"Rishana", "Ekra", "Tabassum", "Niha"}
for x in rishana:
    print(x)

# Python - Join Sets Practice in Python IDE
# Using for UNION

print("\n\n")
setsOne = {"Shanto", 1, 2, 500, "Shipa"}
setsTwo = {20, "B", "Sunny", "Lina"}
setThree = setsOne.union(setsTwo)
print(setThree)

print("\n")
# Join Multiple Sets
set1 = {1, 2, 3, 4, 5, 6}
set2 = {22, 23, 24, 25, 26}
set3 = {30, 40, 50, "Shanto"}
mySet = set1.union(set2, set3)
print(mySet)

# Sets to Join tuple
# Usg for the Union
print("\n")
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


print("\n")
# Python frozenset Practice in the IDE
# Creating a frozenset
sumaiya = frozenset({"Sathi","America","Idila","Rohima"})
print(sumaiya)
print(type(sumaiya))

print("\n")
# Python Set copy() Method
liyana = {1.2,3,4,5}
x = liyana.copy()
print(liyana)
print(x)

print("\n")
# Python Set difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)

print(z)
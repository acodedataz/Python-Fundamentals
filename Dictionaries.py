# Dictionaries Created
print("\n")
MuniyaDic = {
    "Samiya": {
        "name": "Samiya Sultana",
        "Id": 500,
        "Subject": "Computer Science",
        "University": "Dhaka University"
    },
    "Shanto": {
        "name": "Rahatul Hossen Shanto",
        "id": 50,
        "Subject": "Computer Science",
        "University": "North South University",
    }
}
print(MuniyaDic["Shanto"]["University"])

# Another Dictionaries Items Created
print("\n")
shanto = {
    "name": "Habiba",
    "email": "habiba@gmail.com",
    "phone": 1609526234,
    "Location": "Gulshan-3"
}
print(shanto["Location"])
print(shanto["email"])
print(len(shanto))

# Python Dictionary Item Value Access
print("\n")
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict["colors"][0])

print("\n")
# Python - Access Dictionary Items and Key & Value
thisDic = {
    "model": "BMW",
    "price": 50000,
    "title": False
}
print(thisDic.keys())
print(thisDic.values())

# Another Dictionary Created (1.0)
print("\n")
SunnyLeone = {
    "SunnyPersonalInfo": {
        "Name": "Sunny Leone",
        "Age": 35,
        "Location": "United State America-55FS",
        "Gender": "Female",
        "Work": "Porn Star"
    },
    "FriendName": "Miya Miya",
    "FacebookFollower": "7M"
}
# Showing Dictionary Data(1.1)
print(f"{"Sunny Leone Information:"}{"\n"}"
      f"{SunnyLeone["SunnyPersonalInfo"]["Name"]}"
      f"{"\n"}{SunnyLeone["SunnyPersonalInfo"]["Location"]}{"\n"}"
      f"{SunnyLeone["SunnyPersonalInfo"]["Work"]}{"\n"}"
      f"{SunnyLeone["SunnyPersonalInfo"]["Age"]}")

# Python - Change Dictionary Items
print("\n")
shantoDic = {
    "name": "Shanto",
    "Age": "22 year, 3 month",
    "Work": "Software Developer",
    "Location": "Laskshmipur",
    "Salary": 80000
}
shantoDic["Location"] = "New York-USA"
shantoDic["Salary"] = "2000$"
print(shantoDic)

# Another Dictionary
Payel = {
    "Fariha": {
        "name": "Fariha Khadiza",
        "Age": 22,
        "Location": "Alexander",
        "Relationship": "Single"
    },
    "Gender": "Female"
}
Payel.update({"Relationship": "Marred"})
print(Payel)

# Another Dictionary
Nusrat = {
    "Nusrat": {
        "name": "Nusrat Rahman",
        "Age": 21,
        "Location": "Bibir Hat",
        "Relationship": "Marred"
    },
}
Nusrat.update({"Nusrat": "Nusrat Rahman is Shanto Girlfriend"})
print(Nusrat)

print("\n")
# Python - Add Dictionary Items
# Dictionary Create
# Adding Items
Lina = {
    "name": "Mehran Lina",
    "age": 28,
    "gender": "Female",
    "location": "Dhaka,Bangladesh"
}
Lina["Work"] = "Masters Student"
print(Lina)

# Update Dictionary
Ontu = {
    "name": "Nafiza Naznin Antu",
    "age": 23,
    "location": "United Kingdom London",
    "work": "Student",
    "relationship": "Single"
}
Ontu.update({"relationship": "In a Relationship"})
print(Ontu)

print("\n")
# Python - Remove Dictionary Items
# Removing Items for Usg Pop Method
Arisha = {
    "name": "Arisha Jannat",
    "age": 19,
    "work": "Student",
    "color": "white"
}
Arisha.pop("color")
print(Arisha)

print("\n")
# Python - Remove Dictionary Items
# Removing Items for Usg Popitem Method
# Popitem remove the last insert Data Automatically
Ariyana = {
    "name": "Ariyanan Chowdury",
    "age": 22,
    "work": "Medical Student",
    "color": "Brown"
}
Ariyana.popitem()
print(Ariyana)

print("\n")
# Python - Remove Dictionary Items
# Removing Items for Usg Del Method
# Del Keyword deleted the specified key Removing
Anon = {
    "name": "Anon Rahaman",
    "age": 25,
    "work": "CSE Student",
    "color": "Darkish"
}
del Anon["color"]
print(Anon)

"""
print("\n")
# Python - Remove Dictionary Items
# Removing Items Del Method
# Del Keword Usg for Deleted Dictionary Full
Fahima = {
    "name" : "Fahima Houqe",
    "age" : 24,
    "work" : "EEE Student",
    "color" : "Queen"
}
del Fahima
print(Fahima)
"""

print("\n")
# Clear Method Usg and Deleted the Full Dictionary Remove
# clear()_ method Usg the Deleted for the Fully Dictionarys
# clear() Method
Eti = {
    "name": "Eti Hassan",
    "age": 25,
    "work": "Pharmacy Student",
    "color": "Beautiful"
}
Eti.clear()
print(Eti)

print("\n")
# Python - Loop Dictionaries _Practice Here.....
# Loop Through a Dictionary
SanjidaDictionary = {
    "name": "Sanjida",
    "gender": "Female",
    "age": 25
}
# for loop
# Print all key names in the dictionary, one by one:
for x in SanjidaDictionary:
    print(SanjidaDictionary)

print("\n")
# Print all values in the dictionary, one by one:
for x in SanjidaDictionary:
    print(SanjidaDictionary[x])

print("\n")
# You can also use the values() method to return values of a dictionary:
for x in SanjidaDictionary.values():
    print(x)

print("\n")
# You can use the keys() method to return the keys of a dictionary:
# Looping for the Key Dictionary's
# Only Key showing not showing values
for x in SanjidaDictionary.keys():
    print(x)

print("\n")
# Loop through both keys and values, by using the items() method:
# key + value pair একসাথে দেয়
# Key value out put dey for Dictionary

"""
সহজ ভাষায়:
items() = key + value একসাথে দেয়
for x, y = key আর value আলাদা করে নেয়
print(x, y) = দুটোই দেখায়
"""
for x, y in SanjidaDictionary.items():
    print(x, y)


# Python - Copy Dictionaries ( Date : 26-03-2026 )
# Copy a Dictionary
# Copy() Method Usg
print("\n")
muniya = {
    "name" : "Muniya",
    "age" : 21,
    "work" : "Student"
}
print(muniya)
myDic = muniya.copy()
print(myDic)

# dict() Method usg for the Copy
print("\n")
x = dict(muniya)
print(x)

# Python - Nested Dictionaries
print("\n")

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# Access Items in Nested Dictionaries Example
print(myfamily["child3"]["year"])

# Python Dictionary Methods

# clear() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

# copy() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

# fromkeys() Method

# get() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

# items() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)

# keys() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

# pop() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

# popitem() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

# setdefault() Method

# update() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

# values() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

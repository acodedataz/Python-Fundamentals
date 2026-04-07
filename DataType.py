# Python Total DataType Script

# Int Type Data
shanto = 21030
print(type(shanto))
print(shanto)

# Floating Type Data in Python
samiya = 10.25
print(type(samiya))
print(samiya)

# Complex Type Data in Python
munni = 400j
print(type(munni))
print(munni)

# Strig Type Data in Python
yourName = "Rahatul Hossen Shanto"
print(type(yourName))
print(yourName)

# String Type Data in Python
SamiyaBeautiful = "My Name is Shanto,"
shipa = " Shipa My Girlfriend"
print((SamiyaBeautiful + shipa))
print(type(SamiyaBeautiful))

# String Type Data
name = "Samiya"
print("My Love and " + name + " She Live in Always My Hearts.")

# Boolean Type Data in Python
sanjida = True
print(type(sanjida))
print(sanjida)

# Boolean Type Data in Python
Saniya = False
print(type(Saniya))
print(Saniya)

# Boolean Type Data in Python
SamiySultana = 40
MunniAktar = 40
print(SamiySultana > MunniAktar)
print(SamiySultana < MunniAktar)
print(SamiySultana == MunniAktar)

# String Formatting Data System
Number = 99
RollNumber = 88
GfName = "Sadiya Islam Borsha"
MyName = 'Rahatul Hossen Shanto'
MyDefferMent = 'AI/ML'
MyDefRollCSE = 92
UniversityName = 'University Of LuxemBarge'
print(f"This is My Super Number {Number}")
print(f"This is My Roll Number {RollNumber}")
print(f"My Girlfriend Name is {GfName} She is Most Beautiful Girls in Collage.")
print(f"My Name : {MyName} \nMy Group : "
      f"{MyDefferMent} \nMy DefRoll CSE : {MyDefRollCSE}\nMy University Name: {UniversityName}")

# Binary Data Type in Python------(Day-05)

# bytes
shantoList = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 25, 45, 255]
b = bytes(shantoList)  # List Converting in the (bytes)
print(type(b))  # bytes not updated mean Immutable

# bytesarray
samiyaList = [0, 50, 21, 25, 14, 25, 55, 65, 255]
sam = bytearray(samiyaList)  # List Convert in the (bytearray)
sam[1] = 100
print(sam[1])  # bytesarray updated mean Mutable

# BytesArry
b = [10, 20, 60, 40, 50, 60, 70, 80, 90]
c = bytearray(b)
print(type(c))

# None Type Data in Python
x = None
print(x)
print(type(x))

# Sequence Type Data

# List Type Data
listBr = ["shanto", "mobarak", 80, "rakib", "sushanto"]
listBr[1] = "Samiya Sultana"
listBr[3] = "Munni Aktar"  # List Type Data Alwys Updated and Mutable men Updated
print(listBr)
print(type(listBr))

# Tuple Type Data
tupleBr = ("apple", "vivo", "samsung", "banana")
print(tupleBr)  # Tuple Type data is Not A Updated this is Immutable Data
print(type(tupleBr))

# Range Type Data
ranData = range(6)
for i in ranData:
    print(i)

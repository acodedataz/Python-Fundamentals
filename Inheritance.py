# Python Inheritance Practice ---> Python OOP Based Practice

# main Parent Class Created
class myFather():
    car_1 = "Ferrari SF90 Stradale"
    car_2 = "BMW M5 Competition"
    car_3 = "Mercedes-Benz S-Class"
    bank_balance = "500 Cr"
    location = "New Yourk-USA"


# child Class Created
class Shanto(myFather):  # myFather---parent class inherit :
    phone = "I Phone 16pro Max"
    clock = "Alpha 7 Generation Clock"


# another child class
class Mehek(Shanto):  # multiple inheritance
    tablet = "I Pad"
    location_mehek = "Mosscow,Russia"


# Object Created Child Class ----> Shanto()
s = Shanto()  # first Object
print("Shanto Collecting her Father Bank Balance")
print(s.phone)
print(s.clock)
print(s.car_1)
print(s.car_2)
print(s.car_3)
print(s.location)
print(s.bank_balance)

print("\n")

# another object created seam blueprint
w = Mehek()
print(w.car_1)  # myFather
print(w.location_mehek)  # own
print(w.bank_balance)  # myFather
print(w.clock)  # Shanto

print("\n")


# Python Multiple Inheritance Practice System :
# Python Multiple Inheritance Property Access System
# Date : 05-04-2026 | 10:46 AM
# Practice By : Rahatul Hossen Shanto
# (Machine Learning and Deep Learning Research Student)
# I'm not CSE Student : I'm BSS Student

# parent class 01
class Father_One():
    phone = "Nokia"
    television = "BTV"
    car = "BMW-ZX2 Class"


# parent class 02
class Father_Two():
    bike = "Hero Rx100"
    ball = "Football"
    electricity = "Solar System"


# parent class 03
class Father_Three():
    pc = "High Quality PC"
    private_zet = "Air Zx2000 hrs"
    tv = "Sumsung Smart TV"


# child Class Created
class Soon_Child_Class(Father_One, Father_Two, Father_Three):
    mobile = "Vivo V21"
    year_phone = "Xiomi Airbus"


# child Object Created and Access the All Multiple Inheritance Class Property :
soon_Object = Soon_Child_Class()
print(soon_Object.car)  # Father one property
print(soon_Object.bike)  # Father two property
print(soon_Object.private_zet)  # Father three property


# Python Multilevel Inheritance Practice System :
# Rahatul Hossen Shanto :

# Created Parent Class
class parent_Father():
    auto_Car = "Tesla GX200"
    auto_mobile = "Vivo Auto"


# Soon Class 01
class Soon_One(parent_Father):
    smart_phone = "Apple"
    smart_tv = "Vision Tv"


# Soon Class 02
class Soon_Two(Soon_One):
    new_car = "Mozila DX"
    new_cycle = "Ninja H2r"


# Soon Class 03
class Soon_Three(Soon_Two):
    nevrix_choice = "Arrr"
    showing_phonix = "BDI R3"

# This Data Transfering System Multilevel Inheritance System in Python
# Simple But Tricky and Wholesum.

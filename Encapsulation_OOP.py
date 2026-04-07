# Python Encapsulation Practice :
from pip._internal.operations import prepare


# class create
class Parent_Information:
    def __init__(self, Fathers_Name, Mothers_Name, Location):
        self.__Fathers_Name = Fathers_Name
        self.__Mothers_Name = Mothers_Name
        self.__Location = Location  # Under Score Usg __ Safe and Encapsulation


parent_Info = Parent_Information("Mohammad Monir", "Sirin Aktar", "Alexander")


# parent_Info.Fathers_Name = "MD. Monir Hossen" Under Score not usg all time updated value
# public access in all value But if you (__MothersName) Under Score usg and You safe your data


# Encapsulation Another Practice Here.................
# Python OOP Encapsulation Practice

# public class created
class Shanto_Information():
    name = "Rahatul Hossen Shanto"
    __age = "18+"
    __phone = "01609526234"
    __email = "Datafile88@Gmail.Com"


S1 = Shanto_Information()
print(S1.name)
# print(S1.age) Not Access for private value Encapsulation
# print(S1.email) Not Access for private value Encapsulation
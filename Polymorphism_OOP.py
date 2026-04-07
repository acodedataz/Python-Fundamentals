# Python Polymorphism Practice :
# Simple Example in Polymorphism
# Abstraction Example Big Project Build korte hove tai Skipped.

# parent class create : Blueprint
class Vehicle:
    #constructor
    def __init__(self,Brand,Model,Price,Color):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
        self.Color = Color

class AroPlane(Vehicle):
    pass

class Car(AroPlane):
    pass

# One Blue Print usg and Build other System
P1 = AroPlane("Air American","X500GPrivate","100cr","Blue")
C1 = Car("Mercedes","E Classic","4cr","White")
print(P1.Model,P1.Brand,P1.Color,P1.Price)
print(C1.Model,C1.Brand,C1.Color,C1.Price)

# Noted : One BluePrint usg then Your Project Code Reuse System Build Etc.

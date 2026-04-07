# Python OOP Three Method Explained :

# class created
class Class_Name:
    # instance Method
    def Instance_Method(self):
        print("Hello! This is Instance Method")

    # class Method
    @classmethod
    def Class_Method(cls):
        print("Hello! This is Class Method")

    # static Method
    @staticmethod
    def Static_Method():
        print("Hello! This is Static Method")


class_Object = Class_Name()  # class_object_created

class_Object.Instance_Method()  # instance_method
class_Object.Class_Method()  # class_method
class_Object.Static_Method()  # static_method

# Noted : Class_Name - usg then
# Solid Working Method : Class_Method : Static_Method

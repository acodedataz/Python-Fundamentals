# Python Scope Practice

# Global Variable
a = 10
b = 20

# Function
def myLocalVariabel():
    p = 500 # local variable
    q = 300 # local variable
    print(p,q)
myLocalVariabel()


# Function Create
def my_Love():
    global a  # Global keyword then global variable value chaged
    a = 999  # Old value --> Global = 10, Now global keyword usg then value 999
    print(a)
    x = 200  # Local Variable
    y = 300  # Local Variable
    print(x + y)


# Method Calling
my_Love()

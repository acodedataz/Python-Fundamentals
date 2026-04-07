# Python Recursion Practice in IDE

"""
# Recursion Method Created
def myRecursion():
    print("Hello Recursion!")
    myRecursion()

# Called Recursion Method
myRecursion()
"""

# Recursion Documentation : Recursion Limited : 1000 Infinity
# This class Checking for Recursion Limited
# Simple and Basic Example in Recursion

# Noted : [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


print("\n")
# Another Example in Recursion in Python
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)
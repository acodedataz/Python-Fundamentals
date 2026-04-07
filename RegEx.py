import re

# Python Regular Expression : Practice in IDE
# Rahatul Hossen Shanto

# First Regular Expression Example Practice
text = "Hello,My Name Is Rahatul Hossen Shanto"
pattern = "[a-z]"
a = re.findall(pattern, text)
print(a)

print("\n")

# Another Practice in Regular Expression in Python
text_vat = "Jui is My X Girlfriend Collage"
pattern_ex = "^Jui"  # Pattern is Main Filter
x = re.findall(pattern_ex, text_vat)
if x:
    print("Yes! Jui is My Girlfriend")
else:
    print("No! Jui is Chapri")

print("\n")

# Another Regular Expression Practice in Python Language
text_is = "Hello Samiya Sultana"
pattern_is = "Sultana$"  # Pattern is Main Filter
expression = re.findall(pattern_is, text_is)
if expression:
    print("Samiya is My Real Girlfriend! TRUE!!")
else:
    print("I'm Single Person!! YES")

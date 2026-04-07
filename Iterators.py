# Python Iterators
list = ["Shanto","Munni","Shipa",20,25,10]
for x in list:
    print(x)

print("\n")

# Another List Created
Samiy_List = ["Borsha","Sadiya","Adri",502,227,884]
# List to Iterated
S = iter(Samiy_List)
print(S)

# Noted : output : <list_iterator object at 0x000001FF22D905E0>

print("\n")

# Another System Practice
Muniya_Lists = ["Fahmida","Mushfiqa","Fariha",25,14,78]
# list to converting iterated
M = iter(Muniya_Lists)

# print showing
print(next(M))
print(next(M))
print(next(M))
print(next(M))

# Iterator Concept Most Amazing Concept : Lazy Loading - ProgreesBar
#তুমি এখন OOP শিখতেছো —
# এই iterator concept টা পরে generator,
# custom class, lazy loading সব জায়গায় লাগবে 🔥
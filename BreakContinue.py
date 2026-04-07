# Python Break and Continue Practice

# Example in Break Statement
Sanjida = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(len(Sanjida)):
    if x == 6:
        break
    print(x)

print("\n")
# Example in Continue
Tamima = ["Sadiya", "Albi", "fahmida"]
for p in Tamima:
    if p == "Albi":
        continue
    print(p)

print("\n")

# Final Example Break & Continue in List Python
Muniya = ["Samiya", "Fariha", "Munni", "Dola", "Nusrat","Jui"]
for w in Muniya:
    if w == "Dola":
        #break  # ---> Break Statement code off
        continue    # ---> Continue Statement Skipped the Item
    print(w)

# Python File Handle Section Practice
# this class now - Python File Open

# Python File Open
# txt file open code here
file = open("MyPlan.txt", "r")
print(file.read())


# Python File Write Code Here...
# j kono type file created or write kora code here
# exsting file k wirte korte hole "a" diye korte hove nahoy age write kora
# line chole jabee "w" diyee korte gele

create_file = open("Plan.html","a")
create_file.write("Hello Shanto\n")

# Another practice
# Python Delete File Practice
# Delete a File practice
import os
if os.path.exists("Plan.html"):
  os.remove("Plan.html")
else:
  print("The file does not exist")

# Another Practice
# Python Delete File Practice
# Delete a Folder
os.rmdir("Shanto")  # just os.rmdir("and_Folder_name")





#program to check if a name is in a predefined list
l=["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna", "Ginny", "Fred", "George", "Bellatrix"]
name=input("Enter a name: ")
if (name in l):
    print("The name is in the list.")
else:
    print("The name is not in the list.")
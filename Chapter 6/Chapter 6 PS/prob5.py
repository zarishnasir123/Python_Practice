#program to findout wether a given name is present in list or not

names = ["Zarish", "Samavia", "Omer"]


input = input("Enter your name: ")

if(input in names):
    print("Your name is in the list")

else:
    print("your name is not in the list")
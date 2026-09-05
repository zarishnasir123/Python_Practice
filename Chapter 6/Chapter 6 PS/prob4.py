#write a program to find that wether a give user name contains less than 10 characters or not

name = input("Enter your username: ")

if(len(name)<10):
    print("Yes your username contains less than 10 alphabets.")

else:
    print("username is too long")
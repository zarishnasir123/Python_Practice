a = int(input("Enter your age: "))

if(a%2==0):  #independent if statement (1)
    print("Your age is even.")

#end of independent if statement (1)

# Dependent if-elif-else statement (2)
if(a>=18):
    print("You are eligible to vote.")
elif(a<0):
    print("Invalid age entered.")
elif(a==0):
    print("Age cannot be zero.")
else:
    print("You are not eligible to vote.")

#end of dependent if-elif-else statement (2)

print("Thank you for using the program.")
#write a program using functions to find the greatest of three numbers
def greatest(a,b, c):
    if(a>b and b>c):
        return a
    elif(b>a and a>c):
        return b
    else:
        return c
        
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

print("The greatest number is: ",greatest(a,b,c))
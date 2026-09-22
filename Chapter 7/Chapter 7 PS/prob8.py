#write a program to print the following star pattern

'''

for n = 3

*
**
***

'''

n = int(input("enter a number: "))

for row in range(1, n+1):
    
    for star in range(2*row - 1):
        print("*", end="")
        
    print()

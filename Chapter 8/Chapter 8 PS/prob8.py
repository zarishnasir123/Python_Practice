#write a  python function to print the multiplication table of a given number

def multiplication_table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

n = int(input("Enter a number: "))
multiplication_table(n)

# 3. Write a list comprehension to print a list which contains the multiplication
#    table of a user entered number.

num = int(input("Enter a number: "))

list = []

for i in range(1,11):
    list.append(num*i)

print(list)


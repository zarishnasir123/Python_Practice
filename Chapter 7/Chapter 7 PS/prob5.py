# Sum of numbers using while loop

n = int(input("Enter a number: "))

total = 0
i = 0

while i <= n:
    total = total + i
    i = i + 1

print("The sum is:", total)
#write a recursive function to calculate the sum of first n natural numbers

def calculate_sum(n):
    if n == 1:
        return 1
    else:
        return n + calculate_sum(n-1)

n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is", calculate_sum(n))

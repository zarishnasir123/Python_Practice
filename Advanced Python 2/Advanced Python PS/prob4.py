# write a program to filter a list of numbers using filter method which are divisible by 5

def divisble_by_five(n):
    if(n%2==0):
        return True
    else:
        return False
    
a = [10,20,78,98,9,17,88]

f = list(filter(divisble_by_five,a))

print(f)
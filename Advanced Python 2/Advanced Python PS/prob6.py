# write a program to find the maximum of numbers in a list using reduce function

from functools import reduce

def max_num(a,b):
    if a>b:
        return a
    else:
        return b

lst = [1,2,3,4,5,6,7,8,9,10]
print(reduce(max_num,lst))

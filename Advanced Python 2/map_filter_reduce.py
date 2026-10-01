from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y : x+y, numbers)
print(sum)

numbers = [1,2,3,4,5]

square = list(map(lambda x : x*2, numbers))

print(square)


#filter
numbers = [1,2,3,4,5,6,7,8,9,10]

odd = list(filter(lambda x : x%2 !=0, numbers))
print(odd)


#reduce
numbers = [1,2,3,4,5]

sum = reduce(lambda x,y : x+y, numbers)
print(sum)


# calculating maximum value with reduce

numbers = [45, 12, 89, 34, 10000]

max_num = reduce(lambda a, b: a if a > b else b, numbers)

print(max_num)  # Output: 89
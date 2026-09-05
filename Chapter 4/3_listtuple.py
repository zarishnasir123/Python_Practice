a = ("Apple" , "Orange", 5, 345.06, False, "Zarish", "Ahmed")

print(type(a))  #outputs the type of the variable

# a = (1,)
# print(type(a))  #outputs the type of the variable

# Packing
point = (10, 20, 30)

# Unpacking
x, y, z = point
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30

tup = (5, 10, 15, 10)
print(tup.count(10) + tup.index(15))

# Tuple containing a list
data = ("Ali", [10, 20, 30])

# Modify the internal list
data[1][0] = 99

print(data)  # Output: ('Ali', [99, 20, 30])
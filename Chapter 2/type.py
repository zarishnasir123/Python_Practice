# Converting String to Integer
num_str = "100"
num_int = int(num_str)
print(num_int + 5)    # Output: 105

# Converting Integer to Float
x = 5
x_float = float(x)
print(x_float)        # Output: 5.0

# Converting Integer to String
age = 25
age_str = str(age)
print("I am " + age_str + " years old.")  # Output: I am 25 years old.


#implicit type conversion
x = 10    # int
y = 2.5   # float

# Python ne 'x' ko automatically float (10.0) me badal diya taake answer 12.5 aaye
result = x + y  

print(result)        # Output: 12.5
print(type(result))  # Output: <class 'float'>

# Explicit type conversion
# String to Integer
num_str = "50"
num_int = int(num_str)  # Manual conversion

print(num_int + 10)     # Output: 60

# Float to Integer (Decimal point khatam ho jata hai)
price = 99.99
price_int = int(price)  # Manual conversion

print(price_int)        # Output: 99
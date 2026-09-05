a =1      #integer variable

b=5.22    #float variable

c="Harry"  #string variable

d = False  #boolean variable

e = None   #e is a none type variable


# 1. Arithmetic Operators
a, b = 10, 3
print("--- Arithmetic Operators ---")
print("Addition (10 + 3):", a + b)
print("Subtraction (10 - 3):", a - b)
print("Multiplication (10 * 3):", a * b)
print("Division (10 / 3):", a / b)
print("Modulus / Remainder (10 % 3):", a % b)
print("Exponent / Power (10 ** 3):", a ** b)
print("Floor Division (10 // 3):", a // b)

# 2. Comparison Operators
print("\n--- Comparison Operators ---")
print("Is 10 equal to 3? (10 == 3):", a == b)
print("Is 10 not equal to 3? (10 != 3):", a != b)
print("Is 10 greater than 3? (10 > 3):", a > b)
print("Is 10 less than 3? (10 < 3):", a < b)

# 3. Logical Operators
x, y = True, False
print("\n--- Logical Operators ---")
print("True AND False:", x and y)
print("True OR False:", x or y)
print("NOT True:", not x)

# 4. Assignment Operators
num = 5
print("\n--- Assignment Operators ---")
print("Initial value:", num)
num += 3  # Same as num = num + 3
print("After num += 3:", num)
num *= 2  # Same as num = num * 2
print("After num *= 2:", num)

# 5. Membership Operators
fruits = ["apple", "banana", "cherry"]
print("\n--- Membership Operators ---")
print("Is 'apple' in fruits?:", "apple" in fruits)
print("Is 'mango' NOT in fruits?:", "mango" not in fruits)
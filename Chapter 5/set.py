my_set = {10, 20, 30}
my_set.add(20)
my_set.discard(40)

print(len(my_set))

fruits = {"apple", "banana"}

# Adding
fruits.add("cherry")
fruits.update(["date", "elderberry"])

# Removing
fruits.remove("apple")      # Removes 'apple'
fruits.discard("mango")     # Does nothing (no error!)

print(fruits)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (Combines all unique elements from both sets)
print(a | b)             # Output: {1, 2, 3, 4, 5, 6}
print(a.union(b))

# Intersection (Elements present in BOTH sets)
print(a & b)             # Output: {3, 4}
print(a.intersection(b))

# Difference (Elements in 'a' but NOT in 'b')
print(a - b)             # Output: {1, 2}
print(a.difference(b))

# Symmetric Difference (Elements in either set, but NOT in both)
print(a ^ b)             # Output: {1, 2, 5, 6}
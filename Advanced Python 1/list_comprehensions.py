# Basic Syntax

# [expression for item in iterable if condition]

# squares = []
# for x in range(1, 6):
#     squares.append(x ** 2)

# print(squares)  # Output: [1, 4, 9, 16, 25]

squares = [x ** 2 for x in range(1, 6)]

print(squares)  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]

labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(labels)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
# fruits = ["apple", "banana", "cherry"]

# for i in range(len(fruits)):
#     print(i, fruits[i])

fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry


items = ["Task 1", "Task 2", "Task 3"]

for count, item in enumerate(items, start=1):
    print(f"{count}. {item}")

# Output:
# 1. Task 1
# 2. Task 2
# 3. Task 3
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}  # 'b' key dono mein common hai

# Merge operation
merged_dict = dict1 | dict2

print(merged_dict)  # Output: {'a': 1, 'b': 20, 'c': 3}
print(dict1)        # Output: {'a': 1, 'b': 2} (Original change nahi hua)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}

# In-place Update
dict1 |= dict2

print(dict1)  # Output: {'a': 1, 'b': 20, 'c': 3} (dict1 khud modify ho gayi)
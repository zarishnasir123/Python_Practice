def greet(name="Guest", message="Welcome"):
    print(f"Hello {name}, {message}!")

# 1. Using both defaults
greet()                    # Output: Hello Guest, Welcome!

# 2. Overriding the first default
greet("Ali")               # Output: Hello Ali, Welcome!

# 3. Overriding both defaults
greet("Sara", "Good day")  # Output: Hello Sara, Good day!
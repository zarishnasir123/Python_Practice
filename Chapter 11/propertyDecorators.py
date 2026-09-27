# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.full_name = f"{first_name} {last_name}" # Normal variable

# p = Person("Rahul", "Sharma")
# print(p.full_name) # Output: Rahul Sharma

# # Problem:
# p.first_name = "Amit"
# print(p.full_name) # Output: Rahul Sharma ❌ (Data Out of Sync!)

# The `@property` decorator allows you to access a method like a regular attribute without using parentheses `()`,
# while keeping control over getting and setting its value.

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # 1. GETTER: Automatically combine default first & last name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # 2. SETTER: Automatically split full_name into first & last name
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last
        
        # 3. If we don't have this setter, we can't set full_name like this:
        # p.full_name = "Amit Sharma"
        # 4. We can't set full_name like this either:
        # p.full_name("Amit Sharma")
        

p = Person("Rahul", "Sharma")

# 1. Accessing like a variable (No brackets needed!)
print(p.full_name)  # Output: Rahul Sharma

# 2. First name change karne par full_name apne aap update hoga
p.first_name = "Amit"
print(p.full_name)  # Output: Amit Sharma

# 3. Direct full_name change karne par setter first aur last name split kar dega
p.full_name = "Rohan Verma"
print(p.first_name) # Output: Rohan
print(p.last_name)  # Output: Verma
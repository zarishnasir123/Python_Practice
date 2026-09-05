# name = input("Enter your name: ")

# # print("Good Afternoon " +name)

# print(f"Good Afternoon {name}")  # Using f-string for formatted output


letter = '''Dear <Name>,
You are selected!
<Date> '''

print(letter.replace("<Name>", "Zarish").replace("<Date>", "6th June 2026"))  # Replacing placeholders with actual values


text = "I#love#Java!"

print(text.replace("#", " ").replace("Java", "Python"))  # Replacing '#' with space and 'Java' with 'Python'


phone = "+91 (123)-456-7890"

print(phone.replace("+91", "0").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))  # Formatting phone number

msg = "a-b-c"
result = msg.replace("-", "*").replace("*", "!")
print(result)   #output would be a!b!c



# name = "I love  Java!   "
# print(name.find("Jav"))


# name = "I love  Java!   "
# print(name.replace("  ", " "))


letter = "Dear Zarish,\n\tThis python course is nice.\n Thanks!"
print(letter)
friends = {}

name = input("Enter your name: ")
lang = input("Enter your favorite programming language: ")

name1 = input("Enter your name: ")
lang1 = input("Enter your favorite programming language: ")

name2 = input("Enter your name: ")
lang2 = input("Enter your favorite programming language: ")

name3 = input("Enter your name: ")
lang3 = input("Enter your favorite programming language: ")

friends[name] = lang
friends[name1] = lang1
friends[name2] = lang2
friends[name3] = lang3

print(friends)  

print(type(friends))  # Output: <class 'dict'>, because {} creates an empty dictionary, not a set.
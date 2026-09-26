# 1. Create a class "Programmer" for storing information of few programmers
#    working at Microsoft.


class Programmer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
        
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Language: ", self.language)


p1 = Programmer("John", 25, "Python")
p1.display()

p2 = Programmer("Mike", 30, "Java")
p2.display()

p3 = Programmer("Sam", 28, "C++")
p3.display()
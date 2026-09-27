# 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog'
#    from 'Pets'. Add a method 'bark' to class 'Dog'.

class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
class Pets(Animals):
    def __init__(self, name, age, pet_type):
        super().__init__(name, age)
        self.pet_type = pet_type

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Pet Type: {self.pet_type}")
        

class Dog(Pets):
    def bark(self):
        print(f"{self.name} is barking")
        

dog = Dog("Buddy", 3, "Dog")
dog.display()

dog.bark()
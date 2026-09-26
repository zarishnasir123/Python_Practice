# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, roll):
#         self.name = name      # ye line Person me already likhi hai
#         self.age = age        # ye bhi Person me already likhi hai
#         self.roll = roll      # sirf ye nayi cheez hai


# super() lets a child class call a method from its parent class. It's mostly used inside __init__, so the child can reuse the parent's setup code instead of writing it again.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno
        
        
s = Student("Ali", 20, 101)
print(s.name, s.age, s.rollno)
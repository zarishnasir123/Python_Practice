# 4. Add a static method in problem 2, to greet the user with hello.

# 2. Write a class "calculator" capable of finding square, cube and square root
#    of a number.

class Calculator:
    def __init__(self):
        self.number = 0
        
        
    @staticmethod
    def greet():
        print("Hello user")

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5

    def set_number(self, number):
        self.number = number
        

calc = Calculator()
Calculator.greet()
calc.set_number(4)
print(calc.square())
print(calc.cube())
print(calc.square_root())
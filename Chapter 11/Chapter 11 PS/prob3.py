# 3. Create a class 'Employee' and add salary and increment properties to it.
#    Write a method 'salaryAfterIncrement' method with a @property decorator with
#    a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = (value - self.salary) / self.salary
        
e1 = Employee(50000, 0.1)
print(e1.salaryAfterIncrement)
e1.salaryAfterIncrement = 60000
print(e1.salaryAfterIncrement)

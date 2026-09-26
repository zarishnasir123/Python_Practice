# Level 1 (Grandparent)
class Employee:
    def work(self):
        print("Employee: I come to the office")


# Level 2 (Parent) inherits from Employee
class Programmer(Employee):
    def code(self):
        print("Programmer: I write code")


# Level 3 (Child) inherits from Programmer
# (and so it ALSO gets everything from Employee)
class SeniorProgrammer(Programmer):
    def guide(self):
        print("Senior: I guide junior programmers")


s = SeniorProgrammer()

s.guide()     # SeniorProgrammer's own method
s.code()      # came from Programmer (1 level up)
s.work()      # came from Employee (2 levels up)
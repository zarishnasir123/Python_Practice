class Employee:                          # Parent class
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")


class Programmer(Employee):              # Child class inherits from Employee
    def __init__(self, name, salary, language):
        super().__init__(name, salary)   # reuse Employee's __init__
        self.language = language         # new attribute only Programmer has

    def showLanguage(self):              # new method only Programmer has
        print(f"{self.name} codes in {self.language}")


e = Employee("Ali", 40000)
p = Programmer("Noree", 60000, "Python")

e.showDetails()
print()

p.showDetails()     # inherited from Employee
p.showLanguage()    # Programmer's own method
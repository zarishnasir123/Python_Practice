# Parent 1
class Employee:
    company = "Microsoft"          # every Employee works at Microsoft

    def work(self):
        print("I work at", self.company)


# Parent 2
class Coder:
    language = "Python"            # every Coder knows Python

    def code(self):
        print("I write code in", self.language)


# Child inherits from BOTH parents (separated by a comma)
class Programmer(Employee, Coder):
    def intro(self):
        print("I am a Programmer")


p = Programmer()

p.intro()     # Programmer's own method
p.work()      # came from Employee (parent 1)
p.code()      # came from Coder (parent 2)
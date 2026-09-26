class Employee:
    name = "Zarish"
    language = "Python"
    salary = 120000
    
zarish = Employee()    #this is an object/instance attribute
print(zarish.name, zarish.language)

    
khansa = Employee()
print(khansa.salary, khansa.language)


rohan = Employee()
rohan.name = "rohan ahmed jaleel"

print(rohan.name, rohan.language, rohan.salary)

# here name is object attribute and salary and language are class attributes as they directly belond to the class
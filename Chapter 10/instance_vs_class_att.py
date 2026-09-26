class Employee:
    language = "Python"
    salary = 120000
    
zarish = Employee()    #this is an object/instance attribute

zarish.name = "ZarishNasir"
zarish.language = "Java"
print(zarish.name, zarish.language,zarish.salary)  

#instance attributes take preference over class attributes

#if attribute is present in object then it will be used otherwise class attribute will be used


# here name is object attribute and salary and language are class attributes as they directly belond to the class
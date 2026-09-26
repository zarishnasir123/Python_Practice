class Employee:
    language = "Python"
    salary = 120000
    
    def __init__(self, name, language, salary):   #dunder method(starting with underscore) which is automatically called when an object is created
        self.name = name
        self.language = language
        self.salary = salary
        print("i am creating an object")
        
    
    def getInfo(self):
        print(f"the language is {self.language}. The salar is {self.salary}")
        
    @staticmethod       #doesnt take self 
    def greet():
        print("good morning")
        

zarish = Employee("zarish", "python", 12000)    
print(zarish.name, zarish.language, zarish.salary)
    
    
# zarish = Employee()  
# zarish.name = "Zarish Nasir"   #instead of doing this we can use a constructor
# print(zarish.name, zarish.language, zarish.salary)
# Employee.getInfo(zarish)

# zarish.greet()
# ahmed = Employee()   #init dunder method gets called whenever a new object is created
  
class Employee:
    language = "Python"
    salary = 120000
    
    def getInfo(self):
        print(f"the language is {self.language}. The salar is {self.salary}")
        
    @staticmethod       #doesnt take self 
    def greet():
        print("good morning")
        
    
zarish = Employee()  
Employee.getInfo(zarish)

zarish.greet()
  

# zarish.name = "ZarishNasir"
# zarish.language = "Java"
# print(zarish.name, zarish.language,zarish.salary)  
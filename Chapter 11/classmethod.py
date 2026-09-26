class Employee:
    a = 1
    
    @classmethod    #used to get attribute value from class even if an instance is created with some value 
    def show(cls):
        print(cls.a)
        


e = Employee()
e.a = 34   #it will show instance attrubute but what if i need the attribute value from class which is a=1 

      
e.show()

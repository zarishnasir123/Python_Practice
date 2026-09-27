# create a class 2d vector and use it to create another class representing a 3d vector

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")
    
class ThreeDVector(TwoDVector):
    def __init__(self, i,j,k):
       super().__init__(i,j)
       self.k = k
    
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")
    
o1 = TwoDVector(1,2)
o2 = ThreeDVector(1,2,3)
o1.show()
o2.show()
        


        
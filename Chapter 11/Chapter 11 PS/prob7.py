# 7. Override the __len__() method on vector of problem 5 to display the dimension
#    of the vector.

class Vector:
    def __init__(self, *args):
        self.vector = args

    def __add__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Both vectors must have the same dimension")
        return Vector(*[self.vector[i] + other.vector[i] for i in range(len(self.vector))])

    def __sub__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Both vectors must have the same dimension")

    def __len__(self):
        return len(self.vector)
    def __str__(self):
        return str(self.vector)
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(len(v1))
print(len(v2))
print(v1 + v2)
print(v1 - v2)
print(v1)

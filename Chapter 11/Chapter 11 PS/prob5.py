# 5. Write a class vector representing a vector of n dimensions. Overload the + and *
#    operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, *args):
        self.vector = args

    def __add__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must be of the same length")
        return Vector(*[a + b for a, b in zip(self.vector, other.vector)])

    def __mul__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must be of the same length")
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def __str__(self):
        return "Vector: " + str(self.vector)


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2
v4 = v1 * v2
print(v3)
print(v4)

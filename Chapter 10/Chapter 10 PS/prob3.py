# 3. Create a class with a class attribute a; create an object from it and set 'a'
#    directly using object.a = 0. Does this change the class attribute?

class MyClass:
    a = 1

obj = MyClass()
obj.a = 0

print(MyClass.a) # 1
print(obj.a) # 0

# no it does'nt change the class attribute
# 6. Can you change the self-parameter inside a class to something else (say
#    "zarish")? Try changing self to "slf" or "harry" and see the effects.

class Person:
    def __init__(zarish, name):
        zarish.name = name

    def greet(zarish):
        print("Hello, I am", zarish.name)

p = Person("Zarish")
p.greet()          # Hello, I am Zarish


# So should you? No. It's legal but nobody does it. Every Python programmer, every tutorial, and every linter expects self;
x = 10  # Global Variable

def update_x():
    global x  # Python ko bataya ki hum bahar wale 'x' ko use kar rahe hain
    x = 20    # Global x ki value change ho gayi

update_x()
print(x)  # Output: 20


#without global keyword

# x = 10  # Global Variable

# def update_x():
#     x = 20  # Python ise ek naya LOCAL variable maan lega, global x change nahi hoga!

# update_x()
# print(x)  # Output: 10 (Global x unchanged raha)
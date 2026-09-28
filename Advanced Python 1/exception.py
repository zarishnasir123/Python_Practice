try:
    a = int(input("hey, enter a number: "))
    print(a)
    
except Exception as e:
    print(e)
    
    
try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    # Runs ONLY if a ZeroDivisionError occurs
    print("Error: You cannot divide by zero!")
except ValueError:
    # Runs ONLY if user enters invalid input (e.g. text instead of a number)
    print("Error: Please enter a valid integer!")
else:
    # Runs ONLY if NO exception was raised in the try block
    print(f"Success! Result is {result}")
finally:
    # ALWAYS runs no matter what (used for cleanup like closing files/connections)
    print("Execution complete.")
    

#Good practice when exception name is specific
try:
    num = 10 / 0
except ZeroDivisionError:  # Pata hai exact error kya aa sakta hai
    print("Zero se divide mat karo!")    
    

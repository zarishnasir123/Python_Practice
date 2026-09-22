# write a python program using functions to convert celsius to fahrenheit 

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"The temperature in Fahrenheit is: {fahrenheit}")
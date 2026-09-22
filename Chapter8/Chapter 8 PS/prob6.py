#write a python function which converts inches to cms  

def convert_inches_to_cms(inches):
    return inches * 2.54

inches = float(input("Enter the value in inches: "))
cms = convert_inches_to_cms(inches)
print(f"{inches} inches is equal to {cms} cms")

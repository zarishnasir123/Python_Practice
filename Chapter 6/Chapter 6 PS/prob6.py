marks = int(input("Enter your marks: "))

if(marks>100):
    print("Marks can't be greater than 100")
else:
    if(marks>=90):
        grade = "Ex"

    elif(marks>=80):
        grade = "A"

    elif(marks>=70):
        grade = "B"

    elif(marks>=60):
        grade = "C"

    elif(marks>=50):
        grade = "D"

    else:
        grade = "E"

print("your grade is", grade)
    

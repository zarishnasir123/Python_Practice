marks = {
    "Harry" : 100,
    "Zarish" : 98,
    "Sam" : 9
}

print(marks, type(marks))

print(marks["Harry"])


# Empty dictionary
student = {}

# Dictionary with initial data
student = {
    "name": "Ali",
    "age": 21,
    "courses": ["Python", "Math"],
    "is_enrolled": True
}

student["age"] = 43

print(student)

print(student.items())

print(student.keys())

print(student.values())

student.update({"courses" : ["Java", "Math"], "is_enrolled" : False})

print(student)

remove_course = student.pop("courses")
print(remove_course)
print(student)

student.pop("age", None)
print(student)

student.popitem()
print(student)


info = {"name": "Zarish", "score": 85}
info["score"] = 90
info.update({"city": "Lahore"})
 
print(len(info))   #output: 3


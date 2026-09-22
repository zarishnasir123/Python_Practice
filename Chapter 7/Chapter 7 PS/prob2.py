# write a program to greet all the person names stored in a list "l" and which starts with letter 's' or 'S'

l = ["zarish", "saad", "shubham", "shivangi"]


for name in l:
    if(name.startswith("S") or name.startswith("s")):
        print("Hello " + name )



with open("file.txt") as f:
    f.read()
    print(f.read())
    

#you dont need to explicitly close the file
    
# This is equivalent to:
# f = open("file.txt")
# f.read()
# f.close()


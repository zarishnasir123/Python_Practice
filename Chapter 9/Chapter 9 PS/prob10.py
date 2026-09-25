# 10. Write a program to wipe out the content of a file using python.

def wipe_content():
    with open("test.txt", "w") as f:
        f.write("")
        
        
wipe_content()
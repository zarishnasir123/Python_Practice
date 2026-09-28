# 1. Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these
#    files are not present, a message without exiting the program must be printed
#    prompting the same.

def FilesOpen():
    try:
        f1 = open("1.txt", "r")
        f2 = open("2.txt", "r")
        f3 = open("3.txt", "r")
    except FileNotFoundError:
        print("File not found")
    else:
        print(f1.read())
        print(f2.read())
        print(f3.read())
        f1.close()
        f2.close()
        f3.close()
    
    
    finally:
        print("Program executed successfully")
        
FilesOpen()
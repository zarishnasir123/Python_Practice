# 9. Write a program to find out whether a file is identical & matches the content
#    of another file.

def compare_files(file1, file2):
    with open("file1.txt") as f:
        content1 = f.read()
    
    with open("file2.txt") as f:
        content2 = f.read()

    if content1 == content2:
        print("The files are identical.")
    else:
        print("The files are not identical.")
        
compare_files("file1.txt", "file2.txt")
            
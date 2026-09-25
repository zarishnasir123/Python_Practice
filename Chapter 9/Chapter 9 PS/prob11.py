# 11. Write a python program to rename a file to "renamed_by_python.txt".
import os

def rename_file():
    os.rename("rename.txt", "renamed_by_python.txt")
    
rename_file()
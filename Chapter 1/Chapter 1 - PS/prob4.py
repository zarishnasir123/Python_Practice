import os

# Specify the path ('.' means current directory)
path = "."

# Get the list of all files and directories
contents = os.listdir(path)

print(f"Contents of '{path}':")
for item in contents:
    print(item)
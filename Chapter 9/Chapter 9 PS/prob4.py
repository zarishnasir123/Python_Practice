# 4. A file contains a word "Donkey" multiple times. You need to write a program
#    which replaces this word with ##### by updating the same file.


def remove_donkey():
    with open('prob4.txt', 'r') as f:
        lines = f.readlines()
    with open('prob4.txt', 'w') as f:
        for line in lines:
            f.write(line.replace('Donkey', '#####'))
            
remove_donkey()
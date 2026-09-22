#write a python function to print first n lines of the following pattern

'''
***
**
*
'''



def pattern():
    n=int(input("Enter the number of lines: "))
    for i in range(n,0,-1):
        for j in range(i):
            print('*',end='')
        print()
        
pattern()
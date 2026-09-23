#how do u prevent a python print function to print a new line at the end

def print_no_newline(*args, **kwargs):
    kwargs['end'] = ''
    print(*args, **kwargs)
    
print_no_newline("Hello", "World")

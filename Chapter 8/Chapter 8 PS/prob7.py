#write a python function to remove a given word from a list and strip it at the same time   

def remove_word(word, list):
    list.remove(word)
    return list

list = ['hello', 'world', 'hello', 'python']
word = 'hello'
print(remove_word(word, list))

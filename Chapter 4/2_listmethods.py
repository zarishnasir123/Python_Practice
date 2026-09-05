friends = ["Apple" , "Orange", 5, 345.06, False, "Zarish", "Ahmed"]

print(friends)

friends.append("Noreen")  #adds an element to the end of the list
print(friends)

l1 = [900, 800, 544,99, 8093]
l1.sort()  #sorts the list in ascending order
print(l1)

l1.reverse()  #reverses the order of the list
print(l1)

l1.insert(0,10000)
print(l1)  #inserts an element at the specified index

print(l1.pop(2))  #removes the last element of the list
print(l1)

# l1.remove(800)  #removes the specified element from the list
# print(l1)

l1.extend([10,20,30,999999])  #adds multiple elements to the end of the list
print(l1)

# extend(iterable): Appends all items from another list (or any iterable like a tuple or set) to the current list.

print(l1.index(10000))  # finds the index of the first occurrence of an element in the list


print(l1.count(10))  #counts the number of occurrences of an element in the list

new_l1 = l1.copy()  #creates a shallow copy of the list
print(new_l1)
#break example

for num in range(20):
    if(num==6):
        break
    print(num)
    
# continue example

print("for loop with continue statement")
for num in range(20):
    if(num==6):    #skips 17
        continue    
    print(num)
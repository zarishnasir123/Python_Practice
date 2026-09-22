n = int(input("Enter the number: "))

if n < 2:
    print("this num is not prime")
    
else:
    for i in range(2, n):
        if n % i == 0:
            print("this num is not prime")
            break
    else:
        print("this num is prime")
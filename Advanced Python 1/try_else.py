def main():
    try:
        a = int(input("hey, enter a number: "))
        print(a)
    except Exception as e:
        print(e)
        return
    else:
        print("This is the else block")
    finally:
        print("This is the end of the program")

main()
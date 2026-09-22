import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

youDict = {"s": 1, "w": -1, "g": 0}
nameDict = {1: "Snake", -1: "Water", 0: "Gun"}

while True:

    # Computer randomly chooses
    computer = random.choice([1, -1, 0])

    youstr = input("Enter your choice (s,w,g): ")

    # Check invalid input
    if youstr not in youDict:
        print("Invalid input. Try Again")
        continue

    you = youDict[youstr]

    # Show choices
    print("You chose:", nameDict[you])
    print("Computer chose:", nameDict[computer])

    # Game logic
    if you == computer:
        print("It's a tie!")

    else:
        if you == 1 and computer == -1:
            print("You win!")

        elif you == -1 and computer == 1:
            print("You lose!")

        elif you == 0 and computer == 1:
            print("You win!")

        elif you == 1 and computer == 0:
            print("You lose!")

        elif you == -1 and computer == 0:
            print("You win!")

        elif you == 0 and computer == -1:
            print("You lose!")

    # Play again
    again = input("Do you want to play again? (y/n): ")

    if again == "n":
        print("Game Over!")
        break
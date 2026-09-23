# the game function in a program lets a user play a game and returns the score as an integer
#you need to read a file "Hi-score.txt" which is either blank or containts the previous
# Hi-Score. You need to write a program to update the hi-score whenever the game function breaks the Hi-score.

import random

def game():
    print("You're playing the game..")
    score = random.randint(1, 62)
    
    # Fetch the hiscore safely
    try:
        with open("Hi-score.txt", "r") as f:
            hiscore_str = f.read().strip()
            hiscore = int(hiscore_str) if hiscore_str else 0
    except FileNotFoundError:
        hiscore = 0

    print(f"Hi-Score: {hiscore}")
    print(f"Your Score: {score}")

    # Update the Hi-Score if the user beat it
    if score > hiscore:
        print("New High Score!")
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
    
    return score

game()
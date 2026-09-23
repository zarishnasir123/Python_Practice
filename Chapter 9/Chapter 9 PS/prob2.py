# the game function in a program lets a user play a game and returns the score as an integer
#you need to read a file "Hi-score.txt" which is either blank or containts the previous
# Hi-Score. You need to write a program to update the hi-score whenever the game function breaks the Hi-score.

import random

def game():
    print("You're playing the game..")
    score = random.randint(1, 62)
    
    # fetch the hiscore
    with open("Hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Hi-Score: {hiscore}")
    print(f"Your Score: {score}")

    # update the hiscore file if current score is higher
    if(score > hiscore):
        print("Congratulations! You broke the high score!")
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))

    return score

game()
import random

def game():
    print("you are playing the game..")
    score=random.randint(1,100) #generaing random number to compare with high score

    with open("highscore.txt") as f: #opening the file and reading to find out whether it is empty and updating the file content to integer value
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0

    print(f"yourscore={score}") #comparing the high score with the randomly generated number(score) and writing the value which is greater
    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))

    return score


game()
         
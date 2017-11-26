from  random import  randint
z = ["Rock","Paper","Scissor"]
score_p = 0
score_c = 0


def assign_player():
    global score_p
    global score_c
    computer = z[randint(0, 2)]
    print("Player Score: {}     Computer Score:{}\n".format(score_p,score_c))
    player = input("Chose one of the following: \nRock\nPaper\nScissor")
    if player == computer:
        print("Tie!!")

    elif player == "Rock":
        if computer == "Scissor":
            print("You win!!! player: {}  computer: {} \n".format(player,computer))
            score_p += 1

        else:
            print("You lose!!! player: {}  computer: {} \n".format(player,computer))
            score_c += 1

    elif player == "Paper":
        if computer == "Rock":
            print("You win!!! player: {}  computer: {} \n".format(player, computer))
            score_p += 1

        else:
            print("You lose!!! player: {}  computer: {} \n".format(player, computer))
            score_c += 1

    elif player == "Scissor":
        if computer == "Paper":
            print("You win!!! player: {}  computer: {} \n".format(player, computer))
            score_p += 1
        else:
            score_c += 1
            print("You lose!!! \n player: {}  computer: {} \n ".format(player, computer))

    else:
        print("That's not a valid play. Check your spelling!")

    cal_again()
    return score_c,score_p



def cal_again():
    chose = input("**PLAY AGAIN(Y for yes, N for No)**")
    if chose.upper() == "Y":
        assign_player()
    elif chose.upper() == "N":
        print("See you soon!")
    else:
        print("Invalid input!!")
        cal_again()



def welcome():

    print("************Welcome! Paper Scissor Rock game starting*************")


welcome()
assign_player()
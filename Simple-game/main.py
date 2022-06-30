from random import randint


print("Rock...".lower())
print("Paper...".lower())
print("Scissors...".lower())
print('------')


randomNumber = randint(0, 3)
computerMove = "rock"

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"



Player_1 = input("player_1, Make your move : ").lower() 
Player_2 = computerMove
print(f"player_2, Make your move : {computerMove}")


if Player_1 == Player_2:
    print("thats a tie ...")
elif Player_1 == "rock":
    if Player_2 == "scissors":
        print("player_1 wins!...")
    elif Player_2 == "paper":
        print("player_2 wins!....")
elif Player_1 == "paper":
    if Player_2 == "rock":
        print("player_1 wins!....")
    elif Player_2 == "scissors":
        print("player_1 wins!...")
elif Player_1 == "scissors":
    if Player_2 == "paper":
        print("player_1 wins!....")
    elif Player_2 == "rock":
        print("player_2 wins!....")
else:
    print("something went wrong ...")

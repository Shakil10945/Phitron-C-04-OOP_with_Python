player1= input()
player2= input()

if (player1 == "rock" and player2 =="scissor"):
    print("Player 1 is the winner")

elif(player1 == "paper" and player2 =="rock"):
    print("Player 1 is the winner")
elif(player1 == "paper" and player2 =="scissor"):
    print("Player 1 is the winner")
else:
    print("Player 2 is the winner")
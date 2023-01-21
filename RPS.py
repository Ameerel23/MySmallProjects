import random

rps = ['rock', 'paper', 'scissors']
player1 = input("Rock, paper, scissors? ")
rpsrand = random.choice(rps)

if (player1.lower() == 'rock' and rpsrand == 'scissors') or (player1.lower() == 'paper' and rpsrand == 'rock') or (player1.lower() == 'scissors' and rpsrand == 'paper'):
    print("Opponent: ", rpsrand)
    print("You: ", player1.lower())
    print("You win")


elif (player1.lower() == 'scissors' and rpsrand == 'rock') or (player1.lower() == 'rock' and rpsrand == 'paper') or (player1.lower() == 'paper' and rpsrand == 'scissors'):
    print("Opponent: ", rpsrand)
    print("You: ", player1.lower())
    print("You lose")

else:
    print("Opponent: ", rpsrand)
    print("You: ", player1.lower())
    print("Tie game")


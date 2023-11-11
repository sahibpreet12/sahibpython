import random

moves = ['rock', 'paper', 'scissors']

i = 0

while i <= 5:
    i += 1

    player_move = input("Enter your move (rock/paper/scissors): ")

    if player_move not in moves:
        print("Invalid move")
        break

    computer_move = random.choice(moves)

    print("You played:", player_move)

    print("Computer played:", computer_move)

    computer_wins = 0
    player_wins = 0

    if player_move == computer_move:
        print("It's a tie!")
    elif player_move == 'rock' and computer_move == 'scissors':
        print("You win!")
        player_wins += 1
    elif player_move == 'paper' and computer_move == 'rock':
        print("You win!")
        player_wins += 1
    elif player_move == 'scissors' and computer_move == 'paper':
        print("You win!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

if computer_wins > player_wins:
    print("Computer is the ultimate winner")
elif player_wins > computer_wins:
    print("You are the ultimate winner")
else:
    print("It is a total tie")
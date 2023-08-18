import random
def get_choices(): 
    player_choice = input("Enter a choice (rock, paper, or scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options) 
    choices = {"player": player_choice, "computer": computer_choice} 

    return choices


def check_win(player, computer):
    print(f"You choose {player}, The computer choose {computer}")
    if player == computer:
        return "Draw!"
    elif player == "rock":
        if computer == "scissors":
            return "player"
        else:
            return "computer"
    elif player == "paper":
        if computer == "rock":
            return "player"
        else:
            return "computer"
    elif player == "scissors":
        if computer == "paper":
            return "player"
        else:
            return "computer"

player_score = 0 
computer_score = 0 

for i in range(5):
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])

    if result == "player":
        player_score += 1
    elif result == "computer":
        computer_score += 1
    else:
        player_score += 0 
        computer_score += 0

if player_score > computer_score:
    print(f"Player wins! with {player_score} points")
elif player_score < computer_score:
    print(f"the CPU wins with {computer_score} points")
else:
    print(f"the game was a draw, with CPU having {computer_score} and the player having {player_score}")

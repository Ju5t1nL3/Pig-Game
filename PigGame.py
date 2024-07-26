"""
The program allows the user to play the standard dice game Pig
"""

import random

def roll(name,win):
    """
    Keeps rolling a dice until the user wins, the user rolls a 1, or the user chooses to stop
    """
    turn_score = 0
    cont_play = "y"
    while cont_play == "y":
        rolled = random.randint(1,6)
        if rolled == 1:
            turn_score = 0
            cont_play = "n"
            print(f"You rolled a {rolled}. Your turn ends.")
            break
        else:
            print(f"You rolled a {rolled}!")
            turn_score += rolled
            if turn_score + players_dict[name] >= win:
                print(f"Your current turn score is {turn_score}.")
                break
            while True:
                cont_play = input(f"Your current turn score is {turn_score}. Would you like to keep rolling? (Y/N): ").lower().strip()
                if cont_play == "y" or cont_play == "n":
                    break
                else:
                    print("That is not an accepted answer. Try again.")

    players_dict[name] += turn_score
    print(f"\nTotal Score: {players_dict[name]}\n")

def check_winner(name,win):
    """
    Checks if the user won
    """
    if players_dict[name] >= win:
        return True

def play_turn(name,win):
    """
    Plays out a singular turn for one person
    """
    roll(name,win)
    return check_winner(name,win)

def play(num_players,win):
    """
    Plays the entire game
    """
    for num in range(num_players):
        players_dict[f"Player {num + 1}"] = 0

    keep_play = True
    round = 0
    while keep_play:
        round += 1
        print(f"Round {round}\n")
        for name in players_dict:
            print(f"{name}'s Turn")
            if play_turn(name,win):
                keep_play = False
                print(f"The winner is {name}!\n")
                break
        output = ""
        print("Current Scores:")
        for index,(name,score) in enumerate(players_dict.items()):
            if index == 0:
                output += f"{name}: {score}"
            else:
                output += f" | {name}: {score}"
        print(f"{output}\n")


#Start program
players_dict = {}
try:
    players = int(input("How many players are there? ").strip())
except ValueError:
    print("Only integers are accepted. Try again.")
try:
    win = int(input("What score would you like to play to? ").strip())
except ValueError:
    print("Only integers are accepted. Try again.")

play(players,win)


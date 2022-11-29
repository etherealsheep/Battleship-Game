# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def number_turns():
    nTurns = [6, 7, 8]
    choice = random.choice(nTurns)
    return choice


def determine_attacker():
    player1 = ["Attacker", "Defender"]
    choice = random.choice(player1)
    return choice


number_of_turns = number_turns()
player_role = determine_attacker()


print(f"The battle will be {number_of_turns} long.")
print(f"Player 1 is the {player_role} and Player 2 is the {player_role}.")

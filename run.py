# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def number_turns():
    nTurns = [6, 7, 8]
    choice = random.choice(nTurns)
    return choice


number_of_turns = number_turns()


print(f"The battle will be {number_of_turns} long.")
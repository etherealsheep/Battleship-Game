# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import time


army_list = [
    "Empire",
    "Tomb Kings",
    "Chaos",
    "Orcs",
    "High Elves",
    "Dwarfs",
    "Skaven",
    "Lizardmen",
    "Bretonnia",
    "Kislev",
    "Dark Elves",
    "Daemons",
    "Araby",
    "Vampire Counts",
    "Dogs of War",
    "Ogre Kingdoms",
    "Albion",
    "Goblins",
    "Witch Hunters",
    "Chaos Dwarves",
    "Wood Elves",
    "Beastmen",
    "Norse"
]


def title():
    print("  _    _  ___ _________  ___ ___  _____ _____ ___________  ")
    print(" | |  | |/ _ \| ___ |  \/  |/ _ \/  ___|_   _|  ___| ___ \ ")
    print(" | |  | / /_\ | |_/ | .  . / /_\ \ `--.  | | | |__ | |_/ / ")
    print(" | |/\| |  _  |    /| |\/| |  _  |`--. \ | | |  __||    /  ")
    print(" \  /\  | | | | |\ \| |  | | | | /\__/ / | | | |___| |\ \  ")
    print("  \____/\___|_____\_____ __\_| _______/  \_/ \____/\_| \_| ")
    print(" | ___ \/ _ |_   _|_   _| |   |  ___|                      ")
    print(" | |_/ / /_\ \| |   | | | |   | |__                        ")
    print(" | ___ |  _  || |   | | | |   |  __|                       ")
    print(" | |_/ | | | || |   | | | |___| |___                       ")
    print(" \____/|_____||_| _ |_|_|_____|_____|_____ _____ _____     ")
    print(" |  __ |  ___| \ | |  ___| ___ \/ _ |_   _|  _  | ___ \    ")
    print(" | |  \| |__ |  \| | |__ | |_/ / /_\ \| | | | | | |_/ /    ")
    print(" | | __|  __|| . ` |  __||    /|  _  || | | | | |    /     ")
    print(" | |_\ | |___| |\  | |___| |\ \| | | || | \ \_/ | |\ \     ")
    print(" \____\____/\_| \_\____/\_| \_\_| |_/\_/  \___/\_| \_|     ")
    print("                                                           ")
    time.sleep(2)


title()


p1 = input("Please enter Player1 Army: \n").upper()
p2 = input("Please enter Player2 Army: \n").upper()
print(f"{p1} vs {p2}.")
time.sleep(2)


def determine_scenario():
    scenarios = [
        "TAKE AND HOLD",
        "BATTLE FOR THE TOWER",
        "DEFENDING THE VILLAGE",
        "VAGON TRAIN"
    ]
    scenario_choice = random.choice(scenarios)
    return scenario_choice


def number_turns():
    nTurns = [6, 7, 8]
    choice = random.choice(nTurns)
    return choice


def determine_attacker():
    player1 = ["Attacker", "Defender"]
    choice = random.choice(player1)
    return choice


scenario = determine_scenario()
number_of_turns = number_turns()
player_role = determine_attacker()


print(f"The battle between {p1} and {p2} will be: {scenario}. \n")
time.sleep(2)
print(f"The battle will end after {number_of_turns} turns. \n")
time.sleep(2)
print(f"{p1} Army is the {player_role}. {p2} Army is the {player_role}. \n")

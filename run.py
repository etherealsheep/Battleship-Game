import time
import random

objects = {
        'attacker': [
            'The Empire',
            'High Elf Army',
            'Dwarf Army',
            'Undead Horde',
            'Chaos Army',
            'Orc Horde'
        ],
        'defender': [
            'The Empire',
            'High Elf Army',
            'Dwarf Army',
            'Undead Horde',
            'Chaos Army',
            'Orc Horde'
        ],
        'daytime': [
            'dawn'
            'day',
            'sunset'
            'night'
        ],
        'weather': [
            'clear',
            'fog',
            'wind',
            'rain',
            'storm'
        ],
        'turns': [
            '6',
            '7',
            '8'
        ],
        'sceneryOne': [
            'hill',
            'wood',
            'river'
        ],
        'sceneryTwo': [
            'hill',
            'wood',
            'river'
        ],
        'sceneryThree': [
            'road',
            'building',
        ],
        'sceneryFour': [
            'road',
            'building',
            'hill',
            'wood',
            'river'
        ],
        'sceneryFive': [
            'fortified wall'
            'castle'
        ],
        'winner': [
            'The Empire',
            'High Elf Army',
            'Dwarf Army',
            'Undead Horde',
            'Chaos Army',
            'Orc Horde'
        ],
        'loser': [
            'The Empire',
            'High Elf Army',
            'Dwarf Army',
            'Undead Horde',
            'Chaos Army',
            'Orc Horde'
        ],
}


def banner():
    # Initial Banner.
    print("            ██╗    ██╗ █████╗ ██████╗")
    print("            ██║    ██║██╔══██╗██╔══██╗")
    print("            ██║ █╗ ██║███████║██████╔╝")
    print("            ██║███╗██║██╔══██║██╔══██╗")
    print("            ╚███╔███╔╝██║  ██║██║  ██║")
    print("             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
    print("███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗")
    print("████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
    print("██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝")
    print("██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗")
    print("██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║")
    print("╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
    print("██████╗  █████╗ ████████╗████████╗██╗     ███████╗")
    print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝")
    print("██████╔╝███████║   ██║      ██║   ██║     █████╗")
    print("██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝")
    print("██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗")
    print("╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝")
    print("            ██╗      ██████╗  ██████╗")
    print("            ██║     ██╔═══██╗██╔════╝")
    print("            ██║     ██║   ██║██║  ███╗")
    print("            ██║     ██║   ██║██║   ██║")
    print("            ███████╗╚██████╔╝╚██████╔╝")
    print("            ╚══════╝ ╚═════╝  ╚═════╝")
    time.sleep(3)


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

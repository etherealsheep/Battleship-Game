import time

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


def selectObject(key):
    # get the array of items. e.g: attacker, defender, daytime, etc...
    items = objects[key]
    # traverse the array with index "i"
    for i in range(len(items)):
        # print the index and the value in the menu
        print("{} - {}".format(i + 1, items[i]))
    # initialize selection in -1 (no selection)
    selection = -1
    # set validInput initial value to False
    # this variable controls the input validation
    validInput = False
    # "item" is the final value selected from the user menu
    item = None
    # this loop repeats until the user select
    # a valid option from the menu
    while not validInput:
        # ask the user to enter a number asociated to a value in the menu
        # listed above.
        input_value = input("Select a '{}' form the list above: [1..{}]\n"
                            .format(key, len(items)))
        # enclose in a try-except the intructions that could thrown
        # an exception to validate the user input
        # if entered value is not integer the ValueError exception is thrown
        # if integer value selected is not in the range of values
        # the IndexError is thrown when retrieving the items[selection-1]
        try:
            selection = int(input_value)
            item = items[selection-1]
            validInput = True
        except (ValueError, IndexError):
            validInput = False
    return item


def take_and_hold():
    print("*** TAKE AND HOLD (Scenario Tournament - 2000 Army Points)")
    print("The aim of this scenario is to fight over some objectives rather")
    print("than just breaking your opponent.")
    print("The attacker is {attacker}.")
    print("The defender is {defender}.")
    print(" ")
    print("* Special Rules")
    print("- Set up terrain and objectives: refer the drawing on the Ruleset.")
    print("- After {sceneryOne}, {sceneryTwo}, {sceneryThree}, {sceneryFour}")
    print("  and {sceneryFive} are set on the battlefield, players take turns")
    print("  starting from {attacker}, in placing four game objectives.")
    print("- After the objective are placed, {defender} starts deploying")
    print("  within {defender} deployment zone.")
    print("- This game has a number of turns equal to {turns}.")
    print("  {attacker} will start the first turn.")
    print("- Daytime and Weather condition are: {daytime} and {weather}.")
    print(" ")
    print("* Victory Points (VP)")
    print("- 2 VP for breaking the enemy")
    print("- 1 VP for holding objective in your deployment zone")
    print("- 2 VP for holding objective in central deployment zone")
    print("- 3 VP for holding objective in the opponent deployment zone")
    print(" ")
    print("WIN: {winner}      LOSE: {loser}")
    time.sleep(10)


def battle_for_the_tower():
    print("*** BATTLE FOR THE TOWER (Scenario Tournament - 2000 Army Points)")
    print("This scenario featurea a bloody struggle for a tower positioned")
    print("in the middle of the battlefield.")
    print("The attacker is {attacker}.")
    print("The defender is {defender}.")
    print(" ")
    print("* Special Rules")
    print("- Set up terrain and objectives: refer the drawing on the Ruleset.")
    print("- After {sceneryOne}, {sceneryTwo}, {sceneryThree}, {sceneryFour},")
    print("  {sceneryFive}, place a tower right in the middle of the table.")
    print("- After the terrains are placed, {defender} starts deploying")
    print("  within {defender} deployment zone.")
    print("- This game has a number of turns equal to {turns}.")
    print("  {attacker} will start the first turn.")
    print("- Daytime and Weather condition are: {daytime} and {weather}.")
    print(" ")
    print("* Victory Points (VP)")
    print("- 2 VP for breaking the enemy.")
    print("- 2 VP for controlling the tower.")
    print("- 1 VP extra if there is no enemy unit within 10cm of the tower.")
    print("- 1 VP extra if there is no enemy unit within 20cm of the tower.")
    print("       This bonus stacks with the pravious one.")
    print(" ")
    print("WIN: {winner}      LOSE: {loser}")
    time.sleep(10)
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
            'dawn',
            'day',
            'sunset',
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
        'sc_one': [
            'hill',
            'wood',
            'river'
        ],
        'sc_two': [
            'hill',
            'wood',
            'river'
        ],
        'sc_three': [
            'road',
            'building'
        ],
        'sc_four': [
            'road',
            'building',
            'hill',
            'wood',
            'river'
        ]
}


def banner():
    print("            ██╗    ██╗ █████╗ ██████╗")
    print("            ██║    ██║██╔══██╗██╔══██╗")
    print("            ██║ █╗ ██║███████║██████╔╝")
    print("            ██║███╗██║██╔══██║██╔══██╗")
    print("            ╚███╔███╔╝██║  ██║██║  ██║")
    print("███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗")
    print("████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
    print("██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝")
    print("██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗")
    print("██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║")
    print("██████╗  █████╗ ████████╗████████╗██╗═════███████╗")
    print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝")
    print("██████╔╝███████║   ██║      ██║   ██║     █████╗")
    print("██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝")
    print("██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗")
    print("╚═════╝ ╚═╝ ██╗╝   ╚═██████╗╚═██████╗════╝╚══════╝")
    print("            ██║     ██╔═══██╗██╔════╝")
    print("            ██║     ██║   ██║██║  ███╗")
    print("            ██║     ██║   ██║██║   ██║")
    print("            ███████╗╚██████╔╝╚██████╔╝")
    print("            ╚══════╝ ╚═════╝  ╚═════╝")
    time.sleep(3)


def select_obj(key):
    # get the array of items. e.g: attacker, defender, daytime, etc...
    items = objects[key]
    # traverse the array with index "i"
    for i in range(len(items)):
        # print the index and the value in the menu
        print("\n{} - {}".format(i + 1, items[i]))
    # initialize selection in -1 (no selection)
    selection = -1
    # set validInput initial value to False
    validInput = False
    # "item" is the final value selected from the user menu
    item = None
    # this loop repeats until the user select
    # a valid option from the menu
    while not validInput:
        # ask the user to enter a number asociated to a value in the menu
        # listed above.
        input_value = input("\nSelect a '{}' form the list above: [1..{}]\n"
                            .format(key, len(items)))
        print("o()xxxxx[{::::::::::::::::::::::::::::::::::::> \n")
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


def main():
    banner()
    while True:
        print("\n\n\no()xxxxx[{::::::::::::::::::::::::::::::::::::> \n")
        print("Choose from four tournament scenarios: \n")
        print("1. Take and Hold\n")
        print("2. Battle for the Tower\n")
        print("3. Defending the Village\n")
        print("4. Wagon Train\n")
        print("5. Exit \n")
        print("Make your choice: (1, 2, 3, 4):")
        choice = input()
        print("o()xxxx[{::::::::::::::::::::::::::::::::::> \n")
        if choice == "1":
            take_and_hold()
        elif choice == "2":
            battle_for_the_tower()
        elif choice == "3":
            defending_the_village()
        elif choice == "4":
            wagon_train()
        elif choice == "5":
            print(" ")
            print("████████╗ ██████╗     ████████╗██╗  ██╗███████╗")
            print("╚══██╔══╝██╔═══██╗    ╚══██╔══╝██║  ██║██╔════╝")
            print("   ██║   ██║   ██║       ██║   ███████║█████╗")
            print("   ██║   ██║   ██║       ██║   ██╔══██║██╔══╝")
            print("   ██║   ╚██████╔╝       ██║   ██║  ██║███████╗")
            print("   ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝")
            print("███╗   ██╗███████╗██╗  ██╗████████╗")
            print("████╗  ██║██╔════╝╚██╗██╔╝╚══██╔══╝")
            print("██╔██╗ ██║█████╗   ╚███╔╝    ██║")
            print("██║╚██╗██║██╔══╝   ██╔██╗    ██║")
            print("██║ ╚████║███████╗██╔╝ ██╗   ██║")
            print("╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝")
            print("██████╗  █████╗ ████████╗████████╗██╗     ███████╗")
            print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝")
            print("██████╔╝███████║   ██║      ██║   ██║     █████╗")
            print("██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝")
            print("██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗██╗██╗")
            print("╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚═╝╚═╝")
            print(" ")
            print("\n Press RUN PROGRAM to run again WarMaster Battle Log")

            time.sleep(2)
            break
        else:
            print("Please enter a valid option! \n\n")
            time.sleep(1)


def take_and_hold():
    attacker = select_obj('attacker')
    defender = select_obj('defender')
    daytime = select_obj('daytime')
    weather = select_obj('weather')
    turns = select_obj('turns')
    sc_one = select_obj('sc_one')
    sc_two = select_obj('sc_two')
    sc_three = select_obj('sc_three')
    sc_four = select_obj('sc_four')
    print("\n\n*** TAKE AND HOLD")
    print("The aim of this scenario is to fight over some objectives rather")
    print("than just breaking your opponent.")
    print(f"The attacker is {attacker}.")
    print(f"The defender is {defender}.")
    print(" ")
    print("* Special Rules")
    print("- Set up terrain and objectives: refer the drawing on the Ruleset.")
    print(f"- After {sc_one}, {sc_two}, {sc_three} and {sc_four}")
    print("  are set on the battlefield, players take turn")
    print(f"  starting from {attacker}, in placing four game objectives.")
    print(f"- After the objective are placed, {defender} starts deploying")
    print(f"  within {defender} deployment zone.")
    print(f"- This game has a number of turns equal to {turns}.")
    print(f"  {attacker} starts the first turn.")
    print(f"- Daytime and Weather condition are: {daytime} and {weather}.")
    print(" ")
    print("* Victory Points (VP)")
    print("- 2 VP for breaking the enemy")
    print("- 1 VP for holding objective in your deployment zone")
    print("- 2 VP for holding objective in central deployment zone")
    print("- 3 VP for holding objective in the opponent deployment zone")
    time.sleep(10)


def battle_for_the_tower():
    attacker = select_obj('attacker')
    defender = select_obj('defender')
    daytime = select_obj('daytime')
    weather = select_obj('weather')
    turns = select_obj('turns')
    sc_one = select_obj('sc_one')
    sc_two = select_obj('sc_two')
    sc_three = select_obj('sc_three')
    sc_four = select_obj('sc_four')
    print("\n\n*** BATTLE FOR THE TOWER")
    print("This scenario feature a bloody struggle for a tower positioned")
    print("in the middle of the battlefield.")
    print(f"The attacker is {attacker}.")
    print(f"The defender is {defender}.")
    print(" ")
    print("* Special Rules")
    print("- Set up terrain and objectives: refer the drawing on the Ruleset.")
    print(f"- After {sc_one}, {sc_two}, {sc_three}, {sc_four},")
    print("  place a tower right in the middle of the table.")
    print(f"- After the terrains are placed, {defender} starts deploying")
    print(f"  within {defender} deployment zone.")
    print(f"- This game has a number of turns equal to {turns}.")
    print(f"  {attacker} will start the first turn.")
    print(f"- Daytime and Weather condition are: {daytime} and {weather}.")
    print(" ")
    print("* Victory Points (VP)")
    print("- 2 VP for breaking the enemy.")
    print("- 2 VP for controlling the tower.")
    print("- 1 VP extra if there is no enemy unit within 10cm of the tower.")
    print("- 1 VP extra if there is no enemy unit within 20cm of the tower.")
    print("       This bonus stacks with the previous one.")
    time.sleep(10)


def defending_the_village():
    attacker = select_obj('attacker')
    defender = select_obj('defender')
    daytime = select_obj('daytime')
    weather = select_obj('weather')
    turns = select_obj('turns')
    sc_one = select_obj('sc_one')
    sc_two = select_obj('sc_two')
    sc_three = select_obj('sc_three')
    sc_four = select_obj('sc_four')
    print("\n\n*** DEFENDING THE VILLAGE")
    print(f"{defender} is defending a village and farmsteads against")
    print(f"{attacker} raiding the region. {attacker} aim is to ")
    print("burn down as many of the buildings as possible.")
    print(f"The attacker is {attacker}.")
    print(f"The defender is {defender}.")
    print(" ")
    print("* Special Rules")
    print("- Detail about scenario deployment detail are in the Rulebook.")
    print(f"- After {sc_one}, {sc_two}, {sc_three}, {sc_four}")
    print(f"  place a village in {defender} corner.")
    print(f"- After the terrains are placed, {defender} starts deploying")
    print(f"  within {defender} deployment zone.")
    print(f"- This game has a number of turns equal to {turns}.")
    print(f"- {defender} will start the first turn.")
    print(f"- Daytime and Weather condition are: {daytime} and {weather}.")
    print(" ")
    print("* Victory Points (VP)")
    print("- 2 VP for braking the enemy")
    print("- 2 VP for {attacker} for every burnt building.")
    print("- 1 VP for {defender} for every burnt building.")
    print("- 3 VP for {attacker} for burning the village.")
    time.sleep(10)


def wagon_train():
    attacker = select_obj('attacker')
    defender = select_obj('defender')
    daytime = select_obj('daytime')
    weather = select_obj('weather')
    turns = select_obj('turns')
    sc_one = select_obj('sc_one')
    sc_two = select_obj('sc_two')
    sc_three = select_obj('sc_three')
    sc_four = select_obj('sc_four')
    print("\n\n*** WAGON TRAIN")
    print("A supply wagon train escorted by a patrol force is ambushed")
    print(f"by {attacker}. {defender} task is to protect and get")
    print("to safety as many as wagons are possible.")
    print(f"The attacker is {attacker}.")
    print(f"The defender is {defender}.")
    print(" ")
    print("* Special Rules")
    print("- Detail about scenario deployment detail are in the Rulebook.")
    print(f"- After {sc_one}, {sc_two}, {sc_three}, {sc_four}")
    print(f"  add road in the middle of the table. {defender} place 6 wagons")
    print("  on the road. No wagon is more than halfway across the table.")
    print(f"- After the objectives are placed, {defender} starts")
    print(f"  deploying within {defender} deployment zone.")
    print(f"  {attacker} starts the first turn. Game Length: {turns} turns.")
    print(f"- Daytime and Weather condition are: {daytime} and {weather}.")
    print(" ")
    print("* Victory Points (VP)")
    print("- 2 VP for braking the enemy")
    print("- 1 VP for {attacker} for every wagon destroyed in melee.")
    print("- 3 VP for {attacker} for every wagon destroyed and looted.")
    print("- 1 VP for {defender} for every wagon non destroyed.")
    time.sleep(10)


main()
